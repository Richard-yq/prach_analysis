#!/usr/bin/env python3
"""
OTA CBRA timing experiment — USRP gNB + COTS UE (airplane mode via ADB/SSH)

Per run:
  1. Airplane mode ON  (ensure UE is disconnected before starting)
  2. Kill any existing gNB, start fresh
  3. t1 = wall-clock time when gNB prints "CMDLINE:"
  4. Wait for gNB scheduler (Frame.Slot) before releasing UE
  5. Airplane mode OFF → UE starts camping / RA procedure
  6. t2 = wall-clock time when gNB prints "Received Ack of Msg4. CBRA procedure succeeded"
  7. Airplane mode ON  (clean up UE connection)
  delta = t2 - t1  → saved to CSV

Run:
  sudo python3 /home/oaignb/cbra_ota_timing.py
"""

import csv
import os
import signal
import subprocess
import threading
import time
from datetime import datetime

import paramiko

# ── gNB ─────────────────────────────────────────────────────────────────────
GNB_BUILD_DIR = "/home/oaignb/openairinterface5g/cmake_targets/ran_build/build"
GNB_CONF      = "/home/oaignb/richard-config/OAI_gNB_twoFDM.conf"
GNB_LOG_FILE  = "/home/oaignb/OAI_gNB.log"
OUTPUT_CSV    = "/home/oaignb/cbra_ota_timing.csv"

N_RUNS          = 240  # 10 already done → total 250
TIMEOUT_GNB_RDY = 60    # seconds: wait for gNB Frame.Slot (USRP init can be slow)
TIMEOUT_CBRA    = 120   # seconds: wait for CBRA success after airplane off
COOLDOWN        = 5     # seconds between runs (let USRP / sockets settle)

GNB_CMD = [
    "sudo", "./nr-softmodem",
    "-O", GNB_CONF,
    "--gNBs.[0].min_rxtxtime", "6",
    "-E",
    "--continuous-tx",
    "--log_config.PRACH_debug",
    "--telnetsrv",
    "--telnetsrv.shrmod", "o1",
]

# ── UE control PC ────────────────────────────────────────────────────────────
CTL_HOST = "192.168.8.102"
CTL_USER = "control-PC"
CTL_PASS = "bmwlab"


# ─────────────────────────────────────────────────────────────────────────────
# SSH helper (persistent connection with auto-reconnect)
# ─────────────────────────────────────────────────────────────────────────────

class SSHRunner:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self._client = None
        self._lock = threading.Lock()
        self._connect()

    def _connect(self):
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            # try password auth first
            c.connect(self.host, username=self.user, password=self.password,
                      look_for_keys=False, allow_agent=False, timeout=10)
        except paramiko.AuthenticationException:
            # Windows 11 OpenSSH often requires keyboard-interactive even when
            # "password" is listed; fall back to interactive with password answer
            t = paramiko.Transport((self.host, 22))
            t.start_client(timeout=10)
            t.auth_interactive_dumb(self.user,
                                    lambda title, inst, fields: [self.password] * len(fields))
            c._transport = t
        self._client = c
        print(f"[SSH] connected to {self.host}")

    def run(self, cmd, retries=2):
        with self._lock:
            for attempt in range(retries):
                try:
                    if self._client is None or not self._client.get_transport().is_active():
                        self._connect()
                    _, stdout, _ = self._client.exec_command(cmd, timeout=30)
                    return stdout.read().decode("utf-8", errors="replace").strip()
                except Exception as e:
                    if attempt < retries - 1:
                        print(f"[SSH] retrying ({e})")
                        time.sleep(1)
                        try:
                            self._connect()
                        except Exception:
                            pass
                    else:
                        raise

    def close(self):
        if self._client:
            self._client.close()


_ctl_ssh: SSHRunner | None = None

def ctl_ssh() -> SSHRunner:
    global _ctl_ssh
    if _ctl_ssh is None:
        _ctl_ssh = SSHRunner(CTL_HOST, CTL_USER, CTL_PASS)
    return _ctl_ssh


# ─────────────────────────────────────────────────────────────────────────────
# ADB helpers
# ─────────────────────────────────────────────────────────────────────────────

_adb_device: str | None = None

def get_adb_device() -> str:
    global _adb_device
    if _adb_device:
        return _adb_device
    out = ctl_ssh().run("adb devices")
    for line in out.splitlines()[1:]:
        line = line.strip()
        if line and not line.startswith("*") and "\t" in line:
            dev, status = line.split("\t", 1)
            if status.strip() == "device":
                _adb_device = dev.strip()
                print(f"[ADB] device: {_adb_device}")
                return _adb_device
    raise RuntimeError(f"No ADB device found on {CTL_HOST}. adb devices:\n{out}")


def toggle_airplane_mode(state: str) -> bool:
    """Toggle airplane mode on COTS UE via ADB. state = 'on' | 'off'."""
    assert state in ("on", "off")
    dev = get_adb_device()
    val = "1" if state == "on" else "0"
    broadcast_state = "true" if state == "on" else "false"

    ctl_ssh().run(
        f'adb -s {dev} shell "settings put global airplane_mode_on {val}"'
    )
    ctl_ssh().run(
        f'adb -s {dev} shell "am broadcast -a android.intent.action.AIRPLANE_MODE --ez state {broadcast_state}"'
    )
    time.sleep(0.5)  # let Android apply the setting

    # verify
    result = ctl_ssh().run(
        f'adb -s {dev} shell "settings get global airplane_mode_on"'
    )
    if result.strip() == val:
        print(f"[ADB] airplane mode {state} verified")
        return True
    else:
        print(f"[ADB] WARNING: airplane mode {state} not confirmed (got '{result}')")
        return False


# ─────────────────────────────────────────────────────────────────────────────
# gNB process helpers
# ─────────────────────────────────────────────────────────────────────────────

def _kill_gnb():
    """Kill any existing nr-softmodem processes."""
    os.system("sudo pkill -9 nr-softmodem 2>/dev/null")
    time.sleep(2)
    if subprocess.run(["pgrep", "-x", "nr-softmodem"],
                      capture_output=True).returncode == 0:
        os.system("sudo killall -9 nr-softmodem 2>/dev/null")
        time.sleep(1)


def _kill_proc(proc):
    if proc is None or proc.poll() is not None:
        return
    try:
        pgid = os.getpgid(proc.pid)
        os.killpg(pgid, signal.SIGTERM)
        for _ in range(30):
            if proc.poll() is not None:
                return
            time.sleep(0.1)
        os.killpg(pgid, signal.SIGKILL)
    except ProcessLookupError:
        pass


def _gnb_reader(proc, events: dict, log_fh):
    """
    Read gNB stdout line by line.
    - Prepend wall-clock timestamp and write to log file (matches awk format)
    - Record time.time() on keyword hits
    """
    WATCH = [
        ("gnb_cmdline", "CMDLINE:"),
        ("gnb_ready",   "Frame.Slot"),
        ("cbra_success", "Received Ack of Msg4. CBRA procedure succeeded"),
    ]
    try:
        for raw in iter(proc.stdout.readline, b""):
            line = raw.decode("utf-8", errors="replace").rstrip()
            ts_str = datetime.now().strftime("[%Y-%m-%d %H:%M:%S.%f]")[:-4] + "]"
            log_line = f"{ts_str} {line}"
            if log_fh:
                log_fh.write(log_line + "\n")
                log_fh.flush()
            for key, kw in WATCH:
                if key not in events and kw in line:
                    events[key] = time.time()
                    ts = datetime.fromtimestamp(events[key]).strftime("%H:%M:%S.%f")[:-3]
                    print(f"  [gNB] {ts}  {line[:100]}")
    except Exception:
        pass


# ─────────────────────────────────────────────────────────────────────────────
# Single experiment run
# ─────────────────────────────────────────────────────────────────────────────

def run_one(n: int) -> dict | None:
    print(f"\n{'─'*60}")
    print(f"Run {n}  [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
    print('─'*60)

    events: dict[str, float] = {}
    gnb = None

    try:
        # ── step 1: ensure UE is disconnected ───────────────────────────────
        print("  [1] Airplane mode ON ...")
        toggle_airplane_mode("on")

        # ── step 2: kill old gNB, start fresh ───────────────────────────────
        print("  [2] Starting gNB ...")
        _kill_gnb()

        log_fh = open(GNB_LOG_FILE, "w")
        gnb = subprocess.Popen(
            GNB_CMD, cwd=GNB_BUILD_DIR,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            preexec_fn=os.setsid,
        )
        threading.Thread(
            target=_gnb_reader,
            args=(gnb, events, log_fh),
            daemon=True,
        ).start()

        # ── step 3: wait for gNB ready (Frame.Slot = scheduler running) ─────
        deadline = time.time() + TIMEOUT_GNB_RDY
        while "gnb_ready" not in events:
            if time.time() > deadline:
                print("  FAIL: gNB did not reach Frame.Slot within timeout")
                return None
            if gnb.poll() is not None:
                print("  FAIL: gNB exited unexpectedly")
                return None
            time.sleep(0.1)

        # ── step 4: release UE ───────────────────────────────────────────────
        print("  [4] Airplane mode OFF → UE starts RA ...")
        toggle_airplane_mode("off")

        # ── step 5: wait for CBRA success ────────────────────────────────────
        deadline = time.time() + TIMEOUT_CBRA
        while "cbra_success" not in events:
            if time.time() > deadline:
                print("  FAIL: CBRA not completed within timeout")
                return None
            if gnb.poll() is not None:
                print("  FAIL: gNB exited during RA procedure")
                return None
            time.sleep(0.1)

        # ── step 6: disconnect UE ────────────────────────────────────────────
        print("  [6] Airplane mode ON (cleanup) ...")
        toggle_airplane_mode("on")

        # compute delta
        t1 = events.get("gnb_cmdline", events["gnb_ready"])
        t2 = events["cbra_success"]
        delta = round(t2 - t1, 3)
        print(f"\n  OK  CMDLINE → CBRA success: {delta:.3f} s")

        return {
            "run":               n,
            "gnb_cmdline_time":  datetime.fromtimestamp(t1).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],
            "cbra_success_time": datetime.fromtimestamp(t2).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],
            "delta_sec":         delta,
            "status":            "ok",
        }

    except Exception as exc:
        print(f"  EXCEPTION: {exc}")
        return {"run": n, "gnb_cmdline_time": "", "cbra_success_time": "",
                "delta_sec": "", "status": f"error: {exc}"}

    finally:
        _kill_proc(gnb)
        _kill_gnb()
        try:
            log_fh.close()
        except Exception:
            pass
        time.sleep(COOLDOWN)


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    FIELDS = ["run", "gnb_cmdline_time", "cbra_success_time", "delta_sec", "status"]
    new_file = not os.path.exists(OUTPUT_CSV)

    # probe SSH + ADB once before starting loop
    print("Connecting to control PC ...")
    dev = get_adb_device()
    print(f"ADB device: {dev}")
    print(f"Output CSV: {OUTPUT_CSV}")
    print(f"Starting {N_RUNS} runs ...\n")

    results = []
    with open(OUTPUT_CSV, "a", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        if new_file:
            writer.writeheader()

        for i in range(1, N_RUNS + 1):
            row = run_one(i)
            if row:
                results.append(row)
                writer.writerow(row)
                fh.flush()

    # summary
    ok = [r for r in results if r["status"] == "ok"]
    if ok:
        deltas = [float(r["delta_sec"]) for r in ok]
        print(f"\n{'='*60}")
        print(f"Summary  ({len(ok)}/{N_RUNS} successful)")
        print(f"  mean  : {sum(deltas)/len(deltas):.3f} s")
        print(f"  min   : {min(deltas):.3f} s")
        print(f"  max   : {max(deltas):.3f} s")
        print(f"  CSV   : {OUTPUT_CSV}")
    else:
        print("\nNo successful runs.")

    if _ctl_ssh:
        _ctl_ssh.close()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
OAI gNB log monitor
t1 : log timestamp of CMDLINE line  (gNB restart)
t2 : log timestamp of first Frame.Slot after restart
dur: t2 - t1 in seconds (3 decimal places)
"""

import os
import re
import csv
import time
import datetime

LOG_FILE = "/home/oaignb/OAI_gNB.log"
CSV_FILE = "/home/oaignb/experiment-duration.csv"

TS_RE = re.compile(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3})\]')


def parse_ts(line: str):
    m = TS_RE.search(line)
    if m:
        return datetime.datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S.%f")
    return None


def ensure_header(path: str):
    if not os.path.exists(path):
        with open(path, "w", newline="") as f:
            csv.writer(f).writerow(["experiment", "t1_cmdline", "t2_frame_slot", "duration_sec"])


def save_row(path: str, exp: int, t1: str, t2: str, dur: float):
    with open(path, "a", newline="") as f:
        csv.writer(f).writerow([exp, t1, t2, f"{dur:.3f}"])


def open_log(path: str):
    f = open(path, "r", errors="replace")
    st = os.stat(path)
    return f, st.st_ino, st.st_size


def main():
    ensure_header(CSV_FILE)

    state = 0   # 0 = waiting CMDLINE,  1 = waiting Frame.Slot
    exp_num = 0
    t1_str, t1_dt = None, None

    while not os.path.exists(LOG_FILE):
        print(f"Waiting for {LOG_FILE} ...")
        time.sleep(1)

    f, inode, _ = open_log(LOG_FILE)
    f.seek(0, 2)            # start from current end
    pos = f.tell()

    print(f"Monitoring : {LOG_FILE}")
    print(f"CSV output : {CSV_FILE}")
    print("Waiting for next gNB restart (CMDLINE) ...\n")

    try:
        while True:
            # ── check file state ────────────────────────────────────────────
            try:
                st = os.stat(LOG_FILE)
            except FileNotFoundError:
                f.close()
                print("Log file gone, waiting ...")
                while not os.path.exists(LOG_FILE):
                    time.sleep(1)
                f, inode, _ = open_log(LOG_FILE)
                f.seek(0, 2)
                pos = f.tell()
                continue

            # file truncated or rotated → reopen from start
            if st.st_ino != inode or st.st_size < pos:
                f.close()
                f, inode, _ = open_log(LOG_FILE)
                f.seek(0)
                pos = 0

            line = f.readline()
            if not line:
                time.sleep(0.05)
                continue
            pos = f.tell()

            # ── state machine ───────────────────────────────────────────────
            if state == 0:
                if 'CMDLINE: "./nr-softmodem"' in line:
                    ts = parse_ts(line)
                    if ts:
                        t1_str = ts.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
                        t1_dt  = ts
                        state  = 1
                        print(f"[t1] CMDLINE     {t1_str}")

            elif state == 1:
                if "Frame.Slot" in line and "NR_MAC" in line:
                    ts = parse_ts(line)
                    if ts:
                        t2_str = ts.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
                        dur    = (ts - t1_dt).total_seconds()
                        exp_num += 1
                        save_row(CSV_FILE, exp_num, t1_str, t2_str, dur)
                        print(f"[t2] Frame.Slot  {t2_str}")
                        print(f"     duration = {dur:.3f} s  →  exp {exp_num} saved\n")
                        state  = 0
                        t1_str = t1_dt = None

    except KeyboardInterrupt:
        print("\nStopped.")
        f.close()


if __name__ == "__main__":
    main()

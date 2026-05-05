#!/usr/bin/env python3
"""
Plot oai-fdm16.log: 3-panel RACH overload visualization.

Figure 1 – Congestion overview: per-RO preamble detected vs accepted
Figure 2 – UE lifecycle Gantt: RA init → Msg3 initial → retx(1,2,3) → fail
Figure 3 – Msg3 RB resource grid: initial (solid) + retransmissions (hatched)
"""

import re
from pathlib import Path
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

LOG_FILE = Path(__file__).parent / "oai-fdm16.log"
OUT_DIR  = Path(__file__).parent
ANSI_ESCAPE = re.compile(r"\x1b\[[0-9;]*m")

# ── regex patterns ────────────────────────────────────────────────────────────
RAPROC_PAT = re.compile(
    r"\[RAPROC\] Frame (\d+), slot (\d+), fdm (\d+)"
)
NO_FREE_PAT = re.compile(
    r"FAILURE:\s+(\d+)\.(\d+) initiating RA procedure for preamble index \d+: no free RA process"
)
RA_INIT_PAT = re.compile(
    r"(\d+)\.(\d+) UE RA-RNTI [0-9a-f]+ TC-RNTI ([0-9a-f]+): initiating RA procedure"
)
MSG3_PAT = re.compile(
    r"UE ([0-9a-f]+): Msg3 scheduled at (\d+)\.(\d+) "
    r"\((\d+)\.(\d+) TDA (\d+)\) start (\d+) RBs (\d+)"
)
RETX_PAT = re.compile(
    r"RA RNTI ([0-9a-f]+) CC_id 0 Scheduling retransmission of Msg3 in \((\d+),(\d+)\)"
)
FAIL_MSG3_PAT = re.compile(
    r"UE ([0-9a-f]+) RA failed at state WAIT_Msg3"
)
RAPID_PAT = re.compile(
    r"UE ([0-9a-f]+):.*preamble_index\(RAPID\) (\d+)"
)


def parse(path: Path):
    raproc   = defaultdict(int)   # (frame,slot) → detected count
    no_free  = defaultdict(int)   # (frame,slot) → dropped count
    ra_init  = {}                 # tc_rnti → (frame, slot)
    msg3     = {}                 # tc_rnti → dict
    retxs    = defaultdict(list)  # tc_rnti → [(frame, slot)]
    ra_fail  = {}                 # tc_rnti → (frame, slot) when failed
    rapids   = {}                 # tc_rnti → preamble index (RAPID)

    with open(path, "r", errors="replace") as f:
        for line in f:
            line = ANSI_ESCAPE.sub("", line)

            m = RAPROC_PAT.search(line)
            if m:
                raproc[(int(m[1]), int(m[2]))] += 1
                continue

            m = NO_FREE_PAT.search(line)
            if m:
                no_free[(int(m[1]), int(m[2]))] += 1
                continue

            m = RA_INIT_PAT.search(line)
            if m:
                tc = m[3]
                ra_init[tc] = (int(m[1]), int(m[2]))
                continue

            m = RAPID_PAT.search(line)
            if m:
                rapids[m[1]] = int(m[2])
                continue

            m = MSG3_PAT.search(line)
            if m:
                tc = m[1]
                msg3[tc] = {
                    "sched_frame": int(m[2]), "sched_slot": int(m[3]),
                    "tx_frame":    int(m[4]), "tx_slot":    int(m[5]),
                    "rb_start":    int(m[7]), "rb_count":   int(m[8]),
                }
                continue

            m = RETX_PAT.search(line)
            if m:
                tc = m[1]
                retxs[tc].append((int(m[2]), int(m[3])))
                continue

            m = FAIL_MSG3_PAT.search(line)
            if m:
                tc = m[1]
                if retxs[tc]:
                    ra_fail[tc] = retxs[tc][-1]
                elif tc in msg3:
                    ra_fail[tc] = (msg3[tc]["tx_frame"], msg3[tc]["tx_slot"])

    return raproc, no_free, ra_init, msg3, retxs, ra_fail, rapids


def frame_ms(frame, slot=0):
    """NR frame.slot → time in ms (μ=1, 30kHz SCS, 0.5ms/slot)."""
    return frame * 10.0 + slot * 0.5


# ── Figure 1: RACH Congestion Overview ───────────────────────────────────────
def plot_congestion(raproc, no_free, ra_init):
    # Build per-RO table: (frame,slot) → (detected, accepted, dropped)
    all_ro = sorted(set(raproc) | set(no_free))
    # accepted per RO ≈ count of ra_inits whose (frame,slot) == RO
    init_per_ro = defaultdict(int)
    for tc, (fr, sl) in ra_init.items():
        init_per_ro[(fr, sl)] += 1

    detected = [raproc[ro] for ro in all_ro]
    dropped  = [no_free[ro] for ro in all_ro]
    accepted = [init_per_ro[ro] for ro in all_ro]

    x      = np.arange(len(all_ro))
    labels = [f"{f}.{s}" for f, s in all_ro]

    fig, ax = plt.subplots(figsize=(min(2 + len(all_ro) * 0.55, 24), 5))

    w = 0.6
    # stacked bar: accepted (green) at bottom, dropped (red) on top
    ax.bar(x, accepted, w, label="Accepted into RA process", color="#2ecc71", zorder=3)
    ax.bar(x, dropped,  w, bottom=accepted,
                   label="Dropped (no free RA process)", color="#e74c3c", zorder=3, alpha=0.85)

    # capacity line
    ax.axhline(4, color="#2c3e50", linewidth=1.5, linestyle="--",
               label="Max RA processes (4)", zorder=4)

    # annotate total detected on very congested bars
    for xi, (acc, drp) in enumerate(zip(accepted, dropped)):
        total = acc + drp
        if total > 5:
            ax.text(xi, total + 1.5, str(total), ha="center", va="bottom",
                    fontsize=7, color="#e74c3c", fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=55, ha="right", fontsize=7)
    ax.set_xlabel("RACH Occasion (frame.slot)", fontsize=10)
    ax.set_ylabel("Preamble Count", fontsize=10)
    ax.set_title(
        "RACH Congestion: Per-Occasion Preamble Accepted vs Dropped\n"
        f"Total detected: {sum(detected)}  |  Accepted: {sum(accepted)}  |  "
        f"Dropped: {sum(dropped)}  ({100*sum(dropped)/max(sum(detected),1):.0f}% rejection rate)",
        fontsize=11, fontweight="bold"
    )
    ax.legend(fontsize=9, loc="upper right")
    ax.grid(axis="y", linestyle="--", linewidth=0.4, alpha=0.5, zorder=0)
    ax.set_ylim(0, max(detected) * 1.25 if detected else 10)

    plt.tight_layout()
    out = OUT_DIR / "fdm16_fig1_congestion.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved → {out}")


# ── Figure 2: UE Lifecycle Gantt ─────────────────────────────────────────────
def plot_gantt(ra_init, msg3, retxs, ra_fail):
    """Heatmap layout: one row per UE, one column per frame, colored by RA state.
    Gives every lifecycle equal visual weight regardless of total time span.
    """
    from matplotlib.colors import ListedColormap

    ues = sorted(ra_init.keys(), key=lambda tc: ra_init[tc][0] * 20 + ra_init[tc][1])

    # State codes (priority order: higher wins when multiple apply)
    S_INACTIVE = 0
    S_RA_INIT  = 1
    S_MSG3     = 2
    S_RETX1    = 3
    S_RETX2    = 4
    S_RETX3    = 5
    S_FAILED   = 6

    # Frame range across all UEs
    all_frames = [ra_init[tc][0] for tc in ues]
    all_frames += [msg3[tc]["tx_frame"] for tc in ues if tc in msg3]
    for tc in ues:
        all_frames += [f for f, _ in retxs.get(tc, [])]
    all_frames += [ra_fail[tc][0] for tc in ues if tc in ra_fail]
    f_min = min(all_frames) - 1
    f_max = max(all_frames) + 4
    n_frames = f_max - f_min + 1

    grid = np.zeros((len(ues), n_frames), dtype=np.int8)

    for yi, tc in enumerate(ues):
        init_fr = ra_init[tc][0]

        if tc not in msg3:
            fi = init_fr - f_min
            if 0 <= fi < n_frames:
                grid[yi, fi] = S_RA_INIT
            continue

        m = msg3[tc]
        msg3_fr = m["tx_frame"]

        # RA init → Msg3 gap
        for f in range(init_fr, msg3_fr):
            fi = f - f_min
            if 0 <= fi < n_frames:
                grid[yi, fi] = S_RA_INIT

        # Msg3 initial TX frame
        fi = msg3_fr - f_min
        if 0 <= fi < n_frames:
            grid[yi, fi] = S_MSG3

        # Retransmissions
        retx_states = [S_RETX1, S_RETX2, S_RETX3]
        prev_fr = msg3_fr
        for ri, (rfr, _) in enumerate(retxs.get(tc, [])):
            s = retx_states[min(ri, 2)]
            for f in range(prev_fr + 1, rfr + 1):
                fi = f - f_min
                if 0 <= fi < n_frames:
                    grid[yi, fi] = s
            prev_fr = rfr

        # Failure: mark one frame red
        if tc in ra_fail:
            fail_fr = ra_fail[tc][0]
            fi = fail_fr - f_min
            if 0 <= fi < n_frames:
                grid[yi, fi] = S_FAILED
            # Clear frames after failure
            for f in range(fail_fr + 1, f_max + 1):
                fi = f - f_min
                if 0 <= fi < n_frames:
                    grid[yi, fi] = S_INACTIVE

    PALETTE = [
        "#e8e8e8",  # 0 inactive – light grey
        "#3498db",  # 1 RA init  – blue
        "#27ae60",  # 2 Msg3 TX  – green
        "#f1c40f",  # 3 Retx 1   – yellow
        "#e67e22",  # 4 Retx 2   – orange
        "#d35400",  # 5 Retx 3   – dark orange
        "#c0392b",  # 6 Failed   – red
    ]
    cmap = ListedColormap(PALETTE)

    fig_h = max(6, len(ues) * 0.22)
    fig, ax = plt.subplots(figsize=(20, fig_h))

    ax.imshow(grid, aspect="auto", cmap=cmap, vmin=0, vmax=6,
              interpolation="nearest", origin="upper")

    tick_step = max(1, n_frames // 25)
    tick_pos   = list(range(0, n_frames, tick_step))
    ax.set_xticks(tick_pos)
    ax.set_xticklabels([str(f_min + p) for p in tick_pos], fontsize=8, rotation=45, ha="right")

    ax.set_yticks(range(len(ues)))
    ax.set_yticklabels([f"0x{tc}" for tc in ues], fontsize=6.5)

    ax.set_xlabel("Frame Number", fontsize=11)
    ax.set_ylabel("TC-RNTI (each row = one UE)", fontsize=11)
    ax.set_title(
        f"UE RA Lifecycle Heatmap — All {len(ues)} UEs End in Failure\n"
        "Blue → Green → Yellow/Orange (retx) → Red (failed) — no UE reaches success",
        fontsize=12, fontweight="bold"
    )

    legend_items = [
        mpatches.Patch(facecolor=PALETTE[1], label="RA Initiated"),
        mpatches.Patch(facecolor=PALETTE[2], label="Msg3 Initial TX"),
        mpatches.Patch(facecolor=PALETTE[3], label="Msg3 Retx 1"),
        mpatches.Patch(facecolor=PALETTE[4], label="Msg3 Retx 2"),
        mpatches.Patch(facecolor=PALETTE[5], label="Msg3 Retx 3"),
        mpatches.Patch(facecolor=PALETTE[6], label="RA FAILED"),
    ]
    ax.legend(handles=legend_items, loc="upper right", fontsize=9,
              ncol=3, framealpha=0.92)

    plt.tight_layout()
    out = OUT_DIR / "fdm16_fig2_gantt.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved → {out}")


# ── Figure 3: Msg3 RB Resource Grid (initial + retx), split into two slides ───
def _draw_rb_panel(ax, chunk_occasions, msg3, retxs, ra_fail, rapids,
                   colors, max_rb, part_idx, n_parts):
    """Draw one panel of the RB grid onto ax."""
    occ_idx  = {o: i for i, o in enumerate(chunk_occasions)}
    HATCH_RETX = ["///", "xxx", "..."]

    for tc, m in msg3.items():
        occ_init = (m["tx_frame"], m["tx_slot"])
        col      = colors[tc]
        rb0, rbc = m["rb_start"], m["rb_count"]
        failed   = tc in ra_fail
        rapid    = rapids.get(tc, None)
        # label: "P<n>" if RAPID known, else short RNTI
        blabel = f"P{rapid}" if rapid is not None else tc[:3]

        # Initial TX — solid
        if occ_init in occ_idx:
            xi = occ_idx[occ_init]
            rect = mpatches.FancyBboxPatch(
                (xi - 0.42, rb0), 0.84, rbc,
                boxstyle="round,pad=0.03",
                facecolor=col, edgecolor="white", linewidth=0.8,
                alpha=0.95, zorder=3,
            )
            ax.add_patch(rect)
            ax.text(xi, rb0 + rbc / 2, blabel,
                    ha="center", va="center", fontsize=7.5,
                    color="white", fontweight="bold")

        # Retransmissions — hatched, progressively lighter
        for ri, (rfr, rsl) in enumerate(retxs.get(tc, [])):
            occ_rx = (rfr, rsl)
            if occ_rx not in occ_idx:
                continue
            xi    = occ_idx[occ_rx]
            alpha = max(0.35, 0.8 - ri * 0.15)
            rect  = mpatches.FancyBboxPatch(
                (xi - 0.42, rb0), 0.84, rbc,
                boxstyle="round,pad=0.03",
                facecolor=col, edgecolor="white", linewidth=0.5,
                hatch=HATCH_RETX[min(ri, 2)],
                alpha=alpha, zorder=3,
            )
            ax.add_patch(rect)
            rlabel = f"R{ri+1}"
            ax.text(xi, rb0 + rbc / 2, rlabel,
                    ha="center", va="center", fontsize=6.5,
                    color="white", fontweight="bold")

        # Failure marker on last retx (or init)
        if failed:
            last_retx = retxs.get(tc, [])
            last_occ  = last_retx[-1] if last_retx else occ_init
            if last_occ in occ_idx:
                xi = occ_idx[last_occ]
                ax.text(xi, rb0 + rbc * 0.88,
                        "✗", ha="center", va="bottom",
                        fontsize=9, color="#c0392b", fontweight="bold", zorder=6)

    c_labels = [f"{f}.{s}" for f, s in chunk_occasions]
    ax.set_xlim(-0.5, len(chunk_occasions) - 0.5)
    ax.set_ylim(-0.5, max_rb)
    ax.set_xticks(range(len(chunk_occasions)))
    ax.set_xticklabels(c_labels, rotation=50, ha="right", fontsize=8)
    ax.set_xlabel("TX frame.slot", fontsize=10)
    ax.set_ylabel("RB Index", fontsize=10)
    ax.set_yticks(range(0, max_rb + 1, 4))
    ax.grid(axis="y", linestyle="--", linewidth=0.35, alpha=0.45, zorder=0)
    ax.set_title(
        f"Msg3 RB Allocations: Initial TX + Retransmissions  (Part {part_idx}/{n_parts})\n"
        "Label = Preamble index (P#);  R1/R2/R3 = HARQ retransmission rounds  |  "
        "✗ = RA failed",
        fontsize=10.5, fontweight="bold",
    )

    legend_items = [
        mpatches.Patch(facecolor="gray", edgecolor="white",
                       label="Solid   = Msg3 initial TX"),
        mpatches.Patch(facecolor="gray", hatch="///", alpha=0.75,
                       edgecolor="white", label="R1 = 1st retx"),
        mpatches.Patch(facecolor="gray", hatch="xxx", alpha=0.60,
                       edgecolor="white", label="R2 = 2nd retx"),
        mpatches.Patch(facecolor="gray", hatch="...", alpha=0.45,
                       edgecolor="white", label="R3 = 3rd retx"),
        mpatches.Patch(facecolor="#c0392b", label="✗  RA failed"),
    ]
    ax.legend(handles=legend_items, loc="upper right", fontsize=8,
              framealpha=0.88, ncol=5)


def plot_rb_grid(msg3, retxs, ra_fail, rapids, slots_per_part=15, total_slots=30):
    # Collect all tx occasions (frame, slot)
    all_occasions = set()
    for tc, m in msg3.items():
        all_occasions.add((m["tx_frame"], m["tx_slot"]))
        for fr, sl in retxs.get(tc, []):
            all_occasions.add((fr, sl))

    occasions = sorted(all_occasions)[:total_slots]
    max_rb    = max((m["rb_start"] + m["rb_count"] - 1) for m in msg3.values()) + 2

    # Per-UE colour (consistent across parts)
    ues    = sorted(msg3.keys())
    cmap   = matplotlib.colormaps.get_cmap("tab20").resampled(max(len(ues), 1))
    colors = {tc: cmap(i) for i, tc in enumerate(ues)}

    # Split into parts
    chunks  = [occasions[i:i + slots_per_part]
               for i in range(0, len(occasions), slots_per_part)]
    n_parts = len(chunks)

    for pi, chunk in enumerate(chunks, start=1):
        fig_w = 2 + len(chunk) * 0.85   # ~slide-friendly width
        fig, ax = plt.subplots(figsize=(fig_w, 7))
        _draw_rb_panel(ax, chunk, msg3, retxs, ra_fail, rapids,
                       colors, max_rb, pi, n_parts)
        plt.tight_layout()
        out = OUT_DIR / f"fdm16_fig3_rb_grid_part{pi}.png"
        plt.savefig(out, dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"Saved → {out}")


# ── Figure 4: Summary panel (small, shareable) ───────────────────────────────
def plot_summary(raproc, no_free, ra_init, msg3, retxs, ra_fail):
    total_detected = sum(raproc.values())
    total_accepted = len(ra_init)
    total_dropped  = sum(no_free.values())
    total_failed   = len(ra_fail)
    total_msg3     = len(msg3)
    total_retx     = sum(len(v) for v in retxs.values())

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle(
        "oai-fdm16.log — RACH Overload Summary\n"
        "(Simulation: 64 simultaneous preambles, max 4 RA processes)",
        fontsize=13, fontweight="bold"
    )

    # ─ Pie: preamble fate ────────────────────────────────────────────────────
    ax = axes[0]
    ax.set_title("Preamble Fate", fontsize=11)
    labels  = ["Accepted into RA", "Dropped (no free RA process)"]
    sizes   = [total_accepted, total_dropped]
    colors  = ["#2ecc71", "#e74c3c"]
    explode = [0.05, 0]
    wedges, texts, autotexts = ax.pie(
        sizes, labels=labels, colors=colors, explode=explode,
        autopct=lambda p: f"{p:.1f}%\n({int(p*sum(sizes)/100)})",
        startangle=90, textprops={"fontsize": 9},
    )
    for at in autotexts:
        at.set_fontsize(9)

    # ─ Bar: RA lifecycle outcome ──────────────────────────────────────────────
    ax = axes[1]
    ax.set_title("RA Process Outcomes", fontsize=11)
    stages = ["RA\nInitiated", "Msg3\nScheduled", "Msg3\nRetransmitted", "RA\nFailed"]
    counts = [total_accepted, total_msg3,
              len([tc for tc in msg3 if retxs.get(tc)]), total_failed]
    bar_colors = ["#3498db", "#27ae60", "#f39c12", "#e74c3c"]
    bars = ax.bar(stages, counts, color=bar_colors, edgecolor="white",
                  linewidth=0.6, zorder=3)
    for bar, cnt in zip(bars, counts):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                str(cnt), ha="center", va="bottom", fontsize=10, fontweight="bold")
    ax.set_ylabel("Count", fontsize=10)
    ax.set_ylim(0, max(counts) * 1.2)
    ax.grid(axis="y", linestyle="--", linewidth=0.4, alpha=0.5, zorder=0)

    # ─ Stats text box ─────────────────────────────────────────────────────────
    ax = axes[2]
    ax.set_title("Key Metrics", fontsize=11)
    ax.axis("off")
    rejection = 100 * total_dropped / max(total_detected, 1)
    failure   = 100 * total_failed / max(total_accepted, 1)
    avg_retx  = total_retx / max(total_msg3, 1)
    lines = [
        ("Total preambles detected",      f"{total_detected}"),
        ("Preamble rejection rate",         f"{rejection:.1f}%"),
        ("",                               ""),
        ("RA processes started",            f"{total_accepted}"),
        ("Msg3 scheduled",                  f"{total_msg3}"),
        ("Msg3 retransmission events",      f"{total_retx}"),
        ("Avg retx per UE",                 f"{avg_retx:.1f}"),
        ("",                               ""),
        ("RA failure rate",                 f"{failure:.1f}%"),
        ("Successful RA completions",       "0"),
    ]
    y = 0.92
    for label, val in lines:
        if not label:
            y -= 0.04
            continue
        color = "#c0392b" if val in ("0", f"{failure:.1f}%", f"{rejection:.1f}%") else "#2c3e50"
        ax.text(0.05, y, label + ":", fontsize=10, va="top", transform=ax.transAxes)
        ax.text(0.95, y, val, fontsize=10, va="top", ha="right",
                fontweight="bold", color=color, transform=ax.transAxes)
        y -= 0.09

    plt.tight_layout()
    out = OUT_DIR / "fdm16_fig4_summary.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved → {out}")


def main():
    print(f"Parsing {LOG_FILE} …")
    raproc, no_free, ra_init, msg3, retxs, ra_fail, rapids = parse(LOG_FILE)

    print(f"  RACH occasions detected : {len(raproc)}")
    print(f"  Total preambles         : {sum(raproc.values())}")
    print(f"  Dropped (no free RA)    : {sum(no_free.values())}")
    print(f"  RA inits                : {len(ra_init)}")
    print(f"  Msg3 scheduled          : {len(msg3)}")
    print(f"  Retransmission events   : {sum(len(v) for v in retxs.values())}")
    print(f"  RA failures             : {len(ra_fail)}")
    print(f"  RAPIDs parsed           : {len(rapids)}")

    plot_congestion(raproc, no_free, ra_init)
    plot_gantt(ra_init, msg3, retxs, ra_fail)
    plot_rb_grid(msg3, retxs, ra_fail, rapids, slots_per_part=15, total_slots=30)
    plot_summary(raproc, no_free, ra_init, msg3, retxs, ra_fail)


if __name__ == "__main__":
    main()

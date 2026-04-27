#!/usr/bin/env python3
"""
Parse Msg3 scheduled RB allocations from detect-preambles.log,
export to CSV, and plot resource grid + per-RO RB usage.
"""

import re
import csv
import sys
from pathlib import Path
from collections import defaultdict

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

LOG_FILE = Path(__file__).parent / "./detect-preambles.log"
CSV_FILE = Path(__file__).parent / "msg3_rbs.csv"

PATTERN = re.compile(
    r"\[NR_MAC\]\s+UE\s+([0-9a-f]+):\s+Msg3 scheduled at\s+(\d+)\.(\d+)\s+"
    r"\((\d+)\.(\d+)\s+TDA\s+(\d+)\)\s+start\s+(\d+)\s+RBs\s+(\d+)"
)

ANSI_ESCAPE = re.compile(r"\x1b\[[0-9;]*m")


def parse_log(path: Path) -> list[dict]:
    records = []
    with open(path, "r", errors="replace") as f:
        for line in f:
            line = ANSI_ESCAPE.sub("", line)
            m = PATTERN.search(line)
            if not m:
                continue
            ue_id, sched_frame, sched_slot, tx_frame, tx_slot, tda, start, rbs = m.groups()
            records.append({
                "ue_id":       ue_id,
                "sched_frame": int(sched_frame),
                "sched_slot":  int(sched_slot),
                "tx_frame":    int(tx_frame),
                "tx_slot":     int(tx_slot),
                "tda":         int(tda),
                "rb_start":    int(start),
                "rb_count":    int(rbs),
                "rb_end":      int(start) + int(rbs) - 1,
            })
    return records


def export_csv(records: list[dict], path: Path):
    fields = ["ue_id", "sched_frame", "sched_slot", "tx_frame", "tx_slot",
              "tda", "rb_start", "rb_count", "rb_end"]
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)
    print(f"Saved {len(records)} rows → {path}")


def build_ro_summary(records: list[dict]) -> list[dict]:
    """Group by tx_frame (one RO per frame) and compute total RBs used."""
    grouped = defaultdict(list)
    for r in records:
        grouped[r["tx_frame"]].append(r)

    summary = []
    for frame, ues in sorted(grouped.items()):
        total_rbs = sum(u["rb_count"] for u in ues)
        summary.append({
            "tx_frame":  frame,
            "ue_count":  len(ues),
            "total_rbs": total_rbs,
        })
    return summary


# number of frame.slot occasions (columns in resource grid) per figure
SLOTS_PER_FIGURE = 10


def plot(records: list[dict]):
    # ── colour palette per UE ───────────────────────────────────────────────
    ue_ids   = sorted({r["ue_id"] for r in records})
    cmap     = plt.cm.get_cmap("tab20", len(ue_ids))
    ue_color = {uid: cmap(i) for i, uid in enumerate(ue_ids)}

    max_rb = max(r["rb_end"] for r in records) + 2

    # ── per-RO totals (for bar chart) ───────────────────────────────────────
    ro_total: dict[int, int] = defaultdict(int)
    for r in records:
        ro_total[r["tx_frame"]] += r["rb_count"]
    all_ro_totals = list(ro_total.values())
    global_mean   = np.mean(all_ro_totals)

    # ── unique tx occasions (frame.slot) for resource grid ──────────────────
    occasions = sorted({(r["tx_frame"], r["tx_slot"]) for r in records})
    n_chunks = (len(occasions) + SLOTS_PER_FIGURE - 1) // SLOTS_PER_FIGURE
    for chunk_idx in range(n_chunks):
        chunk_occ   = occasions[chunk_idx * SLOTS_PER_FIGURE:(chunk_idx + 1) * SLOTS_PER_FIGURE]
        chunk_set   = set(chunk_occ)
        local_index = {o: i for i, o in enumerate(chunk_occ)}
        c_labels    = [f"{f}.{s}" for f, s in chunk_occ]

        chunk_records = [r for r in records if (r["tx_frame"], r["tx_slot"]) in chunk_set]

        # ROs that appear in this chunk (unique tx_frames, in order of first appearance)
        seen_frames: list[int] = []
        for f, _ in chunk_occ:
            if f not in seen_frames:
                seen_frames.append(f)
        ro_labels = [f"RO {chunk_idx * (SLOTS_PER_FIGURE // 2) + i + 1}\n({f})"
                     for i, f in enumerate(seen_frames)]

        fig, axes = plt.subplots(
            2, 1,
            figsize=(max(16, len(chunk_occ) * 0.8), 10),
            gridspec_kw={"height_ratios": [2, 1]},
        )
        title_start = c_labels[0]
        title_end   = c_labels[-1]
        fig.suptitle(
            f"Msg3 RB Allocations  [{title_start} – {title_end}]  "
            f"(part {chunk_idx + 1}/{n_chunks})",
            fontsize=14, fontweight="bold",
        )

        # ── TOP: Resource Grid (frame.slot columns) ──────────────────────────
        ax1 = axes[0]
        ax1.set_title("Resource Grid  (Y = RB index,  X = tx frame.slot)")
        ax1.set_xlabel("tx frame.slot")
        ax1.set_ylabel("RB Index")
        ax1.set_xlim(-0.5, len(chunk_occ) - 0.5)
        ax1.set_ylim(-0.5, max_rb)

        for r in chunk_records:
            xi    = local_index[(r["tx_frame"], r["tx_slot"])]
            color = ue_color[r["ue_id"]]
            rect  = mpatches.FancyBboxPatch(
                (xi - 0.4, r["rb_start"]),
                0.8, r["rb_count"],
                boxstyle="round,pad=0.05",
                facecolor=color, edgecolor="white", linewidth=0.5, alpha=0.85,
            )
            ax1.add_patch(rect)
            ax1.text(xi, r["rb_start"] + r["rb_count"] / 2,
                     r["ue_id"], ha="center", va="center",
                     fontsize=9, color="black", fontweight="bold")

        ax1.set_xticks(range(len(chunk_occ)))
        ax1.set_xticklabels(c_labels, rotation=45, ha="right", fontsize=8)
        ax1.grid(axis="y", linestyle="--", linewidth=0.4, alpha=0.5)
        ax1.set_yticks(range(0, max_rb + 1, 4))

        chunk_ue_ids = sorted({r["ue_id"] for r in chunk_records})
        patches = [mpatches.Patch(color=ue_color[uid], label=f"UE {uid}") for uid in chunk_ue_ids]
        ax1.legend(handles=patches, loc="upper right", fontsize=7,
                   ncol=max(1, len(chunk_ue_ids) // 6), framealpha=0.7)

        # ── BOTTOM: Total RBs per RO (one bar per tx_frame) ─────────────────
        ax2 = axes[1]
        ax2.set_title("Total RBs Used per RO  (slot 10 + slot 17 combined)")
        ax2.set_xlabel("RO")
        ax2.set_ylabel("Total RBs")

        ro_xs     = list(range(len(seen_frames)))
        ro_totals = [ro_total[f] for f in seen_frames]

        ax2.bar(ro_xs, ro_totals, color="#3a86ff", width=0.6,
                edgecolor="white", linewidth=0.4)
        ax2.set_xlim(-0.5, len(seen_frames) - 0.5)
        ax2.set_ylim(0, max(all_ro_totals) * 1.3)
        ax2.set_xticks(ro_xs)
        ax2.set_xticklabels(ro_labels, rotation=0, ha="center", fontsize=8)
        ax2.axhline(y=global_mean, color="black", linestyle="--", linewidth=1)
        ax2.grid(axis="y", linestyle="--", linewidth=0.4, alpha=0.5)
        ax2.legend(handles=[
            mpatches.Patch(color="black", label=f"global mean {global_mean:.1f} RBs")
        ], fontsize=8, framealpha=0.7)

        plt.tight_layout()
        out = Path(__file__).parent / f"msg3_rbs_{chunk_idx + 1:03d}.png"
        plt.savefig(out, dpi=150, bbox_inches="tight")
        print(f"Saved plot → {out}")
        plt.close(fig)


def main():
    print(f"Parsing {LOG_FILE} …")
    records = parse_log(LOG_FILE)
    if not records:
        print("No Msg3 records found. Check log path / pattern.", file=sys.stderr)
        sys.exit(1)
    print(f"Found {len(records)} Msg3 allocations")

    export_csv(records, CSV_FILE)

    summary = build_ro_summary(records)
    n_ros     = len(summary)
    n_figures = (n_ros * 2 + SLOTS_PER_FIGURE - 1) // SLOTS_PER_FIGURE
    print(f"Unique ROs: {n_ros}  →  {n_figures} figures  ({SLOTS_PER_FIGURE} slots each)")
    print(f"Total RBs per RO — min:{min(s['total_rbs'] for s in summary)} "
          f"max:{max(s['total_rbs'] for s in summary)} "
          f"mean:{sum(s['total_rbs'] for s in summary)/len(summary):.1f}")

    plot(records)


if __name__ == "__main__":
    main()

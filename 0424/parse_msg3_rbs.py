#!/usr/bin/env python3
"""
Parse Msg3 scheduled RB allocations from detect-preambles.log,
export to CSV, and plot resource grid + per-occasion RB usage.
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


def build_occasion_summary(records: list[dict]) -> list[dict]:
    """Group by (tx_frame, tx_slot, tda) and compute total RBs used."""
    grouped = defaultdict(list)
    for r in records:
        key = (r["tx_frame"], r["tx_slot"], r["tda"])
        grouped[key].append(r)

    summary = []
    for (frame, slot, tda), ues in sorted(grouped.items()):
        total_rbs = sum(u["rb_count"] for u in ues)
        min_start  = min(u["rb_start"] for u in ues)
        max_end    = max(u["rb_end"] for u in ues)
        summary.append({
            "tx_frame":  frame,
            "tx_slot":   slot,
            "tda":       tda,
            "ue_count":  len(ues),
            "total_rbs": total_rbs,
            "rb_min":    min_start,
            "rb_max":    max_end,
            "ues":       ues,
        })
    return summary


SLOTS_PER_FIGURE = 10


def plot(records: list[dict], summary: list[dict]):
    # ── colour palette per UE ───────────────────────────────────────────────
    ue_ids   = sorted({r["ue_id"] for r in records})
    cmap     = plt.cm.get_cmap("tab20", len(ue_ids))
    ue_color = {uid: cmap(i) for i, uid in enumerate(ue_ids)}

    slot_palette = ["#3a86ff", "#ff6b6b", "#06d6a0", "#ffd166", "#ef476f", "#118ab2"]
    unique_slots = sorted({r["tx_slot"] for r in records})
    slot_colors  = {sl: slot_palette[i % len(slot_palette)] for i, sl in enumerate(unique_slots)}
    max_rb      = max(r["rb_end"] for r in records) + 2
    all_totals  = [s["total_rbs"] for s in summary]
    global_mean = np.mean(all_totals)

    # ── unique tx occasions (sorted by time) ────────────────────────────────
    occasions = sorted({(r["tx_frame"], r["tx_slot"]) for r in records})

    # build fast lookup: occasion → summary entry
    summary_map = {(s["tx_frame"], s["tx_slot"]): s for s in summary}

    # ── iterate over 50-occasion chunks ─────────────────────────────────────
    n_chunks = (len(occasions) + SLOTS_PER_FIGURE - 1) // SLOTS_PER_FIGURE
    for chunk_idx in range(n_chunks):
        chunk_occ   = occasions[chunk_idx * SLOTS_PER_FIGURE:(chunk_idx + 1) * SLOTS_PER_FIGURE]
        chunk_set   = set(chunk_occ)
        occ_label   = [f"{f}.{s}" for f, s in chunk_occ]
        local_index = {o: i for i, o in enumerate(chunk_occ)}

        chunk_records = [r for r in records if (r["tx_frame"], r["tx_slot"]) in chunk_set]
        chunk_summary = [summary_map[o] for o in chunk_occ if o in summary_map]

        fig, axes = plt.subplots(
            2, 1,
            figsize=(max(16, len(chunk_occ) * 0.35), 10),
            gridspec_kw={"height_ratios": [2, 1]},
        )
        title_range = f"{occ_label[0]} – {occ_label[-1]}"
        fig.suptitle(
            f"Msg3 RB Allocations  [{title_range}]  "
            f"(part {chunk_idx + 1}/{n_chunks})",
            fontsize=14, fontweight="bold",
        )

        # ── TOP: Resource Grid ───────────────────────────────────────────────
        ax1 = axes[0]
        ax1.set_title("Resource Grid  (Y = RB index,  X = RA occasion frame.slot)")
        ax1.set_xlabel("Msg3 scheduled (frame.slot)")
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
                     fontsize=5.5, color="white", fontweight="bold")

        step = max(1, len(chunk_occ) // 30)
        ax1.set_xticks(range(0, len(chunk_occ), step))
        ax1.set_xticklabels(occ_label[::step], rotation=60, ha="right", fontsize=7)
        ax1.grid(axis="y", linestyle="--", linewidth=0.4, alpha=0.5)
        ax1.set_yticks(range(0, max_rb + 1, 4))

        chunk_ue_ids = sorted({r["ue_id"] for r in chunk_records})
        patches = [mpatches.Patch(color=ue_color[uid], label=f"UE {uid}") for uid in chunk_ue_ids]
        ax1.legend(handles=patches, loc="upper right", fontsize=7,
                   ncol=max(1, len(chunk_ue_ids) // 6), framealpha=0.7)

        # ── BOTTOM: Total RBs bar chart ──────────────────────────────────────
        ax2 = axes[1]
        ax2.set_title("Total RBs Used per RA Occasion")
        ax2.set_xlabel("Msg3 scheduled (frame.slot)")
        ax2.set_ylabel("Total RBs")

        xs         = [local_index[(s["tx_frame"], s["tx_slot"])] for s in chunk_summary]
        totals     = [s["total_rbs"] for s in chunk_summary]
        bar_colors = [slot_colors.get(s["tx_slot"], "gray") for s in chunk_summary]

        ax2.bar(xs, totals, color=bar_colors, width=0.7, edgecolor="white", linewidth=0.4)
        ax2.set_xlim(-0.5, len(chunk_occ) - 0.5)
        ax2.set_ylim(0, max(all_totals) * 1.3)
        ax2.set_xticks(range(0, len(chunk_occ), step))
        ax2.set_xticklabels(occ_label[::step], rotation=60, ha="right", fontsize=7)
        ax2.axhline(y=global_mean, color="black", linestyle="--",
                    linewidth=1, label=f"Global mean = {global_mean:.1f} RBs")
        ax2.grid(axis="y", linestyle="--", linewidth=0.4, alpha=0.5)
        slot_patches = [mpatches.Patch(color=c, label=f"slot {s}") for s, c in slot_colors.items()]
        ax2.legend(handles=slot_patches + [
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

    summary = build_occasion_summary(records)
    n_occasions = len(summary)
    n_figures   = (n_occasions + SLOTS_PER_FIGURE - 1) // SLOTS_PER_FIGURE
    print(f"Unique RA occasions: {n_occasions}  →  {n_figures} figures "
          f"({SLOTS_PER_FIGURE} slots each)")
    print(f"Total RBs per occasion — min:{min(s['total_rbs'] for s in summary)} "
          f"max:{max(s['total_rbs'] for s in summary)} "
          f"mean:{sum(s['total_rbs'] for s in summary)/len(summary):.1f}")

    plot(records, summary)


if __name__ == "__main__":
    main()

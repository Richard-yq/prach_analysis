"""
Combined RACH Power Ramping Plot — two trials side by side (slide-ready).
Output: MTKUE_ramping_combined.png  (1920×840, 300 dpi → paste directly into slides)
"""

import re
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from matplotlib.ticker import MultipleLocator

# ── Raw data ──────────────────────────────────────────────────────────────────

TRIAL_DATA = {
    "PRACH-Configuration-Index: 159": {
        "label": "PRACH-Configuration-Index: 159",
        "prach_cfid": "159",
        "raw": """
1,25,-24,success
2,21,-24,success
3,12,-24,success
4,24,-24,success
5,11,-24,success
6,19,-24,success
7,36,-24,success
8,19,-24,success
9,11,-24,success
10,10,-24,success
11,17,-21,failed at RAR
12,20,-19,failed at RAR
13,55,-17,failed at RAR
14,63,-15,failed at RAR
15,25,-14,failed at RAR
16,33,-13,failed at RAR
17,41,-11,failed at RAR
18,49,-9,failed at RAR
19,57,-7,failed at RAR
20,44,-5,failed at RAR
21,52,-3,failed at RAR
22,60,-1,failed at RAR
23,28,1,failed at RAR
24,36,3,failed at RAR
25,33,5,failed at RAR
26,29,7,failed at RAR
27,37,9,failed at RAR
29,10,11,failed at RAR
30,20,13,failed at RAR
31,25,15,success
32,10,-24,success
33,12,-24,success
34,17,-24,success
35,55,-24,success
36,63,-24,success
""",
    },
    "PRACH-Configuration-Index: 148": {
        "label": "PRACH-Configuration-Index: 148",
        "prach_cfid": "148",
        "raw": """
1,38,-24,success
2,24,-24,success
3,22,-24,success
4,44,-24,success
5,18,-24,success
6,28,-24,success
7,29,-24,success
8,19,-24,success
9,22,-24,success
10,32,-24,success
11,8,-24,failed at RAR
12,27,-24,failed at RAR
13,35,-24,failed at RAR
14,43,-22,failed at RAR
15,51,-20,failed at RAR
16,59,-18,failed at RAR
17,23,-16,failed at RAR
18,31,-14,failed at RAR
19,39,-12,failed at RAR
20,47,-10,failed at RAR
21,55,-8,success
22,11,-24,success
23,19,-24,success
24,27,-24,success
25,35,-24,success
26,43,-24,success
27,51,-24,success
""",
    },
}

# ── Parser ─────────────────────────────────────────────────────────────────────

def parse_data(raw: str):
    entries = []
    for line in raw.strip().splitlines():
        parts = [p.strip() for p in line.split(",")]
        if len(parts) < 4:
            continue
        try:
            attempt  = int(parts[0])
            preamble = int(parts[1])
            power    = float(parts[2])
            status   = parts[3]
        except ValueError:
            continue
        entries.append({"attempt": attempt, "preamble": preamble,
                         "power": power, "status": status})
    entries.sort(key=lambda e: e["attempt"])
    return entries

# ── Colors & style ────────────────────────────────────────────────────────────

plt.rcParams.update({
    "font.family":        "sans-serif",
    "font.sans-serif":    ["Arial", "Helvetica", "Arial Unicode MS", "PingFang TC", "sans-serif"],
    "axes.unicode_minus": False,
    "axes.spines.top":    False,
    "axes.spines.right":  False,
})

C_SUCCESS  = "#2ca02c"   # green
C_FAIL     = "#d62728"   # red
C_ATTACK   = "#ffcccc"   # light-red shading for attack window
C_LINE     = "#888888"
C_GRID     = "#dddddd"
C_PREAMBLE = "#555555"

# ── Build figure ──────────────────────────────────────────────────────────────

fig, axes = plt.subplots(
    1, 2,
    figsize=(16, 7),
    sharey=True,
    gridspec_kw={"wspace": 0.10},
)

fig.patch.set_facecolor("white")

all_y = []

for ax, (trial_name, trial_info) in zip(axes, TRIAL_DATA.items()):
    entries  = parse_data(trial_info["raw"])
    x        = [e["attempt"]  for e in entries]
    y        = [e["power"]    for e in entries]
    labels   = [str(e["preamble"]) for e in entries]
    statuses = [e["status"]   for e in entries]
    colors   = [C_SUCCESS if s == "success" else C_FAIL for s in statuses]
    all_y.extend(y)

    # ── Attack window shading ──────────────────────────────────────────────
    fail_attempts = [e["attempt"] for e in entries if e["status"] == "failed at RAR"]
    if fail_attempts:
        ax.axvspan(min(fail_attempts) - 0.5, max(fail_attempts) + 0.5,
                   color=C_ATTACK, alpha=0.35, zorder=0, label="_nolegend_")
        ax.annotate(
            "Attack Active\n(Failed at RAR)",
            xy=(min(fail_attempts) + (max(fail_attempts) - min(fail_attempts)) / 2, max(y) - 1),
            fontsize=9, color="#b22222", ha="center", va="top", style="italic",
            fontweight="bold",
        )

    # ── Starting power reference line ──────────────────────────────────────
    ax.axhline(-24, color="#aaaaaa", linewidth=0.9, linestyle="--", zorder=1)

    # ── Scatter only ───────────────────────────────────────────────────────
    ax.scatter(x, y, c=colors, s=100, edgecolors="white", linewidths=0.8,
               zorder=3)

    # ── Preamble index labels ──────────────────────────────────────────────
    for xi, yi, lab, status in zip(x, y, labels, statuses):
        ax.annotate(lab, (xi, yi),
                    textcoords="offset points", xytext=(4, 6),
                    fontsize=7, color=C_PREAMBLE)

    # ── Axes labels & title ────────────────────────────────────────────────
    succ_count = statuses.count("success")
    fail_count = statuses.count("failed at RAR")
    max_power  = max(e["power"] for e in entries if e["status"] == "failed at RAR")

    ax.set_title(
        f"{trial_name}",
        fontsize=14, fontweight="bold", pad=10,
    )
    ax.set_xlabel("Attempt Number", fontsize=11, labelpad=6)
    ax.grid(axis="y", color=C_GRID, linewidth=0.8, zorder=0)
    ax.tick_params(labelsize=9)
    ax.xaxis.set_minor_locator(MultipleLocator(1))

    # ── Stats box ─────────────────────────────────────────────────────────
    info = (
        f"Total attempts : {len(entries)}\n"
        f"Success         : {succ_count}\n"
        f"Failed at RAR  : {fail_count}"
    )
    ax.text(
        0.015, 0.97, info,
        transform=ax.transAxes,
        fontsize=8.5, va="top", ha="left", family="monospace",
        bbox=dict(boxstyle="round,pad=0.55", facecolor="white",
                  alpha=0.90, edgecolor="#cccccc"),
    )

# ── Shared y-axis label (only on left subplot) ────────────────────────────────
axes[0].set_ylabel("UE Tx Power (dBm)", fontsize=11, labelpad=6)

# ── Legend — below of left subplot ──────────────────────────────────────
succ_patch   = mpatches.Patch(color=C_SUCCESS, label="RACH Success")
fail_patch   = mpatches.Patch(color=C_FAIL,    label="Failed at RAR")
attack_patch = mpatches.Patch(color=C_ATTACK,  alpha=0.6, label="Attack Window")
ref_line     = mlines.Line2D([], [], color="#aaaaaa", linestyle="--",
                              linewidth=1.2, label="Initial Tx Power (−24 dBm)")
note         = mlines.Line2D([], [], marker="", color="none",
                              label="Numbers = preamble index")

fig.legend(
    handles=[succ_patch, fail_patch, attack_patch, ref_line, note],
    loc="lower center", ncol=5,
    fontsize=9.5, framealpha=0.92,
    bbox_to_anchor=(0.5, -0.01),
    edgecolor="#cccccc",
)

# ── Super-title ───────────────────────────────────────────────────────────────
fig.suptitle(
    "COTS UE RACH Power Ramping Under Preamble Collision Attack",
    fontsize=16, fontweight="bold", y=1.01,
)
fig.text(
    0.5, 0.965,
    "PRACH Configuration Index: 148  ·  Band B4  ·  Ramping Step: 2 dBm",
    ha="center", fontsize=10.5, color="#444444",
)

# ── Save ──────────────────────────────────────────────────────────────────────
fig.tight_layout(rect=[0, 0.08, 1, 0.97])
out_dir  = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "MTKUE_ramping_combined.png")
fig.savefig(out_path, dpi=300, bbox_inches="tight", facecolor="white")
print(f"Saved → {out_path}")
plt.show()

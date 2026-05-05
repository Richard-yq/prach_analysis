import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({
    "font.family":      "DejaVu Sans",
    "axes.spines.top":  False,
    "axes.spines.right":False,
    "axes.linewidth":   0.8,
})

# ── Data from gNB log: Frame 997, slot 19 ─────────────────────────────────
fdm0_energy = [
    48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,
    48.0,48.0,48.0,48.0,48.0,47.8,48.0,48.0,48.0,51.0,48.0,48.0,48.0,51.0,48.0,48.0,
    48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,
    54.9,52.7,54.0,55.7,48.0,51.0,48.0,48.0,51.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,
]
fdm1_energy = [
    44.8,44.7,44.9,44.7,44.3,43.7,44.4,43.7,44.8,45.1,44.7,44.8,44.4,44.8,44.8,45.0,
    42.9,43.6,44.2,43.3,43.5,43.5,43.9,43.1,43.1,45.9,43.2,43.4,43.8,45.2,44.4,44.7,
    43.0,43.1,43.8,42.8,43.2,43.5,43.4,44.2,42.1,43.2,42.9,42.5,44.0,44.6,45.0,45.0,
    52.7,51.0,52.7,51.0,45.2,46.0,44.4,45.0,45.3,43.4,42.4,43.5,44.8,43.1,44.5,42.6,
]
fdm1_idx = list(range(64))
preamble_idx = list(range(64))

# ── Colour palette (print-friendly) ───────────────────────────────────────
BLUE   = "#1f77b4"
ORANGE = "#d6620f"
RED    = "#c0392b"
GREEN  = "#2e7d32"
LGRAY  = "#e8e8e8"   # light fill for inactive cells
MGRAY  = "#888888"   # mid-grey for borders / annotations
BLACK  = "#111111"
ATKHATCH = "#e74c3c"  # attack cell border

# ── Figure ─────────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(14, 9), facecolor="white")
gs  = fig.add_gridspec(2, 1, height_ratios=[1, 1.5], hspace=0.52,
                       left=0.07, right=0.97, top=0.92, bottom=0.08)
ax_top = fig.add_subplot(gs[0])
ax_bot = fig.add_subplot(gs[1])

# ══════════════════════════════════════════════════════════════════════════
# Panel A – PRACH Resource Grid
# ══════════════════════════════════════════════════════════════════════════
ax_top.set_facecolor("white")
ax_top.set_xlim(-0.6, 8.2)
ax_top.set_ylim(-0.6, 2.7)
ax_top.axis("off")
ax_top.set_title("(a)  PRACH Resource Grid — Frame 997, Slot 19",
                 fontsize=12, fontweight="bold", color=BLACK, pad=6, loc="left", x=0.0)

SLOT_LABELS = ["slot 15", "slot 16", "slot 17", "slot 18",
               "slot 19\n(PRACH)", "slot 20", "slot 21", "slot 22"]

for col, slabel in enumerate(SLOT_LABELS):
    is_atk = (col == 4)
    if not is_atk:
        # only draw slot label, no cell box
        ax_top.text(col + 0.50, -0.30, slabel,
                    ha="center", va="center", fontsize=7, color=MGRAY)
        continue

    for row in range(2):
        rect = mpatches.FancyBboxPatch(
            (col + 0.05, row + 0.05), 0.90, 0.90,
            boxstyle="round,pad=0.03",
            linewidth=2.2, edgecolor=ATKHATCH, facecolor="#fde8e8", zorder=2,
        )
        ax_top.add_patch(rect)

        txt = f"FDM {row}\n64 preambles\ndetected"
        ax_top.text(col + 0.50, row + 0.50, txt,
                    ha="center", va="center", fontsize=7.5,
                    color=RED, fontweight="bold", zorder=3)

    # slot label below (attack slot)
    ax_top.text(col + 0.50, -0.30, slabel,
                ha="center", va="center", fontsize=7,
                color=BLACK, fontweight="bold")

# Y-axis row labels
ax_top.text(-0.08, 0.50, "FDM 0\n(freq idx 0)", ha="right", va="center",
            fontsize=8, color=BLUE, fontstyle="italic")
ax_top.text(-0.08, 1.50, "FDM 1\n(freq idx 1)", ha="right", va="center",
            fontsize=8, color=ORANGE, fontstyle="italic")

# Frequency axis arrow (left)
ax_top.annotate("", xy=(-0.50, 2.10), xytext=(-0.50, -0.05),
    arrowprops=dict(arrowstyle="-|>", color=MGRAY, lw=1.0))
ax_top.text(-0.53, 1.00, "Frequency", ha="right", va="center",
            fontsize=7, color=MGRAY, rotation=90)

# Attacker box + arrow
ax_top.add_patch(mpatches.FancyBboxPatch(
    (2.40, 0.78), 0.90, 0.44,
    boxstyle="round,pad=0.05", linewidth=1.5,
    edgecolor=RED, facecolor="#fff0f0", zorder=4))
ax_top.text(2.85, 1.00, "Attacker\n(UE)", ha="center", va="center",
            fontsize=8, color=RED, fontweight="bold", zorder=5)
ax_top.annotate("",
    xy=(4.05, 0.55), xytext=(3.30, 0.88),
    arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.8,
                    connectionstyle="arc3,rad=-0.25"), zorder=5)
ax_top.annotate("",
    xy=(4.05, 1.45), xytext=(3.30, 1.12),
    arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.8,
                    connectionstyle="arc3,rad=0.25"), zorder=5)
ax_top.text(3.55, 0.62, "preamble 0–63", ha="center", va="top",
            fontsize=6.5, color=RED)
ax_top.text(3.55, 1.38, "preamble 0–63", ha="center", va="bottom",
            fontsize=6.5, color=RED)

# gNB box + arrows
ax_top.add_patch(mpatches.FancyBboxPatch(
    (7.52, 0.65), 0.60, 0.70,
    boxstyle="round,pad=0.05", linewidth=1.5,
    edgecolor=GREEN, facecolor="#f0fff4", zorder=4))
ax_top.text(7.82, 1.00, "gNB", ha="center", va="center",
            fontsize=10, color=GREEN, fontweight="bold", zorder=5)
for row in range(2):
    ax_top.annotate("",
        xy=(7.52, row + 0.50), xytext=(4.95, row + 0.50),
        arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.5,
                        connectionstyle="arc3,rad=0.0"), zorder=5)

# "all detected" label
ax_top.text(6.24, 2.42, "All preambles detected", ha="center", va="center",
            fontsize=7.5, color=GREEN, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f0fff4",
                      edgecolor=GREEN, linewidth=1.2))

# ══════════════════════════════════════════════════════════════════════════
# Panel B – Preamble Detection Energy
# ══════════════════════════════════════════════════════════════════════════
ax_bot.set_facecolor("white")
bar_w = 0.42
x0    = np.array(preamble_idx)

ax_bot.bar(x0 - bar_w/2, fdm0_energy, width=bar_w,
           color=BLUE,   alpha=0.80, label="FDM 0  (64 preambles detected, freq idx 0)", zorder=3)
ax_bot.bar([i + bar_w/2 for i in fdm1_idx], fdm1_energy, width=bar_w,
           color=ORANGE, alpha=0.80, label="FDM 1  (64 preambles detected, freq idx 1)", zorder=3)

ax_bot.set_xlim(-1, 64)
ax_bot.set_ylim(38, 62)
ax_bot.set_xlabel("Preamble Index", fontsize=11, color=BLACK)
ax_bot.set_ylabel("Detected Energy (dB)", fontsize=11, color=BLACK)
ax_bot.set_title(
    "(b)  Detected Preamble Energy — Frame 997, Slot 19  (Same PRACH Slot, 2 FDM Occasions)",
    fontsize=12, fontweight="bold", color=BLACK, pad=6, loc="left", x=0.0)

ax_bot.tick_params(labelsize=9, colors=BLACK)
ax_bot.set_xticks(range(0, 64, 4))
ax_bot.grid(axis="y", color=LGRAY, linewidth=0.7, zorder=1)
for sp in ["left", "bottom"]:
    ax_bot.spines[sp].set_color(MGRAY)

# Annotate peak preambles (FDM 0)
for idx, val in [(48, 54.9), (49, 52.7), (50, 54.0), (51, 55.7)]:
    ax_bot.text(idx - bar_w/2, val + 0.25, f"{val}", ha="center", va="bottom",
                fontsize=6.5, color=BLUE, fontweight="bold")
# Annotate peak preambles (FDM 1)
for idx, val in [(48, 52.7), (50, 52.7)]:
    ax_bot.text(idx + bar_w/2, val + 0.25, f"{val}", ha="center", va="bottom",
                fontsize=6.5, color=ORANGE, fontweight="bold")

# Bracket: 1 slot × 2 FDM
ax_bot.annotate("", xy=(63.2, 60.2), xytext=(-0.2, 60.2),
    arrowprops=dict(arrowstyle="<->", color=BLACK, lw=1.0))
ax_bot.text(31.5, 61.0,
            "1 PRACH Slot  ×  2 FDM Occasions  →  128 preambles flooded, all detected by gNB",
            ha="center", va="center", fontsize=8.5, color=BLACK,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#fff8e1",
                      edgecolor="#aaa", linewidth=1.0))

legend = ax_bot.legend(loc="lower right", fontsize=9, framealpha=0.9,
                       edgecolor=MGRAY)

fig.suptitle("PRACH Flooding Attack: Multiple Preambles per RO × Multiple FDM Occasions",
             fontsize=13, fontweight="bold", color=BLACK, y=0.97)

out_path = "/Users/yq/Documents/analysis/0505/prach_attack.png"
plt.savefig(out_path, dpi=180, bbox_inches="tight", facecolor="white")
print(f"Saved: {out_path}")

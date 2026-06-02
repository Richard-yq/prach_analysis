import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "font.family":      "DejaVu Sans",
    "axes.spines.top":  False,
    "axes.spines.right":False,
    "axes.linewidth":   0.8,
})

# ── Data from gNB log (oai-fdm16.log): Frame 285, slot 19 ─────────────────
fdm0_energy = [
    51.0,51.0,51.0,51.0,51.0,51.0,52.7,48.0,48.0,51.0,51.0,51.0,51.0,51.0,51.0,51.0,
    51.0,52.7,48.0,51.0,51.0,51.0,51.0,52.7,48.0,51.0,51.0,51.0,48.0,51.0,51.0,48.0,
    52.7,52.7,51.0,52.7,51.0,51.0,51.0,48.0,51.0,51.0,48.0,51.0,51.0,51.0,51.0,51.0,
    51.0,51.0,52.7,48.0,51.0,51.0,48.0,48.0,48.0,51.0,51.0,48.0,52.7,51.0,51.0,51.0,
]
fdm1_energy = [
    44.8,45.1,44.9,45.5,44.9,45.3,45.5,44.3,43.8,45.8,45.3,44.7,45.2,46.3,45.3,45.2,
    46.0,46.6,45.2,45.5,44.0,44.7,44.6,45.9,44.0,44.5,44.5,43.9,44.5,46.0,45.1,45.9,
    45.1,45.0,44.2,45.5,46.1,45.2,45.9,45.5,45.8,45.6,44.8,45.5,44.2,45.1,45.6,44.8,
    44.1,45.2,46.0,43.5,45.0,44.6,44.6,44.3,44.9,45.9,44.5,44.7,45.6,45.7,44.2,45.2,
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
# 22 cm wide → 8.66 in; height ~5.2 in for slide
fig, ax_bot = plt.subplots(figsize=(9.38, 2.95), facecolor="white")
fig.subplots_adjust(left=0.08, right=0.995, top=0.93, bottom=0.15)

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

ax_bot.tick_params(labelsize=9, colors=BLACK)
ax_bot.set_xticks(range(0, 64, 4))
ax_bot.grid(axis="y", color=LGRAY, linewidth=0.7, zorder=1)
for sp in ["left", "bottom"]:
    ax_bot.spines[sp].set_color(MGRAY)

# Annotate peak preambles (FDM 0: 52.7 dB peaks)
for idx in [6, 17, 23, 32, 33, 35, 50, 60]:
    ax_bot.text(idx - bar_w/2, 52.7 + 0.25, "52.7", ha="center", va="bottom",
                fontsize=6, color=BLUE, fontweight="bold")
# Annotate peak preambles (FDM 1)
for idx, val in [(13, 46.3), (17, 46.6), (29, 46.0), (36, 46.1)]:
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

legend = ax_bot.legend(fontsize=9, framealpha=0.9, edgecolor=MGRAY,
                       loc="upper right",
                       bbox_to_anchor=(0.99, 0.90), bbox_transform=ax_bot.transAxes)


out_path = "/Users/yq/Documents/analysis/0602/prach_attack.png"
plt.savefig(out_path, dpi=180, bbox_inches="tight", facecolor="white")
print(f"Saved: {out_path}")

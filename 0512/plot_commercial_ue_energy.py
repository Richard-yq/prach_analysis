import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import re
import csv

plt.rcParams.update({
    "font.family":      "DejaVu Sans",
    "axes.spines.top":  False,
    "axes.spines.right":False,
    "axes.linewidth":   0.8,
})

log_file = "/Users/yq/Documents/analysis/0512/oai-fdm-mtk.log"

energies = []
x_labels = []

pattern = re.compile(r"Frame (\d+), slot (\d+).*?energy ([\d\.]+) dB")

with open(log_file, "r") as f:
    for line in f:
        if " Initiating RA procedure with " in line:
            match = pattern.search(line)
            if match:
                frame = int(match.group(1))
                slot = int(match.group(2))
                energy = float(match.group(3))
                label = f"{frame}.{slot}"
                x_labels.append(label)
                energies.append(energy)

csv_out_path = "/Users/yq/Documents/analysis/0512/0512-MTKUE-power.csv"
with open(csv_out_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Frame.Slot", "Detected Energy (dB)"])
    for label, energy in zip(x_labels, energies):
        writer.writerow([label, energy])
print(f"Saved CSV: {csv_out_path}")

# ── Colour palette ───────────────────────────────────────
BLUE   = "#1f77b4"
BLACK  = "#111111"
LGRAY  = "#e8e8e8"
MGRAY  = "#888888"

# ── Figure ─────────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(12, 5), facecolor="white")
ax = fig.add_subplot(111)

bar_w = 0.5
x_pos = np.arange(len(x_labels))

ax.bar(x_pos, energies, width=bar_w, color=BLUE, alpha=0.80, label="Commercial UE", zorder=3)

# Find max and min to set reasonable y_limit
if energies:
    y_min = max(0, min(energies) - 2)
    y_max = max(energies) + 2
    ax.set_ylim(y_min, y_max)
else:
    ax.set_ylim(38, 62)

ax.set_xlim(-1, len(x_labels))
ax.set_xticks(x_pos)
ax.set_xticklabels(x_labels, rotation=45, ha="right")

ax.set_xlabel("Frame.Slot", fontsize=11, color=BLACK)
ax.set_ylabel("Detected Energy (dB)", fontsize=11, color=BLACK)
ax.set_title(
    "Detected Commercial UE Preamble Energy",
    fontsize=12, fontweight="bold", color=BLACK, pad=10, loc="left", x=0.0)

ax.tick_params(labelsize=9, colors=BLACK)
ax.grid(axis="y", color=LGRAY, linewidth=0.7, zorder=1)
for sp in ["left", "bottom"]:
    ax.spines[sp].set_color(MGRAY)

# Annotate peak/all preambles
for i, val in enumerate(energies):
    ax.text(i, val + 0.2, f"{val:.1f}", ha="center", va="bottom",
            fontsize=8, color=BLUE, fontweight="bold")

legend = ax.legend(loc="lower right", fontsize=9, framealpha=0.9, edgecolor=MGRAY)

out_path = "/Users/yq/Documents/analysis/0512/commercial_ue_energy.png"
plt.savefig(out_path, dpi=180, bbox_inches="tight", facecolor="white")
print(f"Saved: {out_path}")

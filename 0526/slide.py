import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# ── colour palette ──────────────────────────────────────────────────────────
BG       = "#0D1117"   # deep navy
C_STEP1  = "#1A3A5C"   # dark steel blue  (Step 1 panel)
C_STEP2  = "#1A3A2C"   # dark forest green (Step 2 panel)
C_INPUT  = "#1E3A5F"
C_ALERT  = "#C0392B"
C_NORMAL = "#1F618D"
C_ARROW  = "#E0E0E0"
C_ATK    = "#922B21"   # attack path
C_HI     = "#1A5276"   # high-load path
C_GOLD   = "#F4D03F"   # formula highlight
C_WHITE  = "#F0F0F0"
C_GREY   = "#9E9E9E"

def rounded_box(ax, x, y, w, h, color, radius=0.02, alpha=1.0, zorder=2,
                edge_color=None, lw=1.5):
    ec = edge_color if edge_color else color
    box = FancyBboxPatch((x, y), w, h,
                         boxstyle=f"round,pad={radius}",
                         facecolor=color, edgecolor=ec,
                         linewidth=lw, alpha=alpha, zorder=zorder)
    ax.add_patch(box)
    return box

def arrow(ax, x1, y1, x2, y2, color=C_ARROW, lw=2, style="->",
          label=None, label_side="top", zorder=3):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color,
                                lw=lw, connectionstyle="arc3,rad=0.0"),
                zorder=zorder)
    if label:
        mx, my = (x1+x2)/2, (y1+y2)/2
        dy = 0.018 if label_side == "top" else -0.022
        ax.text(mx, my+dy, label, ha="center", va="center",
                fontsize=8, color=color, zorder=zorder+1,
                fontweight="bold")

# ── figure setup ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(16, 9))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# ══════════════════════════════════════════════════════════════════════════════
# TITLE
# ══════════════════════════════════════════════════════════════════════════════
ax.text(0.5, 0.96, "Two-Step Decision Flow for RACH Anomaly Detection",
        ha="center", va="top", fontsize=16, color=C_WHITE,
        fontweight="bold", zorder=5)
ax.text(0.5, 0.925,
        "Step 1: Detect anomaly  →  Step 2: Distinguish attack vs. high load",
        ha="center", va="top", fontsize=10, color=C_GREY, zorder=5)

# ── divider line ─────────────────────────────────────────────────────────────
ax.plot([0.5, 0.5], [0.04, 0.90], color="#444", lw=1.2, ls="--", zorder=1)

# ══════════════════════════════════════════════════════════════════════════════
# LEFT PANEL — Step 1: Anomaly Detection
# ══════════════════════════════════════════════════════════════════════════════
rounded_box(ax, 0.01, 0.04, 0.47, 0.84,
            C_STEP1, radius=0.015, alpha=0.35, lw=0, zorder=1)

ax.text(0.245, 0.875, "STEP 1", ha="center", fontsize=13,
        color="#5DADE2", fontweight="bold", zorder=5)
ax.text(0.245, 0.847, "Anomaly Detection  —  What happened?",
        ha="center", fontsize=9.5, color=C_GREY, zorder=5)

# Input block
rounded_box(ax, 0.04, 0.755, 0.40, 0.068, "#1F3A5F", edge_color="#5DADE2",
            radius=0.012, lw=1.8, zorder=3)
ax.text(0.24, 0.789, "Monitoring Center  |  Input: recent RACH traffic data",
        ha="center", va="center", fontsize=9, color="#AED6F1", zorder=5)

arrow(ax, 0.24, 0.755, 0.24, 0.710, lw=2)

# Core formula box — manual fraction (mathtext \# inside \frac is broken in mpl)
rounded_box(ax, 0.06, 0.645, 0.36, 0.062, "#0B2942", edge_color=C_GOLD,
            radius=0.012, lw=2.2, zorder=3)
ax.text(0.155, 0.683, r"$R_1\ =$", ha="center", va="center",
        fontsize=13, color=C_GOLD, zorder=5)
ax.text(0.265, 0.695, "#Msg3", ha="center", va="center",
        fontsize=11, color=C_GOLD, fontweight="bold", zorder=5)
ax.plot([0.215, 0.315], [0.683, 0.683], color=C_GOLD, lw=1.8, zorder=5)
ax.text(0.265, 0.671, "#Msg5", ha="center", va="center",
        fontsize=11, color=C_GOLD, fontweight="bold", zorder=5)

# Normal vs anomaly scale diagram
# left: normal
rounded_box(ax, 0.035, 0.525, 0.185, 0.105, "#0E2340", edge_color="#1F618D",
            radius=0.010, lw=1.5, zorder=3)
ax.text(0.128, 0.620, "Normal State", ha="center", va="center",
        fontsize=8.5, color="#AED6F1", fontweight="bold", zorder=5)
# balance icon
for bar_x, bar_h, col in [(0.09, 0.022, "#2E86C1"), (0.165, 0.022, "#2E86C1")]:
    rounded_box(ax, bar_x, 0.545, 0.03, bar_h, col, radius=0.004, zorder=4)
ax.plot([0.09, 0.195], [0.567, 0.567], color="#2E86C1", lw=2, zorder=4)
ax.plot([0.1425, 0.1425], [0.548, 0.567], color="#2E86C1", lw=2, zorder=4)
ax.text(0.09+0.015, 0.543, "Msg3", ha="center", va="top",
        fontsize=7, color=C_GREY, zorder=5)
ax.text(0.165+0.015, 0.543, "Msg5", ha="center", va="top",
        fontsize=7, color=C_GREY, zorder=5)
ax.text(0.128, 0.534, r"$R_1 \approx 1$  ✓",
        ha="center", va="center", fontsize=8.5, color="#2ECC71", zorder=5)

# right: anomaly
rounded_box(ax, 0.235, 0.525, 0.185, 0.105, "#2C0E0E", edge_color=C_ALERT,
            radius=0.010, lw=1.5, zorder=3)
ax.text(0.328, 0.620, "Anomaly  ⚠", ha="center", va="center",
        fontsize=8.5, color="#F1948A", fontweight="bold", zorder=5)
# imbalanced bars
rounded_box(ax, 0.255, 0.545, 0.030, 0.040, C_ALERT, radius=0.004, zorder=4)
rounded_box(ax, 0.345, 0.545, 0.030, 0.012, "#888", radius=0.004, zorder=4)
ax.text(0.270, 0.543, "Msg3↑↑", ha="center", va="top",
        fontsize=7, color="#F1948A", zorder=5)
ax.text(0.360, 0.543, "Msg5", ha="center", va="top",
        fontsize=7, color=C_GREY, zorder=5)
ax.text(0.328, 0.534, r"$R_1 \ll 1$  ✗",
        ha="center", va="center", fontsize=8.5, color=C_ALERT, zorder=5)

arrow(ax, 0.24, 0.525, 0.24, 0.480, lw=2)

# EVT adaptive threshold box
rounded_box(ax, 0.04, 0.395, 0.40, 0.078, "#1A1A2E", edge_color="#8E44AD",
            radius=0.012, lw=1.8, zorder=3)
ax.text(0.24, 0.447, "Extreme Value Theory (EVT)",
        ha="center", va="center", fontsize=9, color="#D2B4DE",
        fontweight="bold", zorder=5)
ax.text(0.24, 0.422,
        "Adaptive threshold  τ(t)  computed from tail statistics of R₁",
        ha="center", va="center", fontsize=8, color=C_GREY, zorder=5)

arrow(ax, 0.24, 0.395, 0.24, 0.350, lw=2)

# Decision diamond (anomaly?)
diamond_cx, diamond_cy = 0.24, 0.315
dw, dh = 0.10, 0.055
diamond = plt.Polygon(
    [[diamond_cx, diamond_cy+dh],
     [diamond_cx+dw, diamond_cy],
     [diamond_cx, diamond_cy-dh],
     [diamond_cx-dw, diamond_cy]],
    closed=True, facecolor="#1C1C1C", edgecolor="#F4D03F", lw=2, zorder=3)
ax.add_patch(diamond)
ax.text(diamond_cx, diamond_cy+0.008, "R₁ < τ(t)?",
        ha="center", va="center", fontsize=9, color=C_GOLD,
        fontweight="bold", zorder=5)

# No path (stays normal)
arrow(ax, diamond_cx-dw, diamond_cy,
      0.058, diamond_cy, color="#2ECC71", lw=1.8, label="No", label_side="top")
ax.text(0.045, diamond_cy-0.025, "Normal\nOperation",
        ha="center", va="top", fontsize=8, color="#2ECC71", zorder=5)

# Yes path → Step 2
arrow(ax, diamond_cx, diamond_cy-dh,
      diamond_cx, 0.12, color=C_ALERT, lw=2.2, label="Yes  (Anomaly!)")

# "Go to Step 2" connector box at bottom-left
rounded_box(ax, 0.09, 0.065, 0.30, 0.048, "#3B0000", edge_color=C_ALERT,
            radius=0.010, lw=2, zorder=3)
ax.text(0.24, 0.089, "⚠  Anomaly Detected  →  Proceed to Step 2",
        ha="center", va="center", fontsize=8.5, color="#F1948A",
        fontweight="bold", zorder=5)

# Big arrow across the divider
ax.annotate("", xy=(0.52, 0.089), xytext=(0.39, 0.089),
            arrowprops=dict(arrowstyle="->, head_width=0.4, head_length=0.3",
                            color=C_ALERT, lw=2.5), zorder=4)

# ══════════════════════════════════════════════════════════════════════════════
# RIGHT PANEL — Step 2: Differentiation
# ══════════════════════════════════════════════════════════════════════════════
rounded_box(ax, 0.515, 0.04, 0.47, 0.84,
            C_STEP2, radius=0.015, alpha=0.35, lw=0, zorder=1)

ax.text(0.755, 0.875, "STEP 2", ha="center", fontsize=13,
        color="#58D68D", fontweight="bold", zorder=5)
ax.text(0.755, 0.847, "Differentiation  —  Who caused it?",
        ha="center", fontsize=9.5, color=C_GREY, zorder=5)

# Formula box — manual fraction
rounded_box(ax, 0.535, 0.755, 0.44, 0.068, "#0B2E1A", edge_color=C_GOLD,
            radius=0.012, lw=2.2, zorder=3)
ax.text(0.618, 0.789, r"$R_2\ =$", ha="center", va="center",
        fontsize=13, color=C_GOLD, zorder=5)
ax.text(0.800, 0.803, r"$N_{BUE}$  (active connections)",
        ha="center", va="center", fontsize=10, color=C_GOLD,
        fontweight="bold", zorder=5)
ax.plot([0.675, 0.955], [0.789, 0.789], color=C_GOLD, lw=1.8, zorder=5)
ax.text(0.800, 0.774, r"$N_{max}$  (gNB capacity)",
        ha="center", va="center", fontsize=10, color=C_GOLD,
        fontweight="bold", zorder=5)

arrow(ax, 0.755, 0.755, 0.755, 0.700, lw=2)

# Decision diamond R2
d2_cx, d2_cy = 0.755, 0.660
diamond2 = plt.Polygon(
    [[d2_cx, d2_cy+dh],
     [d2_cx+dw, d2_cy],
     [d2_cx, d2_cy-dh],
     [d2_cx-dw, d2_cy]],
    closed=True, facecolor="#1C1C1C", edgecolor=C_GOLD, lw=2, zorder=3)
ax.add_patch(diamond2)
ax.text(d2_cx, d2_cy+0.008, "R₂ ≈ 1?",
        ha="center", va="center", fontsize=9, color=C_GOLD,
        fontweight="bold", zorder=5)

# ── Path A: Attack (R2 << 1) ──────────────────────────────────────────────
# Arrow goes LEFT-DOWN from diamond
ax.annotate("", xy=(0.605, 0.490),
            xytext=(d2_cx-dw, d2_cy),
            arrowprops=dict(arrowstyle="->", color="#E74C3C", lw=2.2,
                            connectionstyle="arc3,rad=-0.25"), zorder=3)
ax.text(0.645, 0.600, "No  (R₂ ≪ 1)", ha="center", fontsize=8,
        color="#E74C3C", fontweight="bold", zorder=5)

rounded_box(ax, 0.530, 0.395, 0.215, 0.155, "#2C0808", edge_color="#E74C3C",
            radius=0.012, lw=2, zorder=3)

# hacker icon (simple text art)
ax.text(0.638, 0.530, "◈", ha="center", va="center", fontsize=26, color="#E74C3C", zorder=5)
ax.text(0.638, 0.503, "ATTACK", ha="center", va="center",
        fontsize=11, color="#E74C3C", fontweight="bold", zorder=5)
ax.text(0.638, 0.482,
        "Resources occupied,\nno real connections",
        ha="center", va="center", fontsize=7.5, color="#F1948A", zorder=5)
ax.text(0.638, 0.452, "R₂ ≪ 1  →  gNB not full",
        ha="center", va="center", fontsize=8, color="#E74C3C",
        fontweight="bold", zorder=5)
ax.text(0.638, 0.415, "Response: rate-limit / block",
        ha="center", va="center", fontsize=7.5, color=C_GREY,
        fontstyle="italic", zorder=5)

# ── Path B: High Load (R2 ≈ 1) ───────────────────────────────────────────
# Arrow goes RIGHT-DOWN from diamond
ax.annotate("", xy=(0.897, 0.490),
            xytext=(d2_cx+dw, d2_cy),
            arrowprops=dict(arrowstyle="->", color="#2ECC71", lw=2.2,
                            connectionstyle="arc3,rad=0.25"), zorder=3)
ax.text(0.870, 0.600, "Yes  (R₂ ≈ 1)", ha="center", fontsize=8,
        color="#2ECC71", fontweight="bold", zorder=5)

rounded_box(ax, 0.758, 0.395, 0.215, 0.155, "#082C1A", edge_color="#2ECC71",
            radius=0.012, lw=2, zorder=3)

ax.text(0.865, 0.530, "◉", ha="center", va="center", fontsize=26, color="#2ECC71", zorder=5)
ax.text(0.865, 0.503, "HIGH LOAD", ha="center", va="center",
        fontsize=11, color="#2ECC71", fontweight="bold", zorder=5)
ax.text(0.865, 0.482,
        "Legitimate users surge\n(concert, New Year's...)",
        ha="center", va="center", fontsize=7.5, color="#A9DFBF", zorder=5)
ax.text(0.865, 0.452, "R₂ ≈ 1  →  gNB near capacity",
        ha="center", va="center", fontsize=8, color="#2ECC71",
        fontweight="bold", zorder=5)
ax.text(0.865, 0.415, "Response: load-balance / scale",
        ha="center", va="center", fontsize=7.5, color=C_GREY,
        fontstyle="italic", zorder=5)

# ── Insight box (bottom right) ────────────────────────────────────────────
rounded_box(ax, 0.530, 0.065, 0.44, 0.32, "#0A1A10", edge_color="#58D68D",
            radius=0.012, lw=1.5, zorder=3)
ax.text(0.750, 0.368, "Key Insight",
        ha="center", va="center", fontsize=10, color="#58D68D",
        fontweight="bold", zorder=5)

insights = [
    ("Why two ratios?",
     "R₁ detects the symptom; R₂ finds the cause.",
     "#F4D03F"),
    ("Why EVT for threshold?",
     "Tail statistics self-adapt to traffic patterns — no\nmanual tuning needed.",
     "#D2B4DE"),
    ("Why R₂ = N_BUE / N_max?",
     "If genuine users fill the gNB, R₂ → 1 regardless of\nMsg3 flood; attackers leave R₂ ≪ 1.",
     "#AED6F1"),
]
y_ins = 0.338
for title, body, col in insights:
    ax.text(0.548, y_ins, f"▸ {title}",
            ha="left", va="center", fontsize=8, color=col,
            fontweight="bold", zorder=5)
    y_ins -= 0.022
    for line in body.split("\n"):
        ax.text(0.558, y_ins, line,
                ha="left", va="center", fontsize=7.5, color=C_GREY, zorder=5)
        y_ins -= 0.020
    y_ins -= 0.008

# ── entry arrow from left panel cross-divider ─────────────────────────────
rounded_box(ax, 0.525, 0.065, 0.005, 0.048, "#3B0000", edge_color=C_ALERT,
            radius=0.002, lw=0, zorder=2)
arrow(ax, 0.53, 0.089, 0.535, 0.089, color=C_ALERT, lw=0)

# ══════════════════════════════════════════════════════════════════════════════
# Save
# ══════════════════════════════════════════════════════════════════════════════
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
out_path = "/Users/yq/Documents/analysis/0526/two_step_decision_flow.png"
plt.savefig(out_path, dpi=180, bbox_inches="tight",
            facecolor=BG, edgecolor="none")
print(f"Saved → {out_path}")
plt.show()

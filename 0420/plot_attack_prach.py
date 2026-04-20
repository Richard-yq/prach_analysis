"""
Multi-Preamble Attack Detection Visualization
===============================================
Attack concept: attacker superimposes M distinct ZC preambles into ONE signal.

  s_attack[k] = x_{u, CS0}[k] + x_{u, CS1}[k] + x_{u, CS2}[k]
  (amplitude scaling ignored for clarity)

When the gNB runs its correlator, it sees M independent peaks —
one per preamble — and allocates M RA responses.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────────────────────────────────────
# Parameters
# ─────────────────────────────────────────────────────────────────────────────
N_ZC    = 139
NUM_CS  = 34
CS_STEP = N_ZC // NUM_CS   # = 4 samples

ROOT_U  = 138
M       = 3
CS_IDX  = [5, 14, 28]          # 3 preambles: well-separated, all < NUM_CS=34
THR_DB  = -13.0
NOISE_STD = 0.015

COLORS = ["#C62828", "#1565C0", "#2E7D32"]   # red, blue, green (one per preamble)
C_ATK  = "#7B1FA2"    # purple – attack (combined) signal
C_THR  = "#E65100"
C_NOISE= "#E0E0E0"
C_TEXT = "#212121"
C_MUTED= "#757575"
C_PANEL= "#FAFAFA"
C_GRID = "#E0E0E0"

np.random.seed(42)

# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────
def zadoff_chu(u, N):
    n = np.arange(N, dtype=float)
    return np.exp(-1j * np.pi * u * n * (n + 1) / N)

def make_preamble(u, N, cs_idx, cs_step):
    return np.roll(zadoff_chu(u, N), cs_idx * cs_step)

def correlate(rx, u, N):
    Xu = zadoff_chu(u, N)
    R  = np.fft.ifft(np.fft.fft(rx, N) * np.conj(np.fft.fft(Xu, N)), N)
    return np.abs(R) ** 2

# ─────────────────────────────────────────────────────────────────────────────
# Build signals
# ─────────────────────────────────────────────────────────────────────────────
preambles = [make_preamble(ROOT_U, N_ZC, cs, CS_STEP) for cs in CS_IDX]
s_attack  = sum(preambles)
noise     = (np.random.randn(N_ZC) + 1j * np.random.randn(N_ZC)) * NOISE_STD
rx        = s_attack + noise

corr_full = correlate(rx, ROOT_U, N_ZC)
ref_single = correlate(preambles[0], ROOT_U, N_ZC).max()

def to_db(x):
    return 10 * np.log10(np.maximum(x / ref_single, 1e-12))

corr_db     = to_db(corr_full)
cs_arr      = np.arange(NUM_CS)
cs_power    = np.array([corr_full[(i * CS_STEP) % N_ZC] for i in range(NUM_CS)])
cs_power_db = to_db(cs_power)
peak_samples = [cs * CS_STEP for cs in CS_IDX]
x_full = np.arange(N_ZC)

# ─────────────────────────────────────────────────────────────────────────────
# Figure layout
# ─────────────────────────────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family"    : "DejaVu Sans",
    "font.size"      : 10,
    "axes.titlesize" : 11,
    "axes.labelsize" : 10,
    "legend.fontsize": 9,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
})

fig = plt.figure(figsize=(14, 11), facecolor="white")
fig.suptitle(
    f"5G NR PRACH — Multi-Preamble Attack Signal Detection\n"
    f"(ZC root $u={ROOT_U}$,  $M={M}$ preambles superimposed,"
    f"  CS indices: {CS_IDX})",
    fontsize=13, fontweight="bold", color=C_TEXT, y=0.98
)

gs = gridspec.GridSpec(
    3, 2, figure=fig,
    left=0.08, right=0.97,
    top=0.91, bottom=0.07,
    hspace=0.65, wspace=0.38
)

def style(ax, title, xlabel, ylabel):
    ax.set_facecolor(C_PANEL)
    ax.set_title(title, color=C_TEXT, pad=7, fontweight="bold", fontsize=11)
    ax.set_xlabel(xlabel, color=C_TEXT)
    ax.set_ylabel(ylabel, color=C_TEXT)
    ax.tick_params(colors=C_TEXT)
    ax.grid(True, color=C_GRID, linewidth=0.6, zorder=0)
    for sp in ax.spines.values():
        sp.set_edgecolor("#BDBDBD")

# ─────────────────────────────────────────────────────────────────────────────
# Panel ① – Individual preamble components (time-domain, real part)
# ─────────────────────────────────────────────────────────────────────────────
axA = fig.add_subplot(gs[0, 0])
style(axA,
      f"① Individual Preamble Components (×{M})",
      "Sample index $k$", "Amplitude")

for m in range(M):
    axA.plot(x_full, preambles[m].real,
             color=COLORS[m], linewidth=0.9, alpha=0.85,
             label=f"Preamble {m+1}  (CS idx = {CS_IDX[m]})")

axA.set_xlim(0, N_ZC - 1)
axA.legend(loc="lower right", framealpha=0.92, edgecolor=C_GRID, fontsize=8.5)
axA.text(0.02, 0.03,
         f"Each component: unit-amplitude ZC, different cyclic shift",
         transform=axA.transAxes, color=C_MUTED, fontsize=8)

# ─────────────────────────────────────────────────────────────────────────────
# Panel ② – Attack signal (superposition, real part)
# ─────────────────────────────────────────────────────────────────────────────
axB = fig.add_subplot(gs[0, 1])
style(axB,
      "② Attack Signal  =  Sum of All Components",
      "Sample index $k$", "Amplitude")

axB.plot(x_full, s_attack.real, color=C_ATK, linewidth=0.75, alpha=0.85,
         label=rf"$s_{{\mathrm{{atk}}}}[k] = \sum_{{m=1}}^{{{M}}} x_{{u,\,\mathrm{{CS}}_m}}[k]$")
axB.axhline(0, color=C_MUTED, linewidth=0.5, linestyle=":")
axB.set_xlim(0, N_ZC - 1)
axB.legend(loc="upper right", framealpha=0.92, edgecolor=C_GRID, fontsize=8.5)
axB.text(0.02, 0.03,
         "Looks like noise — indistinguishable from normal PRACH at signal level",
         transform=axB.transAxes, color=C_MUTED, fontsize=8)

# ─────────────────────────────────────────────────────────────────────────────
# Panel ③ – Full DFT correlation output (all M peaks visible)
# ─────────────────────────────────────────────────────────────────────────────
axC = fig.add_subplot(gs[1, :])
style(axC,
      r"③ gNB DFT Correlation Output  $|R_u[n]|^2$  —  M Peaks Revealed",
      "Sample index $n$  (proportional to propagation delay)",
      "Power  [dB  re. single preamble peak]")

axC.fill_between(x_full, -32, THR_DB, color=C_NOISE, alpha=0.5,
                 label="Noise floor (below threshold)", zorder=1)
axC.plot(x_full, corr_db, color=C_ATK, linewidth=1.0, alpha=0.88,
         label=r"$|R_u[n]|^2$  (attack signal)", zorder=2)
axC.axhline(THR_DB, color=C_THR, linewidth=1.5, linestyle="--",
            label=f"Detection threshold  ({THR_DB:.0f} dB)", zorder=3)

# Fixed annotation positions (hand-tuned)
annot_cfg = [
    dict(txt_x=3,   txt_y=3.5, ha="left"),   # Peak 1: beside its own peak
    dict(txt_x=30,  txt_y=6.5, ha="left"),   # Peak 2: right side, high
    dict(txt_x=75,  txt_y=4.5, ha="left"),   # Peak 3: between peak2 and peak3
]
for m in range(M):
    n_peak = peak_samples[m]
    db_val = corr_db[n_peak]
    cfg    = annot_cfg[m]
    axC.scatter([n_peak], [db_val], color=COLORS[m], s=90,
                zorder=5, edgecolors="#333", linewidths=0.8)
    axC.axvline(n_peak, color=COLORS[m], linewidth=0.8,
                linestyle=":", alpha=0.6, zorder=2)
    axC.annotate(
        f"Peak {m+1}  (CS {CS_IDX[m]})\n$n = {n_peak}$",
        xy=(n_peak, db_val),
        xytext=(cfg["txt_x"], cfg["txt_y"]),
        color=COLORS[m], fontsize=8.5, fontweight="bold", ha=cfg["ha"],
        arrowprops=dict(arrowstyle="->", color=COLORS[m], lw=0.85),
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=COLORS[m], alpha=0.95)
    )

axC.text(N_ZC * 0.6, THR_DB - 7,
         "Noise floor  (side-lobes, interference)",
         color=C_MUTED, fontsize=8.5, ha="center")
axC.set_xlim(0, N_ZC - 1)
axC.set_ylim(-32, 9)
axC.legend(loc="lower right", framealpha=0.95, edgecolor=C_GRID, ncol=3)

# ─────────────────────────────────────────────────────────────────────────────
# Panel ④ – Per-CS-slot bar chart: detected vs undetected
#   Gray stubs at noise floor for all 34 slots
#   Colored bars at actual power for the 3 detected ones
#   Labels placed directly above each detected bar
# ─────────────────────────────────────────────────────────────────────────────
axD = fig.add_subplot(gs[2, :])
style(axD,
      f"④ gNB Decision: Correlation Power per CS Slot  —  {M} Detections",
      "Cyclic-shift slot  $v$",
      "Power  [dB  re. single preamble peak]")

FLOOR = -28   # visual noise floor for undetected bars

# Gray stubs for all undetected slots
for v in cs_arr:
    if v not in CS_IDX:
        axD.bar(v, FLOOR - (-32), width=0.65, bottom=-32,
                color="#EEEEEE", edgecolor="#CCCCCC",
                linewidth=0.5, zorder=2)

# Green background above threshold
axD.fill_between([-1, NUM_CS], THR_DB, 6,
                 color="#E8F5E9", alpha=0.4, zorder=1)
# Threshold line
axD.axhline(THR_DB, color=C_THR, linewidth=1.8, linestyle="--", zorder=3,
            label=f"Detection threshold  ({THR_DB:.0f} dB)")
# Threshold text on the right side, below the line
axD.text(NUM_CS - 0.3, THR_DB - 3.5,
         f"Threshold\n{THR_DB:.0f} dB",
         color=C_THR, fontsize=8.5, fontweight="bold",
         ha="right", va="top")

# Colored bars for the 3 detected preambles
# stagger: #5 low offset (bar at index 5, far left), #14 high, #28 high
y_label_top_offsets = [1.0, 1.0, 1.0]   # uniform: label just above bar top
for m, cs in enumerate(CS_IDX):
    pw = cs_power_db[cs]
    axD.bar(cs, pw - (-32), width=1.0, bottom=-32,
            color=COLORS[m], edgecolor="#222222",
            linewidth=1.2, zorder=4,
            label=f"Preamble #{cs}  (CS {cs})  ✓ detected")


# Resource exhaustion consequence label — upper centre (above empty area)
# axD.text(0.5, 0.92,
#          f"→  gNB allocates {M} RA responses  ⚠ Resource Exhaustion Attack",
#          transform=axD.transAxes, color="#C62828",
#          fontsize=9, fontweight="bold", ha="center", va="top",
#          bbox=dict(boxstyle="round,pad=0.3", fc="#FFF3E0", ec="#C62828", alpha=0.97))

axD.set_xlim(-1, NUM_CS)
axD.set_ylim(-32, 9)
axD.set_xticks(cs_arr)
axD.set_xticklabels([str(v) if v % 2 == 0 else "" for v in cs_arr], fontsize=8)
axD.legend(loc="lower right", framealpha=0.95, edgecolor=C_GRID, fontsize=8.5, ncol=2)

# ─────────────────────────────────────────────────────────────────────────────
# Footer
# ─────────────────────────────────────────────────────────────────────────────
fig.text(
    0.5, 0.003,
    f"5G NR PRACH  |  ZC root $u = {ROOT_U}$  |  $N_{{ZC}} = {N_ZC}$  |  "
    f"$M = {M}$ preambles superimposed  |  CS indices: {CS_IDX}  |  "
    f"Threshold = {THR_DB} dB  |  Amplitude scaling ignored (illustration)",
    ha="center", fontsize=8, color=C_MUTED, style="italic"
)

out = "/Users/yq/Documents/analysis/0420/plot_attack_prach.png"
plt.savefig(out, dpi=160, bbox_inches="tight", facecolor="white")
print(f"[✓] Saved: {out}")
plt.show()

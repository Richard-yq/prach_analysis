"""
PRACH Preamble Detection Simulation
====================================
N_ZC=139, NCS=34 (zeroCorrelationZoneConfig=13)
Root u=138, 4 preambles per root (v=0,1,2,3)

Uses standard circular cross-correlation (not OAI IFFT method).
Peak for preamble v appears at lag k = v * NCS.

Math:
  R[k] = IFFT(FFT(root) * conj(FFT(rx)))[k]
       = sum_n  x_u[n] * conj(rx[(n-k) mod N_ZC])
  For rx = x_{u, shift=v*NCS}:
       = N_ZC * delta[k - v*NCS]   (CAZAC autocorrelation property)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────────────────────
# Parameters
# ─────────────────────────────────────────────────────────────
N_ZC          = 139
IFFT_SIZE     = 256     # reference only (not used in this correlator)
NCS           = 34
NUM_PREAMBLES = N_ZC // NCS   # = 4
ROOT_U        = 138
PREAMBLE_V    = [0, 1, 2, 3]
THR_DB        = -15.0
NOISE_STD     = 0.10    # complex AWGN std per component

COLORS = ["#C62828", "#1565C0", "#2E7D32", "#7B1FA2"]
C_SUM  = "#FF8F00"
C_THR  = "#E65100"
C_TEXT = "#212121"
C_MUTED= "#757575"
C_PANEL= "#FAFAFA"
C_GRID = "#E0E0E0"

np.random.seed(42)

# ─────────────────────────────────────────────────────────────
# ZC sequence and preamble helpers
# ─────────────────────────────────────────────────────────────
def zadoff_chu(u, N):
    """3GPP TS38.211: x_u[n] = exp(-j*pi*u*n*(n+1)/N)"""
    n = np.arange(N, dtype=float)
    return np.exp(-1j * np.pi * u * n * (n + 1) / N)

def make_preamble(u, N, cyclic_shift):
    return np.roll(zadoff_chu(u, N), cyclic_shift)

def circular_correlate(rx, root):
    """
    R[k] = IFFT(FFT(rx) * conj(FFT(root)))
         = sum_n rx[n] * conj(root[(n-k) mod N])
    For rx = cyclic-shift-v of root: peak at lag k = v*NCS.
    """
    N = len(root)
    R = np.fft.ifft(np.fft.fft(rx, N) * np.conj(np.fft.fft(root, N)))
    return np.abs(R) ** 2

# ─────────────────────────────────────────────────────────────
# Build signals
# ─────────────────────────────────────────────────────────────
root_seq        = zadoff_chu(ROOT_U, N_ZC)
preamble_shifts = [v * NCS for v in PREAMBLE_V]      # [0, 34, 68, 102]
preambles       = [make_preamble(ROOT_U, N_ZC, s) for s in preamble_shifts]

s_combined = np.sum(preambles, axis=0)
noise      = (np.random.randn(N_ZC) + 1j * np.random.randn(N_ZC)) * NOISE_STD
rx         = s_combined + noise

# ─────────────────────────────────────────────────────────────
# Correlation and normalization
# ─────────────────────────────────────────────────────────────
corr      = circular_correlate(rx, root_seq)
ref_power = circular_correlate(preambles[0], root_seq).max()   # = N_ZC^2 = 19321

def to_db(x):
    return 10 * np.log10(np.maximum(x / ref_power, 1e-12))

corr_db       = to_db(corr)
expected_lags = [v * NCS for v in PREAMBLE_V]   # [0, 34, 68, 102]
x_idx         = np.arange(N_ZC)

# Find actual peak within each guard zone (window of NCS samples)
detected_lags = []
for k_exp in expected_lags:
    end    = min(k_exp + NCS, N_ZC)
    offset = int(np.argmax(corr[k_exp:end]))
    detected_lags.append(k_exp + offset)

# ─────────────────────────────────────────────────────────────
# Figure layout
# ─────────────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10,
    "axes.titlesize": 11, "axes.labelsize": 10,
    "legend.fontsize": 9, "xtick.labelsize": 9, "ytick.labelsize": 9,
})

fig = plt.figure(figsize=(16, 8), facecolor="white")
fig.suptitle(
    f"5G NR PRACH — Preamble Detection Simulation\n"
    f"Root $u={ROOT_U}$,  $N_{{ZC}}={N_ZC}$,  $N_{{CS}}={NCS}$,  "
    f"{NUM_PREAMBLES} preambles per root  ($v = {PREAMBLE_V}$)",
    fontsize=13, fontweight="bold", color=C_TEXT, y=0.99
)

gs = gridspec.GridSpec(2, 2, figure=fig,
    left=0.07, right=0.98, top=0.90, bottom=0.08,
    hspace=0.70, wspace=0.28)

def style_ax(ax, title, xlabel, ylabel):
    ax.set_facecolor(C_PANEL)
    ax.set_title(title, color=C_TEXT, pad=8, fontweight="bold")
    ax.set_xlabel(xlabel, color=C_TEXT)
    ax.set_ylabel(ylabel, color=C_TEXT)
    ax.tick_params(colors=C_TEXT)
    ax.grid(True, color=C_GRID, linewidth=0.6, zorder=0)
    for sp in ax.spines.values():
        sp.set_edgecolor("#BDBDBD")

# ──────────────────────────────────────────────────────────────
# Panel ①  Individual preamble waveforms
# ──────────────────────────────────────────────────────────────
ax1 = fig.add_subplot(gs[0, 0])
style_ax(ax1,
    f"① Individual Preamble Waveforms  "
    f"(cyclic shift $= v \\times N_{{CS}} = v \\times {NCS}$ samples)",
    "Sample index $k$",
    r"$\mathrm{Re}\{x_{u,v}[k]\}$")

for i, (p, v, s) in enumerate(zip(preambles, PREAMBLE_V, preamble_shifts)):
    ax1.plot(x_idx, p.real, color=COLORS[i], linewidth=0.9, alpha=0.85,
             label=f"$v={v}$,  shift $= {s}$ samples")

ax1.set_xlim(0, N_ZC - 1)
ax1.legend(loc="lower right", framealpha=0.92, edgecolor=C_GRID,
           ncol=2, fontsize=8.5)
ax1.text(0.02, 0.05,
    r"$x_{u,v}[k]=x_u[(k+v\cdot N_{CS})\,\mathrm{mod}\,N_{ZC}]$,"
    r"   $|x_{u,v}[k]|=1$  (CAZAC)",
    transform=ax1.transAxes, color=C_MUTED, fontsize=9)

# ──────────────────────────────────────────────────────────────
# Panel ②  Superimposed received signal
# ──────────────────────────────────────────────────────────────
ax2 = fig.add_subplot(gs[0, 1])
style_ax(ax2,
    rf"② Superimposed Signal  "
    rf"$r[k]=\sum_{{v=0}}^{{3}} x_{{u,v}}[k]$",
    "Sample index $k$",
    r"$\mathrm{Re}\{r[k]\}$")

ax2.plot(x_idx, s_combined.real, color=C_SUM, linewidth=0.95, alpha=0.90,
         label=r"$\sum_v x_{u,v}[k]$", zorder=3)
ax2.axhline(0, color=C_MUTED, linewidth=0.5, linestyle=":")
ax2.set_xlim(0, N_ZC - 1)
ax2.legend(loc="upper right", framealpha=0.92, edgecolor=C_GRID, fontsize=8.5)
ax2.text(0.02, 0.05,
    f"Superposition of {NUM_PREAMBLES} orthogonal preambles — "
    f"appears noise-like in time domain",
    transform=ax2.transAxes, color=C_MUTED, fontsize=9)

# ──────────────────────────────────────────────────────────────
# Panel ③  Circular cross-correlation output
# ──────────────────────────────────────────────────────────────
ax3 = fig.add_subplot(gs[1, :])
style_ax(ax3,
    r"③ Circular Cross-Correlation  $|R[k]|^2$  — Preamble Detection",
    f"Lag $k$   (expected peaks at $k = v \\cdot N_{{CS}} = $ {expected_lags},  "
    f"guard zone width $= N_{{CS}} = {NCS}$ samples)",
    "Power  [dB  re. single-preamble peak]")

Y_MIN, Y_MAX = -45, 8

# Shade below-threshold region
ax3.fill_between(x_idx, Y_MIN, THR_DB, color="#ECEFF1", alpha=0.60,
                 label="Below threshold (noise floor)", zorder=1)

# Guard-zone shading (one per expected preamble slot)
for k_exp in expected_lags:
    ax3.axvspan(k_exp, min(k_exp + NCS - 1, N_ZC - 1),
                color="#E8EAF6", alpha=0.40, zorder=0)

# Correlation trace
ax3.plot(x_idx, corr_db, color="#37474F", linewidth=1.1, alpha=0.88,
         label=r"$|R[k]|^2$  (correlation output)", zorder=2)

# Threshold line
ax3.axhline(THR_DB, color=C_THR, linewidth=2.0, linestyle="--", zorder=4,
            label=f"Detection threshold  ({THR_DB:.0f} dB)")
ax3.text(N_ZC - 1, THR_DB + 0.9, f"{THR_DB:.0f} dB",
         color=C_THR, fontsize=8.5, fontweight="bold", ha="right")

# Annotate each detected peak
annot_cfg = [
    {"tx": 2,   "ty": -20, "ha": "left"},
    {"tx": 40,  "ty": -20, "ha": "left"},
    {"tx": 75,  "ty": -20, "ha": "left"},
    {"tx": 110, "ty": -20, "ha": "left"},
]
for i, (v, k_exp, k_act) in enumerate(zip(PREAMBLE_V, expected_lags, detected_lags)):
    db_val = corr_db[k_act]
    cfg    = annot_cfg[i]
    ax3.scatter([k_act], [db_val],
                color=COLORS[i], s=100, zorder=6,
                edgecolors="#333333", linewidths=0.9)
    ax3.axvline(k_act,
                color=COLORS[i], linewidth=0.9, linestyle=":", alpha=0.6, zorder=3)
    ax3.annotate(
        f"Preamble ${v}$\n"
        f"$k={v}\\times{NCS}={k_act}$  ✓",
        xy=(k_act, db_val),
        xytext=(cfg["tx"], cfg["ty"]),
        color=COLORS[i], fontsize=8.5, fontweight="bold", ha=cfg["ha"],
        arrowprops=dict(arrowstyle="->", color=COLORS[i], lw=0.9),
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=COLORS[i], alpha=0.95),
        zorder=7)

# Noise floor label
noise_floor_est = to_db(N_ZC * 2 * NOISE_STD**2)
ax3.text(N_ZC * 0.55, noise_floor_est + 5,
         f"Noise floor  ≈ {noise_floor_est:.0f} dB",
         color=C_MUTED, fontsize=8.5, ha="center")

ax3.set_xlim(-2, N_ZC + 1)
ax3.set_ylim(Y_MIN, Y_MAX)
ax3.legend(loc="lower right", framealpha=0.95, edgecolor=C_GRID,
           ncol=3, fontsize=8.5)

# ─────────────────────────────────────────────────────────────
# Footer
# ─────────────────────────────────────────────────────────────
fig.text(
    0.5, 0.007,
    r"Standard circular cross-correlation:  "
    r"$R[k]=\mathrm{IFFT}(\mathrm{FFT}(x_u)\cdot\mathrm{FFT}^*(r))$  |  "
    rf"$N_{{ZC}}={N_ZC}$, $u={ROOT_U}$, $N_{{CS}}={NCS}$  |  "
    r"Peak lag: $k=v\cdot N_\mathrm{CS}$",
    ha="center", fontsize=8, color=C_MUTED, style="italic"
)

out = "/Users/yq/Documents/analysis/0608/detect_preamble.png"
plt.savefig(out, dpi=160, bbox_inches="tight", facecolor="white")
print(f"[OK] Saved: {out}")

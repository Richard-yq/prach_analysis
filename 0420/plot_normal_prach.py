"""
Normal PRACH Preamble Detection Visualization
===============================================
Shows the complete detection chain for a single 5G NR PRACH preamble:

  UE transmits ZC sequence (root u=138, cyclic shift CS_v)
  ↓
  gNB receives + noise
  ↓
  DFT-based cross-correlation: R[n] = IDFT{ FFT(rx) · conj(FFT(X_u)) }
  ↓
  Single sharp peak at delay index n = CS_v × CS_step
  ↓
  Threshold comparison → preamble #v detected
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyArrowPatch
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────────────────────────────────────
# Parameters
# ─────────────────────────────────────────────────────────────────────────────
N_ZC    = 139        # ZC sequence length
NUM_CS  = 34         # number of cyclic-shift (preamble) candidates
CS_STEP = N_ZC // NUM_CS   # = 4 samples per CS slot

ROOT_U  = 138        # ZC root sequence index (coprime with 139 since 139 is prime)
CS_IDX  = 5          # preamble index (cyclic-shift slot) transmitted by UE

NOISE_STD = 0.02
THR_DB    = -13.0    # detection threshold (dB below peak)

np.random.seed(7)

# ─────────────────────────────────────────────────────────────────────────────
# ZC / PRACH helpers
# ─────────────────────────────────────────────────────────────────────────────
def zadoff_chu(u, N):
    n = np.arange(N, dtype=float)
    return np.exp(-1j * np.pi * u * n * (n + 1) / N)

def make_preamble(u, N, cs_idx, cs_step):
    xu = zadoff_chu(u, N)
    return np.roll(xu, cs_idx * cs_step)

def correlate(rx, u, N):
    """DFT-based PRACH correlator. Returns |R[n]|^2."""
    Xu = zadoff_chu(u, N)
    R  = np.fft.ifft(np.fft.fft(rx, N) * np.conj(np.fft.fft(Xu, N)), N)
    return np.abs(R) ** 2

# ─────────────────────────────────────────────────────────────────────────────
# Signal chain
# ─────────────────────────────────────────────────────────────────────────────
tx = make_preamble(ROOT_U, N_ZC, CS_IDX, CS_STEP)
noise = (np.random.randn(N_ZC) + 1j * np.random.randn(N_ZC)) * NOISE_STD
rx = tx + noise

corr = correlate(rx, ROOT_U, N_ZC)

# dB normalise to peak = 0 dB
def to_db(x, ref):
    return 10 * np.log10(np.maximum(x / ref, 1e-12))

ref     = corr.max()
corr_db = to_db(corr, ref)
thr_db  = THR_DB

# CS-slot sampled power (what gNB actually decides on)
cs_idx_arr  = np.arange(NUM_CS)
cs_power    = np.array([corr[(i * CS_STEP) % N_ZC] for i in range(NUM_CS)])
cs_power_db = to_db(cs_power, ref)

peak_sample = int(np.argmax(corr))
peak_cs     = int(np.argmax(cs_power_db))   # should equal CS_IDX

# ─────────────────────────────────────────────────────────────────────────────
# Style
# ─────────────────────────────────────────────────────────────────────────────
C_SIGNAL = "#1565C0"   # blue – ZC signal
C_CORR   = "#2E7D32"   # green – correlation
C_THR    = "#C62828"   # red   – threshold
C_NOISE  = "#E0E0E0"   # light grey – noise floor shade
C_PEAK   = "#E65100"   # orange – peak highlight
C_TEXT   = "#212121"
C_MUTED  = "#757575"
C_PANEL  = "#FAFAFA"
C_GRID   = "#E0E0E0"

plt.rcParams.update({
    "font.family"    : "DejaVu Sans",
    "font.size"      : 10,
    "axes.titlesize" : 11,
    "axes.labelsize" : 10,
    "legend.fontsize": 9,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "axes.spines.top"   : True,
    "axes.spines.right" : True,
})

fig = plt.figure(figsize=(14, 10), facecolor="white")
fig.suptitle(
    "5G NR PRACH — Normal Preamble Detection\n"
    f"(ZC root $u = {ROOT_U}$,  preamble CS index $= {CS_IDX}$,  "
    f"$N_{{ZC}} = {N_ZC}$)",
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
# Row 0  –  TX preamble (real part)  +  constellation
# ─────────────────────────────────────────────────────────────────────────────
axT = fig.add_subplot(gs[0, 0])
style(axT,
      "① UE Transmits: ZC Preamble (Real Part)",
      "Sample index $k$", "Amplitude")

axT.plot(np.arange(N_ZC), tx.real, color=C_SIGNAL, linewidth=0.8,
         label=f"$\\mathrm{{Re}}\\{{x_u[k]\\}}$,  $u={ROOT_U}$, CS={CS_IDX}")
axT.set_xlim(0, N_ZC - 1)
axT.set_ylim(-1.6, 1.6)
axT.axhline(0, color=C_MUTED, linewidth=0.5, linestyle=":")
axT.legend(loc="upper right", framealpha=0.9, edgecolor=C_GRID)
axT.text(0.02, 0.06,
         f"Unit-amplitude ZC sequence  |  $N_{{ZC}} = {N_ZC}$ samples",
         transform=axT.transAxes, color=C_MUTED, fontsize=8.5)

# Constellation (I/Q scatter)
axQ = fig.add_subplot(gs[0, 1])
style(axQ, "② ZC Sequence Constellation (I/Q)", "In-phase (I)", "Quadrature (Q)")
axQ.scatter(tx.real, tx.imag, s=3, color=C_SIGNAL, alpha=0.6, linewidths=0)
axQ.set_aspect("equal")
axQ.set_xlim(-1.5, 1.5)
axQ.set_ylim(-1.5, 1.5)
axQ.axhline(0, color=C_MUTED, linewidth=0.5, linestyle=":")
axQ.axvline(0, color=C_MUTED, linewidth=0.5, linestyle=":")
axQ.text(0.03, 0.93, f"$|x_u[k]| = 1$ (constant envelope)",
         transform=axQ.transAxes, color=C_MUTED, fontsize=8.5)

# ─────────────────────────────────────────────────────────────────────────────
# Row 1  –  Full correlation output (DFT-based)
# ─────────────────────────────────────────────────────────────────────────────
axC = fig.add_subplot(gs[1, :])   # spans both columns
style(axC,
      "③ gNB DFT-Based Cross-Correlation Output  $|R_u[n]|^2$",
      "Sample index $n$  (proportional to propagation delay)",
      "Power  [dB  re. peak]")

x_full = np.arange(N_ZC)
axC.fill_between(x_full, -32, thr_db, color=C_NOISE, alpha=0.5,
                 label="Noise floor (below threshold)", zorder=1)
axC.plot(x_full, corr_db, color=C_CORR, linewidth=1.0,
         alpha=0.9, label="$|R_u[n]|^2$", zorder=2)
axC.axhline(thr_db, color=C_THR, linewidth=1.5, linestyle="--",
            label=f"Detection threshold  ({thr_db:.0f} dB)", zorder=3)

# Highlight peak
axC.scatter([peak_sample], [corr_db[peak_sample]],
            color=C_PEAK, s=90, zorder=5, edgecolors="#333", linewidths=0.8)

# Vertical line at peak
axC.axvline(peak_sample, color=C_PEAK, linewidth=0.8,
            linestyle=":", alpha=0.7, zorder=2)

# Annotation – place right of peak, not too close to edge
ann_x = peak_sample + 55
axC.annotate(
    f"Peak at $n = {peak_sample}$\n"
    f"= CS index {CS_IDX} × {CS_STEP} samples\n"
    f"→ Preamble #{CS_IDX} detected",
    xy=(peak_sample, corr_db[peak_sample]),
    xytext=(ann_x, -2.5),
    color=C_TEXT, fontsize=9,
    arrowprops=dict(arrowstyle="->", color="#444", lw=0.9),
    bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#BDBDBD", alpha=0.95)
)

# Label noise floor
axC.text(N_ZC * 0.55, thr_db - 5,
         "Noise floor  (side-lobes, interference)",
         color=C_MUTED, fontsize=8.5, ha="center")

# Arrow showing peak height above threshold
axC.annotate("", xy=(peak_sample + 18, 0),
             xytext=(peak_sample + 18, thr_db),
             arrowprops=dict(arrowstyle="<->", color=C_THR, lw=1.2))
axC.text(peak_sample + 25, thr_db / 2,
         f"{abs(thr_db):.0f} dB\nmargin",
         color=C_THR, fontsize=8, va="center")

axC.set_xlim(0, N_ZC - 1)
axC.set_ylim(-32, 6)
axC.legend(loc="upper right", framealpha=0.95, edgecolor=C_GRID, ncol=3)

# ─────────────────────────────────────────────────────────────────────────────
# Row 2  –  Per-CS-slot detection map (bar chart)
# ─────────────────────────────────────────────────────────────────────────────
axD = fig.add_subplot(gs[2, :])
style(axD,
      f"④ gNB Decision: Correlation Power per Preamble Slot  ({NUM_CS} candidates)",
      "Preamble index  (cyclic-shift slot $v$)",
      "Power  [dB  re. peak]")

bar_c = [C_CORR if v >= thr_db else C_NOISE for v in cs_power_db]
axD.bar(cs_idx_arr, cs_power_db, color=bar_c, width=0.75,
        alpha=0.85, zorder=2, label="Corr. power at CS slot $v$")

# Highlight detected bar with orange edge
axD.bar([peak_cs], [cs_power_db[peak_cs]], color=C_CORR, width=0.75,
        alpha=1.0, zorder=3, edgecolor=C_PEAK, linewidth=2.0)

axD.axhline(thr_db, color=C_THR, linewidth=1.5, linestyle="--",
            label=f"Threshold  ({thr_db:.0f} dB)")
axD.fill_between([-1, NUM_CS], -32, thr_db, color=C_NOISE, alpha=0.35, zorder=1)

# Annotate detected slot
axD.annotate(
    f"✓  Preamble #{peak_cs} detected\n    (only 1 peak ≥ threshold)",
    xy=(peak_cs, cs_power_db[peak_cs]),
    xytext=(peak_cs + 7, 2.0),
    color=C_PEAK, fontsize=9, fontweight="bold",
    arrowprops=dict(arrowstyle="->", color=C_PEAK, lw=1.0),
    bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=C_PEAK, alpha=0.95)
)

# Cost label
axD.text(0.99, 0.06,
         "→  gNB allocates 1 RA response  (normal cost)",
         transform=axD.transAxes, color=C_CORR,
         fontsize=9, fontweight="bold", ha="right",
         bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=C_CORR, alpha=0.9))

axD.set_xlim(-1, NUM_CS)
axD.set_ylim(-32, 8)
axD.set_xticks(cs_idx_arr[::4])
axD.legend(loc="upper right", framealpha=0.95, edgecolor=C_GRID)

# ─────────────────────────────────────────────────────────────────────────────
# Footer
# ─────────────────────────────────────────────────────────────────────────────
fig.text(
    0.5, 0.003,
    f"5G NR PRACH  |  ZC root $u = {ROOT_U}$  |  $N_{{ZC}} = {N_ZC}$  |  "
    f"CS step = {CS_STEP} samples  |  {NUM_CS} preamble candidates  |  "
    f"Noise $\\sigma = {NOISE_STD}$  |  Threshold = {thr_db} dB below peak",
    ha="center", fontsize=8, color=C_MUTED, style="italic"
)

# ─────────────────────────────────────────────────────────────────────────────
# Save
# ─────────────────────────────────────────────────────────────────────────────
out = "/Users/yq/Documents/analysis/0420/plot_normal_prach.png"
plt.savefig(out, dpi=160, bbox_inches="tight", facecolor="white")
print(f"[✓] Saved: {out}")
plt.show()

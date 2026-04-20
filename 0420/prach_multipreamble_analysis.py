"""
PRACH Multi-Preamble Attack Analysis
======================================
Simulates and visualizes:
  1. Normal single-preamble PRACH detection (ZC correlation output)
  2. Multi-preamble attack signal detection (M preambles superimposed)

5G NR PRACH uses Zadoff-Chu (ZC) sequences.
The gNB detects preambles by cross-correlating (in frequency domain via DFT)
the received signal with each root ZC sequence X_u; the IDFT output has a
sharp peak at the cyclic-shift delay index corresponding to the transmitted
preamble.

Attack (from readme.md / nr_prach.c modification):
  Y_attack[k] = sum_{m=0}^{M-1}  (alpha/M) * X_{u_m}[k] * exp(-j2pi*k*Cv_m/N_ZC)
  → M simultaneous peaks appear in the gNB correlator → M RA responses triggered
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────────────────────────────────────
# Parameters  (5G NR long-format PRACH, format 0)
# ─────────────────────────────────────────────────────────────────────────────
N_ZC         = 839          # ZC sequence length
NUM_CS       = 64           # number of cyclic-shift candidates per root
CS_STEP      = N_ZC // NUM_CS   # = 13 samples per CS slot

# ── Attack config  (matches readme: num_attack_sequences = 3) ─────────────────
M            = 3
ALPHA        = 1.0
# Attacker transmits at full power alpha; each component is alpha/M.
# But the ZC correlator for each root sees a matched peak ~ alpha/M * N_ZC.
# To make the peaks detectably above threshold (realistic: attacker raises TX power),
# we set ALPHA_ATTACK = M (so per-component amp = 1, same as normal UE).
# This models the worst-case scenario where the attacker compensates 1/M scaling
# by boosting overall TX power by factor M (still within UE max TX power budget
# for a jammer hardware scenario).
ALPHA_ATTACK = float(M)               # total TX amplitude (attacker)

# Different root sequences for each attack preamble
ROOT_U_NORMAL = 138                    # root used by the normal UE
PREAMBLE_CS_NORMAL = 3                 # cyclic-shift index

# Attack uses 3 different (root, CS-index) pairs — mimics 3 distinct UEs
# Use spread-out CS indices to avoid peak overlap in the delay domain
ROOT_U_ATTACK    = [138,  138, 138]
CS_IDX_ATTACK    = [  3,   15,  30]   # well-separated CS slot indices

# Noise (very low to keep peaks clean)
NOISE_STD    = 0.015

# ─────────────────────────────────────────────────────────────────────────────
# ZC helpers
# ─────────────────────────────────────────────────────────────────────────────
def zadoff_chu(u, N):
    n = np.arange(N, dtype=float)
    return np.exp(-1j * np.pi * u * n * (n + 1) / N)

def prach_preamble(u, N, cs_samples):
    """ZC root sequence with cyclic shift of cs_samples."""
    xu = zadoff_chu(u, N)
    return np.roll(xu, cs_samples)

def correlate_full(rx, u, N):
    """
    DFT-based PRACH correlator.
    R[n] = IDFT{ FFT(rx) · conj(FFT(X_u)) }
    Returns |R[n]|^2 for n = 0 … N-1
    """
    Xu  = zadoff_chu(u, N)
    R   = np.fft.ifft(np.fft.fft(rx, N) * np.conj(np.fft.fft(Xu, N)), N)
    return np.abs(R) ** 2

def cs_sampled_power(corr_power, num_cs, step):
    """
    Sample the full correlation at each expected cyclic-shift position.
    Returns array of length num_cs.
    """
    return np.array([corr_power[(i * step) % len(corr_power)]
                     for i in range(num_cs)])

# ─────────────────────────────────────────────────────────────────────────────
# Build received signals
# ─────────────────────────────────────────────────────────────────────────────
np.random.seed(42)
noise = lambda: (np.random.randn(N_ZC) + 1j * np.random.randn(N_ZC)) * NOISE_STD

# Normal: single preamble
s_normal   = prach_preamble(ROOT_U_NORMAL, N_ZC, PREAMBLE_CS_NORMAL * CS_STEP)
rx_normal  = ALPHA * s_normal + noise()

# Attack: superposition of M preambles
#   Each component amplitude = ALPHA_ATTACK / M = 1.0  (same as normal UE's amplitude)
#   This is the worst-case attacker: boosts total TX power by M to compensate scaling.
s_attack = np.zeros(N_ZC, dtype=complex)
for m in range(M):
    s_attack += (ALPHA_ATTACK / M) * prach_preamble(ROOT_U_ATTACK[m], N_ZC,
                                                     CS_IDX_ATTACK[m] * CS_STEP)
rx_attack = s_attack + noise()

# ─────────────────────────────────────────────────────────────────────────────
# Run gNB correlator
# ─────────────────────────────────────────────────────────────────────────────
corr_normal  = correlate_full(rx_normal,  ROOT_U_NORMAL, N_ZC)
NORM_PEAK    = corr_normal.max()            # reference power → 0 dB

def db(x): return 10 * np.log10(np.maximum(x / NORM_PEAK, 1e-12))

# Threshold: 13 dB below the normal peak (typical PRACH det. threshold margin)
THR_DB = -13.0
THR_LIN = NORM_PEAK * 10 ** (THR_DB / 10)

# Normal CS-indexed output
cs_normal_lin = cs_sampled_power(corr_normal, NUM_CS, CS_STEP)
cs_normal_db  = db(cs_normal_lin)

# Attack correlations (one per root sequence used)
corr_attack   = [correlate_full(rx_attack, ROOT_U_ATTACK[m], N_ZC) for m in range(M)]
cs_attack_lin = [cs_sampled_power(corr_attack[m], NUM_CS, CS_STEP) for m in range(M)]
cs_attack_db  = [db(cs_attack_lin[m]) for m in range(M)]

# Per-attack-root detection threshold (same dB offset applied relative to *that* root's peak)
# This matches what the gNB actually does: threshold is relative to noise floor, not peak,
# but for visualization we use the same -13 dB from the normal-case reference.
ATK_THR_DB = [db(cs_attack_lin[m]).max() - 13.0 for m in range(M)]

# ─────────────────────────────────────────────────────────────────────────────
# Plot Style
# ─────────────────────────────────────────────────────────────────────────────
BG      = "#FFFFFF"
PANEL   = "#F8F9FA"
GRID    = "#DEE2E6"
TEXT    = "#212529"
MUTED   = "#6C757D"

C_NORMAL  = "#1A7F3C"          # dark green
C_ATTACK  = ["#C0392B", "#1A6EBD", "#B7770D"]  # deep red, blue, amber
C_THR     = "#E03131"
C_NOISE   = "#CED4DA"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10.5,
    "axes.titlesize": 12,
    "axes.labelsize": 10,
    "legend.fontsize": 8.5,
    "xtick.labelsize": 8.5,
    "ytick.labelsize": 8.5,
    "axes.facecolor": "#F8F9FA",
    "figure.facecolor": "#FFFFFF",
    "text.color": "#212529",
    "axes.labelcolor": "#212529",
    "xtick.color": "#212529",
    "ytick.color": "#212529",
})

fig = plt.figure(figsize=(17, 11), facecolor=BG)
fig.suptitle(
    "5G NR PRACH Preamble Detection  ·  Normal UE  vs.  Multi-Preamble Attack",
    fontsize=15, fontweight="bold", color=TEXT, y=0.975
)

gs = gridspec.GridSpec(2, 2, figure=fig,
                       left=0.07, right=0.97,
                       top=0.93, bottom=0.08,
                       hspace=0.50, wspace=0.35)

x_full = np.arange(N_ZC)
x_cs   = np.arange(NUM_CS)

def style_ax(ax, title, xlabel, ylabel):
    ax.set_facecolor(PANEL)
    ax.set_title(title, color=TEXT, pad=8, fontweight="bold")
    ax.set_xlabel(xlabel, color=TEXT)
    ax.set_ylabel(ylabel, color=TEXT)
    ax.tick_params(colors=TEXT, which="both")
    ax.grid(True, color=GRID, linewidth=0.6, alpha=0.8, zorder=0)
    for sp in ax.spines.values():
        sp.set_edgecolor(GRID)

def add_threshold(ax, label=True):
    lbl = f"Detection threshold  ({THR_DB:.0f} dB)" if label else "_nolegend_"
    ax.axhline(THR_DB, color=C_THR, linewidth=1.4, linestyle="--",
               label=lbl, zorder=3)

# =============================================================================
# Panel A – Normal: full DFT correlation output
# =============================================================================
axA = fig.add_subplot(gs[0, 0])
style_ax(axA,
         "① Normal UE  —  Correlation Output (full)",
         "Sample index  $n$  (proportional to delay)", "Power  [dB  re. peak]")

axA.plot(x_full, db(corr_normal), color=C_NORMAL, linewidth=0.9, alpha=0.9,
         label=f"$|R_{{u}}[n]|^2$  (root $u = {ROOT_U_NORMAL}$)", zorder=2)
add_threshold(axA)

# Annotate the single peak
pk_n = int(np.argmax(corr_normal))
axA.scatter([pk_n], [db(corr_normal[pk_n])], color=C_NORMAL,
            s=80, zorder=5, marker='o',
            edgecolors="#333333", linewidths=1.2)
axA.annotate(
    f"Single peak  (CS index {PREAMBLE_CS_NORMAL})\n$n = {pk_n}$",
    xy=(pk_n, db(corr_normal[pk_n])),
    xytext=(pk_n + 80, -1.5),
    color=TEXT, fontsize=8.5,
    arrowprops=dict(arrowstyle="->", color="#444444", lw=0.8)
)

axA.set_xlim(0, N_ZC - 1)
axA.set_ylim(-28, 6)
axA.legend(loc="upper right", framealpha=0.25,
           labelcolor=TEXT, facecolor=PANEL, edgecolor=GRID)

# Shade noise floor
axA.fill_between(x_full, -28, THR_DB, color=C_NOISE, alpha=0.25, zorder=1)
axA.text(400, THR_DB - 4.5, "Noise floor  (below threshold)", color=MUTED,
         fontsize=8, ha="center")

# =============================================================================
# Panel B – Attack: full DFT correlation output (all M roots overlaid)
# =============================================================================
axB = fig.add_subplot(gs[0, 1])
style_ax(axB,
         f"② Multi-Preamble Attack  —  Correlation Output  ($M={M}$)",
         "Sample index  $n$", "Power  [dB  re. peak]")

# Stagger y-offsets for peak annotations so they don't overlap
B_ANNOT_Y = [2.5, 4.5, 2.5]   # alternating heights above peak
for m in range(M):
    axB.plot(x_full, db(corr_attack[m]),
             color=C_ATTACK[m], linewidth=0.85, alpha=0.88,
             label=f"Root $u={ROOT_U_ATTACK[m]}$, CS idx {CS_IDX_ATTACK[m]}",
             zorder=2)
    # Peak marker
    pk_m = int(np.argmax(corr_attack[m]))
    pk_db = db(corr_attack[m][pk_m])
    axB.scatter([pk_m], [pk_db],
                color=C_ATTACK[m], s=70, zorder=5,
                edgecolors="#333333", linewidths=0.8)
    axB.annotate(
        f"Peak {m+1}  (CS {CS_IDX_ATTACK[m]})",
        xy=(pk_m, pk_db),
        xytext=(pk_m + 55, pk_db + B_ANNOT_Y[m]),
        color=C_ATTACK[m], fontsize=8,
        arrowprops=dict(arrowstyle="->", color=C_ATTACK[m], lw=0.7)
    )

add_threshold(axB)
axB.set_xlim(0, N_ZC - 1)
axB.set_ylim(-28, 8)
axB.fill_between(x_full, -28, THR_DB, color=C_NOISE, alpha=0.25, zorder=1)

# Legend top-right, annotation box bottom-center (no overlap)
axB.legend(loc="upper right", framealpha=0.85,
           labelcolor=TEXT, facecolor=PANEL, edgecolor=GRID)

# Annotation box placed at bottom-left, away from peaks and legend
axB.text(0.02, 0.04,
         f"{M} peaks ≥ threshold  →  gNB triggers {M} RA responses\n"
         f"⚠ Resource Exhaustion Attack",
         transform=axB.transAxes, color="#C0392B",
         fontsize=8.5, fontweight="bold", va="bottom",
         bbox=dict(boxstyle="round,pad=0.40", fc="#FFF0F0", ec="#C0392B",
                   alpha=0.92))

# =============================================================================
# Panel C – Normal: per-CS-slot detection (bar chart)
# =============================================================================
axC = fig.add_subplot(gs[1, 0])
style_ax(axC,
         "③ gNB Correlator  —  Per-Cyclic-Shift Map  (Normal UE)",
         "Preamble slot index  (cyclic shift)", "Power  [dB  re. peak]")

bar_colors_n = [C_NORMAL if v >= THR_DB else C_NOISE for v in cs_normal_db]
axC.bar(x_cs, cs_normal_db, color=bar_colors_n, width=0.75, alpha=0.9,
        zorder=2, label="Correlation per CS slot")
add_threshold(axC)

# Detected bar highlight
det_n = int(np.argmax(cs_normal_db))
axC.bar([det_n], [cs_normal_db[det_n]], color=C_NORMAL,
        width=0.75, alpha=1.0, zorder=3, edgecolor="#FFFFFF", linewidth=1.2)
axC.annotate(f"✓  Preamble #{det_n}  detected",
             xy=(det_n, cs_normal_db[det_n]),
             xytext=(det_n + 8, 2.5),
             color=C_NORMAL, fontsize=8.5, fontweight="bold",
             arrowprops=dict(arrowstyle="->", color=C_NORMAL, lw=0.8))

axC.set_xlim(-1, NUM_CS)
axC.set_ylim(-26, 8)
axC.set_xticks(x_cs[::8])
axC.fill_between([-1, NUM_CS], -26, THR_DB, color=C_NOISE, alpha=0.2)

# "Cost" label at bottom-right, legend at upper-right
axC.text(0.98, 0.04,
         "Cost:  1 RA response  (NORMAL)",
         transform=axC.transAxes, color=C_NORMAL,
         fontsize=8.5, style="italic", fontweight="bold", ha="right")
axC.legend(loc="upper right", framealpha=0.85,
           labelcolor=TEXT, facecolor=PANEL, edgecolor=GRID)

# =============================================================================
# Panel D – Attack: per-CS-slot detection (grouped bars, one group per root)
# =============================================================================
axD = fig.add_subplot(gs[1, 1])
style_ax(axD,
         f"④ gNB Correlator  —  Per-Cyclic-Shift Map  (Attack, $M={M}$)",
         "Preamble slot index  (cyclic shift)", "Power  [dB  re. peak]")

bw   = 0.75 / M              # width of each sub-bar
off0 = -(M - 1) * bw / 2    # offset for first sub-bar

# Stagger annotation y-offsets to prevent overlap
D_ANNOT_Y = [5.5, 3.5, 1.5]   # descending heights so arrows diverge

det_labels = []
for m in range(M):
    offsets = x_cs + off0 + m * bw
    # Use per-root threshold for coloring
    bar_c   = [C_ATTACK[m] if v >= ATK_THR_DB[m] else C_NOISE
               for v in cs_attack_db[m]]
    axD.bar(offsets, cs_attack_db[m], width=bw, color=bar_c,
            alpha=0.88, zorder=2,
            label=f"Root $u={ROOT_U_ATTACK[m]}$, CS idx {CS_IDX_ATTACK[m]}")

    # Highlight the detected bar
    det_m = int(np.argmax(cs_attack_db[m]))
    det_labels.append(det_m)
    axD.bar([offsets[det_m]], [cs_attack_db[m][det_m]],
            width=bw, color=C_ATTACK[m], alpha=1.0,
            zorder=3, edgecolor="#333333", linewidth=0.8)
    # Staggered annotation: place text to the right of the bar with varying y
    axD.annotate(
        f"✓ CS {CS_IDX_ATTACK[m]}",
        xy=(offsets[det_m], cs_attack_db[m][det_m]),
        xytext=(offsets[det_m] + 5, D_ANNOT_Y[m]),
        color=C_ATTACK[m], fontsize=8, fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=C_ATTACK[m], lw=0.6)
    )

add_threshold(axD)
axD.set_xlim(-1, NUM_CS)
axD.set_ylim(-26, 8)
axD.set_xticks(x_cs[::8])
axD.fill_between([-1, NUM_CS], -26, THR_DB, color=C_NOISE, alpha=0.2)

# Cost label at bottom-right; legend at upper-right
axD.text(0.98, 0.04,
         f"Cost:  {M}× RA responses  →  RESOURCE EXHAUSTION",
         transform=axD.transAxes, color="#C0392B",
         fontsize=8.5, style="italic", fontweight="bold", ha="right")
axD.legend(loc="upper right", framealpha=0.85,
           labelcolor=TEXT, facecolor=PANEL, edgecolor=GRID)

# =============================================================================
# Footer
# =============================================================================
fig.text(
    0.5, 0.003,
    (f"5G NR PRACH  |  $N_{{ZC}}={N_ZC}$  |  Cyclic shifts = {NUM_CS}  |  "
     f"Attack: $M={M}$, amplitude $= \\alpha/M$ each  |  "
     f"Roots used: {ROOT_U_ATTACK}  |  CS indices: {CS_IDX_ATTACK}  |  "
     f"Threshold: {THR_DB} dB below peak"),
    ha="center", fontsize=7.8, color=MUTED, style="italic"
)

# =============================================================================
# Save
# =============================================================================
out = "/Users/yq/Documents/analysis/0420/prach_multipreamble_analysis.png"
plt.savefig(out, dpi=160, bbox_inches="tight", facecolor=BG)
print(f"[✓] Saved: {out}")
plt.show()

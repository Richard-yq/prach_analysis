"""
5G NR PRACH Preamble Detection Animation
=========================================
Animates the effect of different Root Indices (u) on the received signal waveform
and the corresponding circular cross-correlation output.

Root indices sequence:
[1, 138, 2, 137, 3, 136, 4, 135, 5, 134, 6, 133, 7, 132, 8, 131]
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.animation import FuncAnimation, PillowWriter
import os
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────────────────────
# Parameters
# ─────────────────────────────────────────────────────────────
N_ZC          = 139
NCS           = 34
NUM_PREAMBLES = N_ZC // NCS   # = 4
PREAMBLE_V    = [0, 1, 2, 3]
THR_DB        = -15.0
NOISE_STD     = 0.10          # complex AWGN std per component

# The 16 root indices requested by the user
ROOT_INDICES = [1, 138, 2, 137, 3, 136, 4, 135, 5, 134, 6, 133, 7, 132, 8, 131] # 38.211 Table 6.3.3.1-4:

# Aesthetics
COLORS = ["#C62828", "#1565C0", "#2E7D32", "#7B1FA2"]
C_SUM  = "#FF8F00"
C_THR  = "#E65100"
C_TEXT = "#212121"
C_MUTED= "#757575"
C_PANEL= "#FAFAFA"
C_GRID = "#E0E0E0"

# Fix seed for noise consistency across roots
np.random.seed(42)
fixed_noise = (np.random.randn(N_ZC) + 1j * np.random.randn(N_ZC)) * NOISE_STD

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
    N = len(root)
    R = np.fft.ifft(np.fft.fft(rx, N) * np.conj(np.fft.fft(root, N)))
    return np.abs(R) ** 2

def to_db(x, ref_power):
    return 10 * np.log10(np.maximum(x / ref_power, 1e-12))

# ─────────────────────────────────────────────────────────────
# Animation setup
# ─────────────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10,
    "axes.titlesize": 11, "axes.labelsize": 10,
    "legend.fontsize": 9, "xtick.labelsize": 9, "ytick.labelsize": 9,
})

fig = plt.figure(figsize=(16, 9), facecolor="white")
gs = gridspec.GridSpec(2, 2, figure=fig,
                       left=0.06, right=0.98, top=0.88, bottom=0.07,
                       hspace=0.38, wspace=0.22)

# Subplots
ax_indiv = fig.add_subplot(gs[0, 0])      # Top-Left: Individual Preamble Waveforms
ax_sum   = fig.add_subplot(gs[0, 1])      # Top-Right: Superimposed Preamble Waveform (Tx)
ax_noise = fig.add_subplot(gs[1, 0])      # Bottom-Left: Noisy Received Preamble Waveform (Rx)
ax_corr  = fig.add_subplot(gs[1, 1])      # Bottom-Right: Correlation output

def style_ax(ax, title, xlabel, ylabel):
    ax.set_facecolor(C_PANEL)
    ax.set_title(title, color=C_TEXT, pad=8, fontweight="bold")
    ax.set_xlabel(xlabel, color=C_TEXT)
    ax.set_ylabel(ylabel, color=C_TEXT)
    ax.tick_params(colors=C_TEXT)
    ax.grid(True, color=C_GRID, linewidth=0.6, zorder=0)
    for sp in ax.spines.values():
        sp.set_edgecolor("#BDBDBD")

# Initialize plots
style_ax(ax_indiv, "① Individual Preamble Waveforms (Real Part)", "Sample index $k$", r"$\mathrm{Re}\{x_{u,v}[k]\}$")
style_ax(ax_sum, "② Superimposed Preamble Waveform (Tx) (Real Part)", "Sample index $k$", r"$\mathrm{Re}\{s_{\mathrm{sum}}[k]\}$")
style_ax(ax_noise, "③ Noisy Received Preamble Waveform (Rx) (Real Part)", "Sample index $k$", r"$\mathrm{Re}\{r[k]\}$")
style_ax(ax_corr, "④ Circular Cross-Correlation $|R[k]|^2$ (dB Scale)", "Lag $k$", "Power [dB re. peak]")

# Set axis limits
x_idx = np.arange(N_ZC)
ax_indiv.set_xlim(0, N_ZC - 1)
ax_indiv.set_ylim(-1.3, 1.3)

ax_sum.set_xlim(0, N_ZC - 1)
ax_sum.set_ylim(-3.5, 3.5)

ax_noise.set_xlim(0, N_ZC - 1)
ax_noise.set_ylim(-3.5, 3.5)

ax_corr.set_xlim(-2, N_ZC + 1)
ax_corr.set_ylim(-45, 8)

# Static visual elements for Correlation Plot
ax_corr.fill_between(x_idx, -45, THR_DB, color="#ECEFF1", alpha=0.60, label="Below threshold (noise floor)", zorder=1)
expected_lags = [v * NCS for v in PREAMBLE_V]
for k_exp in expected_lags:
    ax_corr.axvspan(k_exp, min(k_exp + NCS - 1, N_ZC - 1), color="#E8EAF6", alpha=0.40, zorder=0)
ax_corr.axhline(THR_DB, color=C_THR, linewidth=1.8, linestyle="--", zorder=4, label=f"Detection threshold ({THR_DB} dB)")

# Static elements for sum and noise plots
ax_sum.axhline(0, color=C_MUTED, linewidth=0.5, linestyle=":")
ax_noise.axhline(0, color=C_MUTED, linewidth=0.5, linestyle=":")

# Handle objects that will be updated in animation
lines_indiv = []
for i in range(NUM_PREAMBLES):
    line, = ax_indiv.plot([], [], color=COLORS[i], linewidth=0.9, alpha=0.85,
                          label=f"$v={i}$, shift $={i*NCS}$")
    lines_indiv.append(line)

line_sum, = ax_sum.plot([], [], color=C_SUM, linewidth=1.2, label=r"Superimposed Waveform (Tx) $\sum_v x_{u,v}[k]$", zorder=3)
line_noise, = ax_noise.plot([], [], color="#00897B", linewidth=1.2, label=r"Noisy Waveform (Rx) $r[k]$", zorder=3)
line_corr, = ax_corr.plot([], [], color="#37474F", linewidth=1.2, label=r"Correlation $|R[k]|^2$", zorder=2)
scatters = ax_corr.scatter([0, 0, 0, 0], [0, 0, 0, 0], color=COLORS, s=80, zorder=6, edgecolors="#333333", linewidths=0.9)

# For annotations and lines, we'll keep list of items to clear or update
vlines = []
annotations = []
title_text = fig.suptitle("", fontsize=14, fontweight="bold", color=C_TEXT, y=0.97)

# Add legends once
ax_indiv.legend(loc="lower right", framealpha=0.92, edgecolor=C_GRID, ncol=2, fontsize=8)
ax_sum.legend(loc="upper right", framealpha=0.92, edgecolor=C_GRID, fontsize=8)
ax_noise.legend(loc="upper right", framealpha=0.92, edgecolor=C_GRID, fontsize=8)
ax_corr.legend(loc="lower right", framealpha=0.92, edgecolor=C_GRID, ncol=3, fontsize=8)

# Note in individual plot
note_indiv = ax_indiv.text(0.01, 0.05, "", transform=ax_indiv.transAxes, color=C_MUTED, fontsize=8.5, fontweight="bold")

def animate(frame_idx):
    # Get current root index u
    u = ROOT_INDICES[frame_idx]
    
    # 1. Generate signal
    root_seq = zadoff_chu(u, N_ZC)
    preamble_shifts = [v * NCS for v in PREAMBLE_V]
    preambles = [make_preamble(u, N_ZC, s) for s in preamble_shifts]
    s_combined = np.sum(preambles, axis=0)
    rx = s_combined + fixed_noise
    
    # 2. Correlate
    corr = circular_correlate(rx, root_seq)
    ref_power = circular_correlate(preambles[0], root_seq).max()
    corr_db = to_db(corr, ref_power)
    
    # 3. Find peaks
    detected_lags = []
    for k_exp in preamble_shifts:
        end = min(k_exp + NCS, N_ZC)
        offset = int(np.argmax(corr[k_exp:end]))
        detected_lags.append(k_exp + offset)
    
    # 4. Update Time Plots
    # 4.1 Update Individual Preamble Waveforms
    for i, p in enumerate(preambles):
        lines_indiv[i].set_data(x_idx, p.real)
        
    # 4.2 Update Superimposed Preamble Signal
    line_sum.set_data(x_idx, s_combined.real)
    
    # 4.3 Update Received Signal with Noise
    line_noise.set_data(x_idx, rx.real)
    
    # Check conjugation relationship (e.g. u and 139-u)
    # 139 is prime, u and 139-u are complex conjugates
    conj_partner = 139 - u
    note_indiv.set_text(f"Root Index $u = {u}$\nComplex conjugate of $u = {conj_partner}$")
    
    # 5. Update Correlation Plot
    line_corr.set_data(x_idx, corr_db)
    
    # Update Scatter Points for Peaks
    peak_y = [corr_db[lag] for lag in detected_lags]
    scatters.set_offsets(np.column_stack((detected_lags, peak_y)))
    
    # Clear old vertical lines and annotations
    global vlines, annotations
    for vl in vlines:
        vl.remove()
    vlines.clear()
    for ann in annotations:
        ann.remove()
    annotations.clear()
    
    # Draw new vertical lines and annotations
    annot_cfg = [
        {"tx": 3,   "ty": -20, "ha": "left"},
        {"tx": 38,  "ty": -20, "ha": "left"},
        {"tx": 72,  "ty": -20, "ha": "left"},
        {"tx": 106, "ty": -20, "ha": "left"},
    ]

    for i, (v, k_act, y_val) in enumerate(zip(PREAMBLE_V, detected_lags, peak_y)):
        # Vertical line
        vl = ax_corr.axvline(k_act, color=COLORS[i], linewidth=0.9, linestyle=":", alpha=0.7, zorder=3)
        vlines.append(vl)
        
        # Global preamble index
        v_global = frame_idx * NUM_PREAMBLES + v
        
        # Annotation box
        cfg = annot_cfg[i]
        ann = ax_corr.annotate(
            f"Preamble ${v_global}$\n$k={k_act}$",
            xy=(k_act, y_val),
            xytext=(cfg["tx"], cfg["ty"]),
            color=COLORS[i], fontsize=8.5, fontweight="bold", ha=cfg["ha"],
            arrowprops=dict(arrowstyle="->", color=COLORS[i], lw=0.9),
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=COLORS[i], alpha=0.9),
            zorder=7
        )
        annotations.append(ann)
        
    # Update Suptitle
    title_text.set_text(
        f"PRACH Preamble Transmit & Receive Signal Simulation — Varying Root Index ($u$)\n"
        f"Active Root: $u={u}$  |  $N_{{ZC}}={N_ZC}$  |  $N_{{CS}}={NCS}$  | {frame_idx + 1}/{len(ROOT_INDICES)}"
    )
    
    return lines_indiv + [line_sum, line_noise, line_corr, scatters] + vlines + annotations

# Create animation
anim = FuncAnimation(fig, animate, frames=len(ROOT_INDICES), interval=1000, blit=False)

# Save to GIF
gif_path = "/Users/yq/Documents/analysis/0609/detect_preamble_roots.gif"
print(f"Generating GIF animation at {gif_path} ...")
writer = PillowWriter(fps=1)
anim.save(gif_path, writer=writer)
print("[OK] Finished saving GIF animation!")

# Also display if run interactively (will not block the non-interactive execution if saved)
# plt.show()

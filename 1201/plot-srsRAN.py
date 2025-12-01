"""
PRACH Detection Mechanism Visualization
Illustrating the working principles of srsRAN PRACH detector
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from matplotlib.gridspec import GridSpec
import matplotlib.patches as mpatches

# Set default font
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

def generate_zc_sequence(u, N_zc, q=0):
    """生成 Zadoff-Chu 序列"""
    n = np.arange(N_zc)
    return np.exp(-1j * np.pi * u * n * (n + 1 + 2*q) / N_zc)

def apply_cyclic_shift(seq, shift):
    """應用循環移位"""
    return np.roll(seq, -shift)

def plot_1_zc_sequence_properties():
    """Figure 1: ZC Sequence Properties"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Figure 1: Zadoff-Chu (ZC) Sequence Properties', fontsize=16, fontweight='bold')
    
    N_zc = 139  # Short preamble sequence length
    u = 1  # Root sequence index
    
    # Generate ZC sequence
    zc = generate_zc_sequence(u, N_zc)
    
    # (a) Real and imaginary parts of ZC sequence
    ax = axes[0, 0]
    ax.plot(np.real(zc), label='Real Part', linewidth=1.5)
    ax.plot(np.imag(zc), label='Imaginary Part', linewidth=1.5, alpha=0.8)
    ax.set_xlabel('Sample Index n')
    ax.set_ylabel('Amplitude')
    ax.set_title('(a) Real and Imaginary Parts of ZC Sequence')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0, N_zc])
    
    # (b) ZC sequence magnitude (constant)
    ax = axes[0, 1]
    ax.plot(np.abs(zc), 'g-', linewidth=2)
    ax.set_xlabel('Sample Index n')
    ax.set_ylabel('Magnitude |x[n]|')
    ax.set_title('(b) ZC Sequence Magnitude (Constant Amplitude Property)')
    ax.set_ylim([0, 1.5])
    ax.axhline(y=1.0, color='r', linestyle='--', label='Amplitude = 1')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0, N_zc])
    
    # (c) Autocorrelation property
    ax = axes[1, 0]
    autocorr = np.abs(np.correlate(zc, zc, mode='full'))
    autocorr = autocorr / np.max(autocorr)
    lags = np.arange(-N_zc+1, N_zc)
    ax.plot(lags, autocorr, 'b-', linewidth=1.5)
    ax.set_xlabel('Delay (samples)')
    ax.set_ylabel('Normalized Correlation')
    ax.set_title('(c) ZC Sequence Autocorrelation (Ideal Impulse Property)')
    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    ax.grid(True, alpha=0.3)
    
    # (d) Cross-correlation with different cyclic shifts
    ax = axes[1, 1]
    shifts = [0, 10, 20, 30]
    colors = ['blue', 'red', 'green', 'orange']
    
    for shift, color in zip(shifts, colors):
        zc_shifted = apply_cyclic_shift(zc, shift)
        # Correlation with original sequence
        corr = np.abs(np.fft.ifft(np.fft.fft(zc) * np.conj(np.fft.fft(zc_shifted))))
        corr = corr / np.max(corr)
        ax.plot(corr, color=color, label=f'Cyclic Shift = {shift}', linewidth=1.5)
    
    ax.set_xlabel('Delay (samples)')
    ax.set_ylabel('Normalized Correlation')
    ax.set_title('(d) Correlation Output with Different Cyclic Shifts')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0, N_zc])
    
    plt.tight_layout()
    plt.savefig('fig1_zc_sequence_properties.png', dpi=150, bbox_inches='tight')
    plt.show()

def plot_2_detection_principle():
    """Figure 2: PRACH Detection Principle"""
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    fig.suptitle('Figure 2: PRACH Detection Principle', fontsize=16, fontweight='bold')
    
    N_zc = 139
    dft_size = 256
    u = 1
    
    # Simulate received signal (one UE sends preamble at delay=20)
    delay = 20
    snr_db = 10
    
    # Generate transmitted ZC sequence (with cyclic shift)
    zc_tx = generate_zc_sequence(u, N_zc)
    zc_tx_shifted = apply_cyclic_shift(zc_tx, delay)
    
    # Add noise
    noise_power = 10 ** (-snr_db / 10)
    noise = np.sqrt(noise_power / 2) * (np.random.randn(N_zc) + 1j * np.random.randn(N_zc))
    rx_signal = zc_tx_shifted + noise
    
    # Local root sequence
    root = generate_zc_sequence(u, N_zc)
    
    # (a) Received signal (frequency domain)
    ax = axes[0, 0]
    ax.plot(np.real(rx_signal), label='Real', alpha=0.8)
    ax.plot(np.imag(rx_signal), label='Imag', alpha=0.8)
    ax.set_xlabel('Subcarrier Index')
    ax.set_ylabel('Amplitude')
    ax.set_title('(a) Received Signal Y[k] (Frequency Domain)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # (b) Local root sequence
    ax = axes[0, 1]
    ax.plot(np.real(root), label='Real', alpha=0.8)
    ax.plot(np.imag(root), label='Imag', alpha=0.8)
    ax.set_xlabel('Subcarrier Index')
    ax.set_ylabel('Amplitude')
    ax.set_title('(b) Local Root Sequence X[k]')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # (c) Frequency domain multiplication Y[k] × X*[k]
    ax = axes[0, 2]
    product = rx_signal * np.conj(root)
    ax.plot(np.real(product), label='Real', alpha=0.8)
    ax.plot(np.imag(product), label='Imag', alpha=0.8)
    ax.set_xlabel('Subcarrier Index')
    ax.set_ylabel('Amplitude')
    ax.set_title('(c) Frequency Domain Product Y[k] × X*[k]')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # (d) IDFT output (time domain correlation)
    ax = axes[1, 0]
    # Zero padding to dft_size
    product_padded = np.zeros(dft_size, dtype=complex)
    product_padded[:N_zc] = product
    time_domain = np.fft.ifft(product_padded) * dft_size
    
    ax.plot(np.abs(time_domain), 'b-', linewidth=1.5)
    ax.axvline(x=delay, color='r', linestyle='--', label=f'True Delay = {delay}')
    ax.set_xlabel('Delay Samples')
    ax.set_ylabel('|Correlation|')
    ax.set_title('(d) IDFT Output (Time Domain Correlation)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0, 100])
    
    # (e) Power calculation |correlation|²
    ax = axes[1, 1]
    power = np.abs(time_domain) ** 2
    power_normalized = power / np.max(power)
    
    ax.plot(power_normalized, 'g-', linewidth=1.5)
    ax.axvline(x=delay, color='r', linestyle='--', label=f'Peak Position = {delay}')
    ax.axhline(y=0.3, color='orange', linestyle='--', label='Threshold')
    ax.fill_between(range(len(power_normalized)), power_normalized, 
                    where=power_normalized > 0.3, alpha=0.3, color='green')
    ax.set_xlabel('Delay Samples')
    ax.set_ylabel('Normalized Power')
    ax.set_title('(e) Power |correlation|² vs Threshold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0, 100])
    
    # (f) Detection result
    ax = axes[1, 2]
    ax.text(0.5, 0.7, 'Detection Result', fontsize=16, fontweight='bold',
            ha='center', transform=ax.transAxes)
    ax.text(0.5, 0.5, f'Peak > Threshold ✓', fontsize=14, color='green',
            ha='center', transform=ax.transAxes)
    ax.text(0.5, 0.35, f'Delay = {delay} samples', fontsize=12,
            ha='center', transform=ax.transAxes)
    ax.text(0.5, 0.2, f'Time Advance = {delay * 1e6 / 2.56e6:.2f} us', fontsize=12,
            ha='center', transform=ax.transAxes)
    ax.axis('off')
    ax.set_title('(f) Detection Output')
    
    plt.tight_layout()
    plt.savefig('fig2_detection_principle.png', dpi=150, bbox_inches='tight')
    plt.show()

def plot_3_window_structure():
    """Figure 3: Detection Window Structure"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Figure 3: PRACH Detection Window Structure', fontsize=16, fontweight='bold')
    
    # Parameter settings
    dft_size = 2048
    L_ra = 839
    N_cs = 13
    nof_shifts = min(64, L_ra // N_cs)  # 64
    win_width = (N_cs * dft_size) // L_ra
    
    # (a) Time domain correlation output and window division
    ax = axes[0, 0]
    
    # Simulate multiple UE peaks
    time_domain = np.random.randn(dft_size) * 0.1
    
    # Add several peaks (simulate different UEs)
    ue_delays = [10, 150, 280]  # Delays in different windows
    for d in ue_delays:
        if d < dft_size:
            time_domain[d] = 2.0 + np.random.randn() * 0.1
    
    ax.plot(time_domain, 'b-', linewidth=0.5, alpha=0.7)
    
    # Mark windows
    colors = ['red', 'green', 'blue', 'orange', 'purple']
    for i in range(5):
        window_start = (dft_size - (N_cs * i * dft_size) // L_ra) % dft_size
        if window_start + win_width <= dft_size:
            rect = Rectangle((window_start, -0.5), win_width, 3, 
                            linewidth=2, edgecolor=colors[i % len(colors)], 
                            facecolor=colors[i % len(colors)], alpha=0.2)
            ax.add_patch(rect)
            ax.text(window_start + win_width/2, 2.8, f'Win{i}', 
                   ha='center', fontsize=9, color=colors[i % len(colors)])
    
    ax.set_xlabel('Sample Index')
    ax.set_ylabel('Correlation Power')
    ax.set_title(f'(a) Time Domain Correlation and Window Division (first 5 windows)\n'
                f'N_cs={N_cs}, win_width={win_width}, nof_shifts={nof_shifts}')
    ax.set_xlim([0, 400])
    ax.set_ylim([-0.5, 3.5])
    ax.grid(True, alpha=0.3)
    
    # (b) Single window structure
    ax = axes[0, 1]
    win_margin = 10
    
    # Create diagram
    ax.axhline(y=0.5, color='black', linewidth=2)
    
    # Left margin
    rect1 = FancyBboxPatch((0, 0.3), win_margin, 0.4, 
                           boxstyle="round,pad=0.02", 
                           facecolor='lightblue', edgecolor='blue', linewidth=2)
    ax.add_patch(rect1)
    ax.text(win_margin/2, 0.5, 'Left\nMargin\n(Noise)', ha='center', va='center', fontsize=10)
    
    # Detection window
    rect2 = FancyBboxPatch((win_margin, 0.3), win_width, 0.4,
                           boxstyle="round,pad=0.02",
                           facecolor='lightgreen', edgecolor='green', linewidth=2)
    ax.add_patch(rect2)
    ax.text(win_margin + win_width/2, 0.5, 'Detection\nWindow\n(Signal+Noise)', 
           ha='center', va='center', fontsize=9)
    
    # Right margin
    rect3 = FancyBboxPatch((win_margin + win_width, 0.3), win_margin, 0.4,
                           boxstyle="round,pad=0.02",
                           facecolor='lightblue', edgecolor='blue', linewidth=2)
    ax.add_patch(rect3)
    ax.text(win_margin + win_width + win_margin/2, 0.5, 'Right\nMargin\n(Noise)', 
           ha='center', va='center', fontsize=10)
    
    # Annotations
    ax.annotate('', xy=(0, 0.15), xytext=(win_margin, 0.15),
               arrowprops=dict(arrowstyle='<->', color='blue'))
    ax.text(win_margin/2, 0.05, 'win_margin', ha='center', fontsize=9, color='blue')
    
    ax.annotate('', xy=(win_margin, 0.15), xytext=(win_margin + win_width, 0.15),
               arrowprops=dict(arrowstyle='<->', color='green'))
    ax.text(win_margin + win_width/2, 0.05, 'win_width', ha='center', fontsize=9, color='green')
    
    ax.set_xlim([-5, win_margin * 2 + win_width + 5])
    ax.set_ylim([0, 0.8])
    ax.set_title('(b) Single Window Structure')
    ax.axis('off')
    
    # (c) Cyclic shift and window mapping tablet and window mapping table
    ax = axes[1, 0]
    
    # Draw mapping table
    data = [
        ['i_window', 'preamble_index', 'window_start'],
        ['0', '0', f'{dft_size}→0'],
        ['1', '1', f'{dft_size - (N_cs * dft_size) // L_ra}'],
        ['2', '2', f'{dft_size - (2 * N_cs * dft_size) // L_ra}'],
        ['...', '...', '...'],
        [f'{nof_shifts-1}', f'{nof_shifts-1}', f'≈{(N_cs * dft_size) // L_ra}'],
    ]
    
    table = ax.table(cellText=data, loc='center', cellLoc='center',
                    colWidths=[0.25, 0.35, 0.35])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1.2, 1.8)
    
    # Set header style
    for i in range(3):
        table[(0, i)].set_facecolor('#4472C4')
        table[(0, i)].set_text_props(color='white', fontweight='bold')
    
    ax.set_title('(c) Cyclic Shift and Window Index Mapping')
    ax.axis('off')
    
    # (d) Window and preamble index relationshippreamble index relationship
    ax = axes[1, 1]
    
    # Draw matrix diagram
    nof_sequences = 4
    nof_shifts_display = 16
    
    matrix = np.arange(64).reshape(nof_sequences, nof_shifts_display)
    
    im = ax.imshow(matrix, cmap='viridis', aspect='auto')
    
    # Annotations
    ax.set_xlabel('i_window (Cyclic Shift Index)')
    ax.set_ylabel('i_sequence (Root Sequence Index)')
    ax.set_title('(d) Preamble Index = i_sequence × nof_shifts + i_window')
    
    # Add numeric annotations
    for i in range(nof_sequences):
        for j in range(nof_shifts_display):
            if j < 4 or j > 12:  # Only annotate part
                ax.text(j, i, str(matrix[i, j]), ha='center', va='center', 
                       color='white', fontsize=8)
            elif j == 8:
                ax.text(j, i, '...', ha='center', va='center', 
                       color='white', fontsize=10)
    
    plt.colorbar(im, ax=ax, label='Preamble Index')
    
    plt.tight_layout()
    plt.savefig('fig3_window_structure.png', dpi=150, bbox_inches='tight')
    plt.show()

def plot_4_multi_ue_detection():
    """Figure 4: Multi-UE Detection Scenarios"""
    fig = plt.figure(figsize=(16, 12))
    gs = GridSpec(3, 2, figure=fig, height_ratios=[1, 1, 1])
    fig.suptitle('Figure 4: Multi-UE Detection Scenarios', fontsize=16, fontweight='bold')
    
    # Parameters
    win_width = 50
    threshold = 1.5
    nof_windows = 8
    
    # Scenario 1: Different UEs use different preambles (normal case)
    ax1 = fig.add_subplot(gs[0, :])
    
    x = np.arange(nof_windows * win_width)
    y = np.random.rand(len(x)) * 0.5  # Noise floor
    
    # Add three UE peaks in different windows
    ue_info = [
        {'window': 1, 'delay': 10, 'peak': 3.2, 'color': 'red', 'name': 'UE1'},
        {'window': 3, 'delay': 25, 'peak': 2.8, 'color': 'blue', 'name': 'UE2'},
        {'window': 6, 'delay': 5, 'peak': 2.5, 'color': 'green', 'name': 'UE3'},
    ]
    
    for ue in ue_info:
        idx = ue['window'] * win_width + ue['delay']
        y[idx] = ue['peak']
    
    ax1.plot(x, y, 'k-', linewidth=0.5, alpha=0.5)
    ax1.axhline(y=threshold, color='orange', linestyle='--', linewidth=2, label=f'Threshold = {threshold}')
    
    # Mark windows and peaks
    for i in range(nof_windows):
        ax1.axvline(x=i * win_width, color='gray', linestyle=':', alpha=0.5)
        ax1.text(i * win_width + win_width/2, -0.3, f'Win{i}\n(Preamble{i})', 
                ha='center', fontsize=9)
    
    for ue in ue_info:
        idx = ue['window'] * win_width + ue['delay']
        ax1.scatter([idx], [ue['peak']], color=ue['color'], s=100, zorder=5)
        ax1.annotate(f"{ue['name']}\npeak={ue['peak']}", 
                    xy=(idx, ue['peak']), xytext=(idx, ue['peak'] + 0.5),
                    fontsize=10, ha='center', color=ue['color'],
                    arrowprops=dict(arrowstyle='->', color=ue['color']))
    
    ax1.set_xlim([0, nof_windows * win_width])
    ax1.set_ylim([-0.5, 4.5])
    ax1.set_xlabel('Sample Index')
    ax1.set_ylabel('Detection Metric')
    ax1.set_title('Scenario 1: Different UEs use Different Preambles \u2192 All Detected Successfully \u2713')
    ax1.legend(loc='upper right')
    ax1.grid(True, alpha=0.3)
    
    # Scenario 2: Two UEs use same preamble (collision - large power difference)reamble (collision - large power difference)
    ax2 = fig.add_subplot(gs[1, 0])
    
    x = np.arange(win_width)
    y = np.random.rand(len(x)) * 0.3
    
    # UE1 stronger, UE2 weaker
    y[10] = 3.0  # UE1
    y[35] = 1.8  # UE2
    
    ax2.plot(x, y, 'k-', linewidth=1)
    ax2.axhline(y=threshold, color='orange', linestyle='--', linewidth=2)
    
    ax2.scatter([10], [3.0], color='red', s=100, zorder=5, label='UE1 (Strong)')
    ax2.scatter([35], [1.8], color='blue', s=100, zorder=5, label='UE2 (Weak)')
    
    ax2.annotate('max_element\nOnly found this!', xy=(10, 3.0), xytext=(25, 3.5),
                fontsize=10, color='red',
                arrowprops=dict(arrowstyle='->', color='red'))
    
    ax2.set_xlabel('delay (samples)')
    ax2.set_ylabel('Detection Metric')
    ax2.set_title('Scenario 2a: Collision - UE1 Stronger\n\u2192 Only UE1 Detected, UE2 Missed \u26a0\ufe0f')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim([0, win_width])
    ax2.set_ylim([0, 4.5])
    
    # Scenario 3: Two UEs use same preamble (collision - destructive interference)
    ax3 = fig.add_subplot(gs[1, 1])
    
    x = np.arange(win_width)
    y = np.random.rand(len(x)) * 0.3
    
    # 兩個峰值都低於門檻
    y[15] = 1.2
    y[30] = 1.0
    
    ax3.plot(x, y, 'k-', linewidth=1)
    ax3.axhline(y=threshold, color='orange', linestyle='--', linewidth=2, label=f'Threshold = {threshold}')
    
    ax3.scatter([15], [1.2], color='red', s=100, zorder=5, label='UE1')
    ax3.scatter([30], [1.0], color='blue', s=100, zorder=5, label='UE2')
    
    ax3.fill_between(x, y, threshold, where=y < threshold, alpha=0.3, color='red')
    ax3.text(25, 2.0, 'Both < threshold\nBoth UEs Detection Failed!', 
            fontsize=11, ha='center', color='red', fontweight='bold')
    
    ax3.set_xlabel('delay (samples)')
    ax3.set_ylabel('Detection Metric')
    ax3.set_title('Scenario 2b: Collision - Destructive Interference\n\u2192 Both UEs Detection Failed \u2717')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    ax3.set_xlim([0, win_width])
    ax3.set_ylim([0, 4.5])
    
    # Detection result tableion result table
    ax4 = fig.add_subplot(gs[2, :])
    ax4.axis('off')
    
    # Create result table
    results_text = """
    \u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510
    \u2502                         PRACH Detection Results (result.preambles)                  \u2502
    \u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524
    \u2502  Scenario 1: Different Preambles                                                    \u2502
    \u2502  result.preambles = [                                                                \u2502
    \u2502    {preamble_index: 1, time_advance: 3.9 us, detection_metric: 2.13},  // UE1        \u2502
    \u2502    {preamble_index: 3, time_advance: 9.8 us, detection_metric: 1.87},  // UE2        \u2502
    \u2502    {preamble_index: 6, time_advance: 2.0 us, detection_metric: 1.67}   // UE3        \u2502
    \u2502  ]                                                                                   \u2502
    \u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524
    \u2502  Scenario 2a: Collision (UE1 Stronger)                                              \u2502
    \u2502  result.preambles = [                                                                \u2502
    \u2502    {preamble_index: 5, time_advance: 3.9 us, detection_metric: 2.0}   // Only UE1    \u2502
    \u2502  ]                                                                                   \u2502
    \u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524
    \u2502  Scenario 2b: Collision (Destructive Interference)                                  \u2502
    \u2502  result.preambles = []  // Empty! Both detections failed                             \u2502
    \u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518
    """
    
    ax4.text(0.5, 0.5, results_text, transform=ax4.transAxes, fontsize=10,
            verticalalignment='center', horizontalalignment='center',
            fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.savefig('fig4_multi_ue_detection.png', dpi=150, bbox_inches='tight')
    plt.show()

def plot_5_detection_flowchart():
    """Figure 5: Detection Algorithm Flowchart"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 16))
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 16])
    ax.axis('off')
    ax.set_title('Figure 5: PRACH Detection Algorithm Flowchart', fontsize=16, fontweight='bold', pad=20)
    
    def draw_box(x, y, w, h, text, color='lightblue', fontsize=9):
        rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05",
                              facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', 
               fontsize=fontsize, wrap=True)
    
    def draw_diamond(x, y, w, h, text, color='lightyellow'):
        diamond = plt.Polygon([(x + w/2, y + h), (x + w, y + h/2), 
                               (x + w/2, y), (x, y + h/2)],
                             facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(diamond)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=9)
    
    def draw_arrow(x1, y1, x2, y2, text=''):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
        if text:
            ax.text((x1 + x2)/2 + 0.2, (y1 + y2)/2, text, fontsize=8)
    
    # Start
    draw_box(4, 15, 2, 0.6, 'Start Detection', 'lightgreen')
    draw_arrow(5, 15, 5, 14.6)
    
    # Initialize
    draw_box(3, 13.8, 4, 0.7, 'Initialize Parameters\n(threshold, win_width, nof_shifts)', 'lightblue')
    draw_arrow(5, 13.8, 5, 13.4)
    
    # Calculate RSSI
    draw_box(3, 12.6, 4, 0.7, 'Calculate RSSI\n(Received Signal Strength)', 'lightblue')
    draw_arrow(5, 12.6, 5, 12.2)
    
    # Root sequence loop
    draw_box(2.5, 11.4, 5, 0.7, 'for i_sequence = 0 to nof_sequences-1', 'lightyellow')
    draw_arrow(5, 11.4, 5, 11)
    
    # Generate root sequence
    draw_box(3, 10.2, 4, 0.7, 'Generate Root Sequence\nroot = generator->generate()', 'lightblue')
    draw_arrow(5, 10.2, 5, 9.8)
    
    # Antenna port loop
    draw_box(2.5, 9, 5, 0.7, 'for i_port = 0 to nof_rx_ports-1', 'lightyellow')
    draw_arrow(5, 9, 5, 8.6)
    
    # Symbol loop
    draw_box(2.5, 7.8, 5, 0.7, 'for i_symbol = 0 to nof_symbols-1', 'lightyellow')
    draw_arrow(5, 7.8, 5, 7.4)
    
    # Correlation operation
    draw_box(2.5, 6.4, 5, 0.9, 'Correlation:\n1. Y × X* (Freq domain mult)\n2. IDFT (To time domain)\n3. |·|² (Power)', 'lightcyan')
    draw_arrow(5, 6.4, 5, 6)
    
    # Window loop
    draw_box(2.5, 5.2, 5, 0.7, 'for i_window = 0 to nof_shifts-1', 'lightyellow')
    draw_arrow(5, 5.2, 5, 4.8)
    
    # Accumulate metrics
    draw_box(2.5, 4, 5, 0.7, 'Accumulate metric_global_num[i_window]\nAccumulate metric_global_den[i_window]', 'lightblue')
    
    # Back to window loop
    draw_arrow(7.5, 4.35, 8, 4.35)
    ax.annotate('', xy=(8, 5.55), xytext=(8, 4.35),
               arrowprops=dict(arrowstyle='->', color='gray', lw=1))
    ax.annotate('', xy=(7.5, 5.55), xytext=(8, 5.55),
               arrowprops=dict(arrowstyle='->', color='gray', lw=1))
    
    # After processing
    draw_arrow(5, 4, 5, 3.6)
    
    # Calculate final metric
    draw_box(2.5, 2.8, 5, 0.7, 'Calculate metric = num / |den|\nFind peak: max_element(metric)', 'lightblue')
    draw_arrow(5, 2.8, 5, 2.4)
    
    # Decision
    draw_diamond(3.5, 1.4, 3, 0.9, 'peak > threshold?', 'lightyellow')
    
    # Yes branch
    draw_arrow(6.5, 1.85, 8, 1.85)
    ax.text(7, 2, 'Yes', fontsize=9)
    draw_box(7.5, 1.2, 2, 1.2, 'Record Result:\npreamble_index\ntime_advance\ndetection_metric', 'lightgreen', fontsize=8)
    
    # No branch
    draw_arrow(5, 1.4, 5, 0.8)
    ax.text(5.2, 1.1, 'No', fontsize=9)
    draw_box(4, 0.2, 2, 0.5, 'Continue Next', 'lightgray')
    
    # Return result
    draw_arrow(5, 0.2, 5, -0.2)
    draw_box(3.5, -0.8, 3, 0.5, 'return result', 'lightgreen')
    
    plt.tight_layout()
    plt.savefig('fig5_detection_flowchart.png', dpi=150, bbox_inches='tight')
    plt.show()

def plot_6_threshold_decision():
    """Figure 6: Threshold Decision Explanation"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Figure 6: Threshold Decision and Detection Metric', fontsize=16, fontweight='bold')
    
    # (a) Threshold decision illustration
    ax = axes[0]
    
    x = np.linspace(0, 10, 1000)
    # Assumed distributions
    noise_dist = 2 * np.exp(-((x - 1) ** 2) / 0.5)  # Noise distribution
    signal_dist = 1.5 * np.exp(-((x - 4) ** 2) / 1.0)  # Signal distribution
    
    ax.fill_between(x, noise_dist, alpha=0.5, color='blue', label='H0: Noise Only')
    ax.fill_between(x, signal_dist, alpha=0.5, color='green', label='H1: Signal+Noise')
    
    threshold = 2.5
    ax.axvline(x=threshold, color='red', linestyle='--', linewidth=2, label=f'Threshold = {threshold}')
    
    # Mark regions
    ax.fill_between(x[x > threshold], noise_dist[x > threshold], alpha=0.3, color='red')
    ax.text(3.5, 0.5, 'False\nAlarm', fontsize=10, color='red', ha='center')
    
    ax.fill_between(x[x < threshold], signal_dist[x < threshold], alpha=0.3, color='orange')
    ax.text(1.5, 0.3, 'Missed\nDetection', fontsize=10, color='orange', ha='center')
    
    ax.set_xlabel('Detection Metric Value')
    ax.set_ylabel('Probability Density')
    ax.set_title('(a) Statistical Decision Theory: Threshold Decision')
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0, 8])
    ax.set_ylim([0, 2.5])
    
    # (b) Meaning of detection_metric
    ax = axes[1]
    
    metrics = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]
    colors = ['red', 'orange', 'yellow', 'lightgreen', 'green', 'darkgreen']
    labels = ['Very Unreliable', 'Barely Pass', 'Acceptable', 'Good', 'Very Good', 'Excellent']
    
    bars = ax.bar(range(len(metrics)), metrics, color=colors, edgecolor='black', linewidth=2)
    ax.axhline(y=1.0, color='red', linestyle='--', linewidth=2, label='Threshold')
    
    ax.set_xticks(range(len(metrics)))
    ax.set_xticklabels([f'{m}' for m in metrics])
    ax.set_xlabel('detection_metric = peak / threshold')
    ax.set_ylabel('Value')
    ax.set_title('(b) Meaning of detection_metric')
    
    # Add labels
    for i, (bar, label) in enumerate(zip(bars, labels)):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
               label, ha='center', va='bottom', fontsize=9, rotation=45)
    
    ax.set_ylim([0, 6.5])
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('fig6_threshold_decision.png', dpi=150, bbox_inches='tight')
    plt.show()

def plot_all():
    """Generate all figures"""
    print("Generating Figure 1: ZC Sequence Properties...")
    plot_1_zc_sequence_properties()
    
    print("Generating Figure 2: PRACH Detection Principle...")
    plot_2_detection_principle()
    
    print("Generating Figure 3: Detection Window Structure...")
    plot_3_window_structure()
    
    print("Generating Figure 4: Multi-UE Detection Scenarios...")
    plot_4_multi_ue_detection()
    
    print("Generating Figure 5: Detection Algorithm Flowchart...")
    plot_5_detection_flowchart()
    
    print("Generating Figure 6: Threshold Decision Explanation...")
    plot_6_threshold_decision()
    
    print("\nAll figures generated successfully!")
    print("Generated files:")
    print("  - fig1_zc_sequence_properties.png")
    print("  - fig2_detection_principle.png")
    print("  - fig3_window_structure.png")
    print("  - fig4_multi_ue_detection.png")
    print("  - fig5_detection_flowchart.png")
    print("  - fig6_threshold_decision.png")

if __name__ == "__main__":
    plot_all()
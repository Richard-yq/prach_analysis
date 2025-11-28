"""
PRACH Detection Mechanism Visualization
用於說明 srsRAN PRACH 偵測器的工作原理
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from matplotlib.gridspec import GridSpec
import matplotlib.patches as mpatches

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def generate_zc_sequence(u, N_zc, q=0):
    """生成 Zadoff-Chu 序列"""
    n = np.arange(N_zc)
    return np.exp(-1j * np.pi * u * n * (n + 1 + 2*q) / N_zc)

def apply_cyclic_shift(seq, shift):
    """應用循環移位"""
    return np.roll(seq, -shift)

def plot_1_zc_sequence_properties():
    """圖1: ZC 序列的特性"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('圖1: Zadoff-Chu (ZC) 序列特性', fontsize=16, fontweight='bold')
    
    N_zc = 139  # 短前導碼序列長度
    u = 1  # 根序列索引
    
    # 生成 ZC 序列
    zc = generate_zc_sequence(u, N_zc)
    
    # (a) ZC 序列的實部和虛部
    ax = axes[0, 0]
    ax.plot(np.real(zc), label='實部 (Real)', linewidth=1.5)
    ax.plot(np.imag(zc), label='虛部 (Imag)', linewidth=1.5, alpha=0.8)
    ax.set_xlabel('樣本索引 n')
    ax.set_ylabel('振幅')
    ax.set_title('(a) ZC 序列的實部與虛部')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0, N_zc])
    
    # (b) ZC 序列的振幅（恆定）
    ax = axes[0, 1]
    ax.plot(np.abs(zc), 'g-', linewidth=2)
    ax.set_xlabel('樣本索引 n')
    ax.set_ylabel('振幅 |x[n]|')
    ax.set_title('(b) ZC 序列的振幅（恆定振幅特性）')
    ax.set_ylim([0, 1.5])
    ax.axhline(y=1.0, color='r', linestyle='--', label='振幅 = 1')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0, N_zc])
    
    # (c) 自相關特性
    ax = axes[1, 0]
    autocorr = np.abs(np.correlate(zc, zc, mode='full'))
    autocorr = autocorr / np.max(autocorr)
    lags = np.arange(-N_zc+1, N_zc)
    ax.plot(lags, autocorr, 'b-', linewidth=1.5)
    ax.set_xlabel('延遲 (樣本)')
    ax.set_ylabel('正規化相關值')
    ax.set_title('(c) ZC 序列自相關（理想脈衝特性）')
    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    ax.grid(True, alpha=0.3)
    
    # (d) 不同循環移位的互相關
    ax = axes[1, 1]
    shifts = [0, 10, 20, 30]
    colors = ['blue', 'red', 'green', 'orange']
    
    for shift, color in zip(shifts, colors):
        zc_shifted = apply_cyclic_shift(zc, shift)
        # 與原始序列的相關
        corr = np.abs(np.fft.ifft(np.fft.fft(zc) * np.conj(np.fft.fft(zc_shifted))))
        corr = corr / np.max(corr)
        ax.plot(corr, color=color, label=f'循環移位 = {shift}', linewidth=1.5)
    
    ax.set_xlabel('延遲 (樣本)')
    ax.set_ylabel('正規化相關值')
    ax.set_title('(d) 不同循環移位的相關輸出')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0, N_zc])
    
    plt.tight_layout()
    plt.savefig('fig1_zc_sequence_properties.png', dpi=150, bbox_inches='tight')
    plt.show()

def plot_2_detection_principle():
    """圖2: PRACH 偵測原理流程圖"""
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    fig.suptitle('圖2: PRACH 偵測原理', fontsize=16, fontweight='bold')
    
    N_zc = 139
    dft_size = 256
    u = 1
    
    # 模擬接收訊號 (有一個 UE 在 delay=20 發送 preamble)
    delay = 20
    snr_db = 10
    
    # 生成發送的 ZC 序列（帶循環移位）
    zc_tx = generate_zc_sequence(u, N_zc)
    zc_tx_shifted = apply_cyclic_shift(zc_tx, delay)
    
    # 加入雜訊
    noise_power = 10 ** (-snr_db / 10)
    noise = np.sqrt(noise_power / 2) * (np.random.randn(N_zc) + 1j * np.random.randn(N_zc))
    rx_signal = zc_tx_shifted + noise
    
    # 本地根序列
    root = generate_zc_sequence(u, N_zc)
    
    # (a) 接收訊號（頻域）
    ax = axes[0, 0]
    ax.plot(np.real(rx_signal), label='實部', alpha=0.8)
    ax.plot(np.imag(rx_signal), label='虛部', alpha=0.8)
    ax.set_xlabel('子載波索引')
    ax.set_ylabel('振幅')
    ax.set_title('(a) 接收訊號 Y[k] (頻域)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # (b) 本地根序列
    ax = axes[0, 1]
    ax.plot(np.real(root), label='實部', alpha=0.8)
    ax.plot(np.imag(root), label='虛部', alpha=0.8)
    ax.set_xlabel('子載波索引')
    ax.set_ylabel('振幅')
    ax.set_title('(b) 本地根序列 X[k]')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # (c) 頻域相乘 Y[k] × X*[k]
    ax = axes[0, 2]
    product = rx_signal * np.conj(root)
    ax.plot(np.real(product), label='實部', alpha=0.8)
    ax.plot(np.imag(product), label='虛部', alpha=0.8)
    ax.set_xlabel('子載波索引')
    ax.set_ylabel('振幅')
    ax.set_title('(c) 頻域相乘 Y[k] × X*[k]')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # (d) IDFT 輸出（時域相關）
    ax = axes[1, 0]
    # 補零到 dft_size
    product_padded = np.zeros(dft_size, dtype=complex)
    product_padded[:N_zc] = product
    time_domain = np.fft.ifft(product_padded) * dft_size
    
    ax.plot(np.abs(time_domain), 'b-', linewidth=1.5)
    ax.axvline(x=delay, color='r', linestyle='--', label=f'真實延遲 = {delay}')
    ax.set_xlabel('延遲樣本')
    ax.set_ylabel('|相關值|')
    ax.set_title('(d) IDFT 輸出（時域相關）')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0, 100])
    
    # (e) 功率計算 |correlation|²
    ax = axes[1, 1]
    power = np.abs(time_domain) ** 2
    power_normalized = power / np.max(power)
    
    ax.plot(power_normalized, 'g-', linewidth=1.5)
    ax.axvline(x=delay, color='r', linestyle='--', label=f'峰值位置 = {delay}')
    ax.axhline(y=0.3, color='orange', linestyle='--', label='門檻值 (threshold)')
    ax.fill_between(range(len(power_normalized)), power_normalized, 
                    where=power_normalized > 0.3, alpha=0.3, color='green')
    ax.set_xlabel('延遲樣本')
    ax.set_ylabel('正規化功率')
    ax.set_title('(e) 功率 |correlation|² 與門檻比較')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0, 100])
    
    # (f) 偵測結果
    ax = axes[1, 2]
    ax.text(0.5, 0.7, '偵測結果', fontsize=16, fontweight='bold',
            ha='center', transform=ax.transAxes)
    ax.text(0.5, 0.5, f'Peak > Threshold ✓', fontsize=14, color='green',
            ha='center', transform=ax.transAxes)
    ax.text(0.5, 0.35, f'Delay = {delay} 樣本', fontsize=12,
            ha='center', transform=ax.transAxes)
    ax.text(0.5, 0.2, f'Time Advance = {delay * 1e6 / 2.56e6:.2f} μs', fontsize=12,
            ha='center', transform=ax.transAxes)
    ax.axis('off')
    ax.set_title('(f) 偵測輸出')
    
    plt.tight_layout()
    plt.savefig('fig2_detection_principle.png', dpi=150, bbox_inches='tight')
    plt.show()

def plot_3_window_structure():
    """圖3: 偵測窗口結構"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('圖3: PRACH 偵測窗口結構', fontsize=16, fontweight='bold')
    
    # 參數設定
    dft_size = 2048
    L_ra = 839
    N_cs = 13
    nof_shifts = min(64, L_ra // N_cs)  # 64
    win_width = (N_cs * dft_size) // L_ra
    
    # (a) 時域相關輸出與窗口劃分
    ax = axes[0, 0]
    
    # 模擬多個 UE 的峰值
    time_domain = np.random.randn(dft_size) * 0.1
    
    # 添加幾個峰值（模擬不同 UE）
    ue_delays = [10, 150, 280]  # 不同窗口中的延遲
    for d in ue_delays:
        if d < dft_size:
            time_domain[d] = 2.0 + np.random.randn() * 0.1
    
    ax.plot(time_domain, 'b-', linewidth=0.5, alpha=0.7)
    
    # 標示窗口
    colors = ['red', 'green', 'blue', 'orange', 'purple']
    for i in range(5):
        window_start = (dft_size - (N_cs * i * dft_size) // L_ra) % dft_size
        if window_start + win_width <= dft_size:
            rect = Rectangle((window_start, -0.5), win_width, 3, 
                            linewidth=2, edgecolor=colors[i % len(colors)], 
                            facecolor=colors[i % len(colors)], alpha=0.2)
            ax.add_patch(rect)
            ax.text(window_start + win_width/2, 2.8, f'窗口{i}', 
                   ha='center', fontsize=9, color=colors[i % len(colors)])
    
    ax.set_xlabel('樣本索引')
    ax.set_ylabel('相關功率')
    ax.set_title(f'(a) 時域相關輸出與窗口劃分 (前5個窗口)\n'
                f'N_cs={N_cs}, win_width={win_width}, nof_shifts={nof_shifts}')
    ax.set_xlim([0, 400])
    ax.set_ylim([-0.5, 3.5])
    ax.grid(True, alpha=0.3)
    
    # (b) 單一窗口結構
    ax = axes[0, 1]
    win_margin = 10
    
    # 創建示意圖
    ax.axhline(y=0.5, color='black', linewidth=2)
    
    # 左邊界
    rect1 = FancyBboxPatch((0, 0.3), win_margin, 0.4, 
                           boxstyle="round,pad=0.02", 
                           facecolor='lightblue', edgecolor='blue', linewidth=2)
    ax.add_patch(rect1)
    ax.text(win_margin/2, 0.5, '左邊界\n(雜訊)', ha='center', va='center', fontsize=10)
    
    # 偵測窗口
    rect2 = FancyBboxPatch((win_margin, 0.3), win_width, 0.4,
                           boxstyle="round,pad=0.02",
                           facecolor='lightgreen', edgecolor='green', linewidth=2)
    ax.add_patch(rect2)
    ax.text(win_margin + win_width/2, 0.5, '偵測窗口\n(訊號+雜訊)', 
           ha='center', va='center', fontsize=10)
    
    # 右邊界
    rect3 = FancyBboxPatch((win_margin + win_width, 0.3), win_margin, 0.4,
                           boxstyle="round,pad=0.02",
                           facecolor='lightblue', edgecolor='blue', linewidth=2)
    ax.add_patch(rect3)
    ax.text(win_margin + win_width + win_margin/2, 0.5, '右邊界\n(雜訊)', 
           ha='center', va='center', fontsize=10)
    
    # 標註
    ax.annotate('', xy=(0, 0.15), xytext=(win_margin, 0.15),
               arrowprops=dict(arrowstyle='<->', color='blue'))
    ax.text(win_margin/2, 0.05, 'win_margin', ha='center', fontsize=9, color='blue')
    
    ax.annotate('', xy=(win_margin, 0.15), xytext=(win_margin + win_width, 0.15),
               arrowprops=dict(arrowstyle='<->', color='green'))
    ax.text(win_margin + win_width/2, 0.05, 'win_width', ha='center', fontsize=9, color='green')
    
    ax.set_xlim([-5, win_margin * 2 + win_width + 5])
    ax.set_ylim([0, 0.8])
    ax.set_title('(b) 單一窗口結構')
    ax.axis('off')
    
    # (c) 循環移位與窗口對應關係
    ax = axes[1, 0]
    
    # 繪製對應關係表
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
    
    # 設定表頭樣式
    for i in range(3):
        table[(0, i)].set_facecolor('#4472C4')
        table[(0, i)].set_text_props(color='white', fontweight='bold')
    
    ax.set_title('(c) 循環移位與窗口索引對應表')
    ax.axis('off')
    
    # (d) 窗口與前導碼索引關係圖
    ax = axes[1, 1]
    
    # 繪製矩陣示意圖
    nof_sequences = 4
    nof_shifts_display = 16
    
    matrix = np.arange(64).reshape(nof_sequences, nof_shifts_display)
    
    im = ax.imshow(matrix, cmap='viridis', aspect='auto')
    
    # 標註
    ax.set_xlabel('i_window (循環移位索引)')
    ax.set_ylabel('i_sequence (根序列索引)')
    ax.set_title('(d) 前導碼索引 = i_sequence × nof_shifts + i_window')
    
    # 添加數值標註
    for i in range(nof_sequences):
        for j in range(nof_shifts_display):
            if j < 4 or j > 12:  # 只標註部分
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
    """圖4: 多 UE 偵測情況"""
    fig = plt.figure(figsize=(16, 12))
    gs = GridSpec(3, 2, figure=fig, height_ratios=[1, 1, 1])
    fig.suptitle('圖4: 多 UE 偵測情況', fontsize=16, fontweight='bold')
    
    # 參數
    win_width = 50
    threshold = 1.5
    nof_windows = 8
    
    # 情況1: 不同 UE 使用不同前導碼（正常情況）
    ax1 = fig.add_subplot(gs[0, :])
    
    x = np.arange(nof_windows * win_width)
    y = np.random.rand(len(x)) * 0.5  # 雜訊底限
    
    # 添加三個 UE 的峰值在不同窗口
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
    
    # 標示窗口和峰值
    for i in range(nof_windows):
        ax1.axvline(x=i * win_width, color='gray', linestyle=':', alpha=0.5)
        ax1.text(i * win_width + win_width/2, -0.3, f'窗口{i}\n(前導碼{i})', 
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
    ax1.set_xlabel('樣本索引')
    ax1.set_ylabel('偵測度量')
    ax1.set_title('情況1: 不同 UE 使用不同前導碼 → 全部偵測成功 ✓')
    ax1.legend(loc='upper right')
    ax1.grid(True, alpha=0.3)
    
    # 情況2: 兩個 UE 使用相同前導碼（碰撞 - 功率差異大）
    ax2 = fig.add_subplot(gs[1, 0])
    
    x = np.arange(win_width)
    y = np.random.rand(len(x)) * 0.3
    
    # UE1 較強，UE2 較弱
    y[10] = 3.0  # UE1
    y[35] = 1.8  # UE2
    
    ax2.plot(x, y, 'k-', linewidth=1)
    ax2.axhline(y=threshold, color='orange', linestyle='--', linewidth=2)
    
    ax2.scatter([10], [3.0], color='red', s=100, zorder=5, label='UE1 (強)')
    ax2.scatter([35], [1.8], color='blue', s=100, zorder=5, label='UE2 (弱)')
    
    ax2.annotate('max_element\n只找到這個!', xy=(10, 3.0), xytext=(25, 3.5),
                fontsize=10, color='red',
                arrowprops=dict(arrowstyle='->', color='red'))
    
    ax2.set_xlabel('delay (延遲樣本)')
    ax2.set_ylabel('偵測度量')
    ax2.set_title('情況2a: 碰撞 - UE1 較強\n→ 只偵測到 UE1，UE2 遺失 ⚠️')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim([0, win_width])
    ax2.set_ylim([0, 4.5])
    
    # 情況3: 兩個 UE 使用相同前導碼（碰撞 - 破壞性干擾）
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
    ax3.text(25, 2.0, '兩者都 < threshold\n兩個 UE 都偵測失敗!', 
            fontsize=11, ha='center', color='red', fontweight='bold')
    
    ax3.set_xlabel('delay (延遲樣本)')
    ax3.set_ylabel('偵測度量')
    ax3.set_title('情況2b: 碰撞 - 破壞性干擾\n→ 兩個 UE 都偵測失敗 ✗')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    ax3.set_xlim([0, win_width])
    ax3.set_ylim([0, 4.5])
    
    # 偵測結果表格
    ax4 = fig.add_subplot(gs[2, :])
    ax4.axis('off')
    
    # 創建結果表格
    results_text = """
    ┌──────────────────────────────────────────────────────────────────────────────────────┐
    │                              PRACH 偵測結果 (result.preambles)                         │
    ├──────────────────────────────────────────────────────────────────────────────────────┤
    │  情況1: 不同前導碼                                                                    │
    │  result.preambles = [                                                                │
    │    {preamble_index: 1, time_advance: 3.9 μs, detection_metric: 2.13},  // UE1        │
    │    {preamble_index: 3, time_advance: 9.8 μs, detection_metric: 1.87},  // UE2        │
    │    {preamble_index: 6, time_advance: 2.0 μs, detection_metric: 1.67}   // UE3        │
    │  ]                                                                                   │
    ├──────────────────────────────────────────────────────────────────────────────────────┤
    │  情況2a: 碰撞 (UE1 較強)                                                              │
    │  result.preambles = [                                                                │
    │    {preamble_index: 5, time_advance: 3.9 μs, detection_metric: 2.0}   // 只有 UE1    │
    │  ]                                                                                   │
    ├──────────────────────────────────────────────────────────────────────────────────────┤
    │  情況2b: 碰撞 (破壞性干擾)                                                            │
    │  result.preambles = []  // 空！兩個都偵測失敗                                         │
    └──────────────────────────────────────────────────────────────────────────────────────┘
    """
    
    ax4.text(0.5, 0.5, results_text, transform=ax4.transAxes, fontsize=10,
            verticalalignment='center', horizontalalignment='center',
            fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.savefig('fig4_multi_ue_detection.png', dpi=150, bbox_inches='tight')
    plt.show()

def plot_5_detection_flowchart():
    """圖5: 偵測演算法流程圖"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 16))
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 16])
    ax.axis('off')
    ax.set_title('圖5: PRACH 偵測演算法流程圖', fontsize=16, fontweight='bold', pad=20)
    
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
    
    # 開始
    draw_box(4, 15, 2, 0.6, '開始偵測', 'lightgreen')
    draw_arrow(5, 15, 5, 14.6)
    
    # 初始化
    draw_box(3, 13.8, 4, 0.7, '初始化參數\n(threshold, win_width, nof_shifts)', 'lightblue')
    draw_arrow(5, 13.8, 5, 13.4)
    
    # 計算 RSSI
    draw_box(3, 12.6, 4, 0.7, '計算 RSSI\n(接收訊號強度)', 'lightblue')
    draw_arrow(5, 12.6, 5, 12.2)
    
    # 根序列迴圈
    draw_box(2.5, 11.4, 5, 0.7, 'for i_sequence = 0 to nof_sequences-1', 'lightyellow')
    draw_arrow(5, 11.4, 5, 11)
    
    # 生成根序列
    draw_box(3, 10.2, 4, 0.7, '生成根序列\nroot = generator->generate()', 'lightblue')
    draw_arrow(5, 10.2, 5, 9.8)
    
    # 天線埠迴圈
    draw_box(2.5, 9, 5, 0.7, 'for i_port = 0 to nof_rx_ports-1', 'lightyellow')
    draw_arrow(5, 9, 5, 8.6)
    
    # 符號迴圈
    draw_box(2.5, 7.8, 5, 0.7, 'for i_symbol = 0 to nof_symbols-1', 'lightyellow')
    draw_arrow(5, 7.8, 5, 7.4)
    
    # 相關運算
    draw_box(2.5, 6.4, 5, 0.9, '相關運算:\n1. Y × X* (頻域相乘)\n2. IDFT (轉換到時域)\n3. |·|² (計算功率)', 'lightcyan')
    draw_arrow(5, 6.4, 5, 6)
    
    # 窗口迴圈
    draw_box(2.5, 5.2, 5, 0.7, 'for i_window = 0 to nof_shifts-1', 'lightyellow')
    draw_arrow(5, 5.2, 5, 4.8)
    
    # 累加度量
    draw_box(2.5, 4, 5, 0.7, '累加 metric_global_num[i_window]\n累加 metric_global_den[i_window]', 'lightblue')
    
    # 回到窗口迴圈
    draw_arrow(7.5, 4.35, 8, 4.35)
    ax.annotate('', xy=(8, 5.55), xytext=(8, 4.35),
               arrowprops=dict(arrowstyle='->', color='gray', lw=1))
    ax.annotate('', xy=(7.5, 5.55), xytext=(8, 5.55),
               arrowprops=dict(arrowstyle='->', color='gray', lw=1))
    
    # 處理完成後
    draw_arrow(5, 4, 5, 3.6)
    
    # 計算最終度量
    draw_box(2.5, 2.8, 5, 0.7, '計算 metric = num / |den|\n找峰值: max_element(metric)', 'lightblue')
    draw_arrow(5, 2.8, 5, 2.4)
    
    # 判斷
    draw_diamond(3.5, 1.4, 3, 0.9, 'peak > threshold?', 'lightyellow')
    
    # Yes 分支
    draw_arrow(6.5, 1.85, 8, 1.85)
    ax.text(7, 2, 'Yes', fontsize=9)
    draw_box(7.5, 1.2, 2, 1.2, '記錄結果:\npreamble_index\ntime_advance\ndetection_metric', 'lightgreen', fontsize=8)
    
    # No 分支
    draw_arrow(5, 1.4, 5, 0.8)
    ax.text(5.2, 1.1, 'No', fontsize=9)
    draw_box(4, 0.2, 2, 0.5, '繼續下一個', 'lightgray')
    
    # 返回結果
    draw_arrow(5, 0.2, 5, -0.2)
    draw_box(3.5, -0.8, 3, 0.5, 'return result', 'lightgreen')
    
    plt.tight_layout()
    plt.savefig('fig5_detection_flowchart.png', dpi=150, bbox_inches='tight')
    plt.show()

def plot_6_threshold_decision():
    """圖6: 門檻判決說明"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('圖6: 門檻判決與偵測度量', fontsize=16, fontweight='bold')
    
    # (a) 門檻判決示意
    ax = axes[0]
    
    x = np.linspace(0, 10, 1000)
    # 假設分佈
    noise_dist = 2 * np.exp(-((x - 1) ** 2) / 0.5)  # 雜訊分佈
    signal_dist = 1.5 * np.exp(-((x - 4) ** 2) / 1.0)  # 訊號分佈
    
    ax.fill_between(x, noise_dist, alpha=0.5, color='blue', label='H0: 只有雜訊')
    ax.fill_between(x, signal_dist, alpha=0.5, color='green', label='H1: 訊號+雜訊')
    
    threshold = 2.5
    ax.axvline(x=threshold, color='red', linestyle='--', linewidth=2, label=f'Threshold = {threshold}')
    
    # 標示區域
    ax.fill_between(x[x > threshold], noise_dist[x > threshold], alpha=0.3, color='red')
    ax.text(3.5, 0.5, '誤警\n(False Alarm)', fontsize=10, color='red', ha='center')
    
    ax.fill_between(x[x < threshold], signal_dist[x < threshold], alpha=0.3, color='orange')
    ax.text(1.5, 0.3, '漏檢\n(Missed Detection)', fontsize=10, color='orange', ha='center')
    
    ax.set_xlabel('偵測度量值')
    ax.set_ylabel('機率密度')
    ax.set_title('(a) 統計決策理論：門檻判決')
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0, 8])
    ax.set_ylim([0, 2.5])
    
    # (b) detection_metric 的意義
    ax = axes[1]
    
    metrics = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]
    colors = ['red', 'orange', 'yellow', 'lightgreen', 'green', 'darkgreen']
    labels = ['非常不可靠', '剛好達標', '可接受', '良好', '很好', '優秀']
    
    bars = ax.bar(range(len(metrics)), metrics, color=colors, edgecolor='black', linewidth=2)
    ax.axhline(y=1.0, color='red', linestyle='--', linewidth=2, label='Threshold (門檻)')
    
    ax.set_xticks(range(len(metrics)))
    ax.set_xticklabels([f'{m}' for m in metrics])
    ax.set_xlabel('detection_metric = peak / threshold')
    ax.set_ylabel('數值')
    ax.set_title('(b) detection_metric 的意義')
    
    # 添加標籤
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
    """生成所有圖片"""
    print("正在生成圖1: ZC 序列特性...")
    plot_1_zc_sequence_properties()
    
    print("正在生成圖2: PRACH 偵測原理...")
    plot_2_detection_principle()
    
    print("正在生成圖3: 偵測窗口結構...")
    plot_3_window_structure()
    
    print("正在生成圖4: 多 UE 偵測情況...")
    plot_4_multi_ue_detection()
    
    print("正在生成圖5: 偵測演算法流程圖...")
    plot_5_detection_flowchart()
    
    print("正在生成圖6: 門檻判決說明...")
    plot_6_threshold_decision()
    
    print("\n所有圖片已生成完成！")
    print("生成的檔案：")
    print("  - fig1_zc_sequence_properties.png")
    print("  - fig2_detection_principle.png")
    print("  - fig3_window_structure.png")
    print("  - fig4_multi_ue_detection.png")
    print("  - fig5_detection_flowchart.png")
    print("  - fig6_threshold_decision.png")

if __name__ == "__main__":
    plot_all()
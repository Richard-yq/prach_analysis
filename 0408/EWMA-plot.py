import matplotlib.pyplot as plt
import numpy as np

# 設置字體與樣式，適合論文與圖表展示
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Liberation Sans', 'Helvetica']
plt.rcParams['font.size'] = 14

# ================================
# 參數設定區 (使用者可自行調整)
# ================================
P_initial = 16.5     # 系統初始的背景雜訊 / 閾值 (dB) - 假設從較低數值開始
P_received = 56.0    # 每次接收到的訊號大小 (dB) - 例如 Attacker 造成的 56dB 訊號
beta = 0.2           # EWMA 平滑參數預設值
total_times = 15     # 要觀察接收幾次

# 計算：
# 產生 X 軸 (接收次數 j = 0, 1, 2... )
j_values = np.arange(0, total_times + 1)

# EWMA 數學遞迴公式所推導出的理論成長曲線：
# P_th[j] = P_initial * (1-beta)^j + P_received * (1 - (1-beta)^j)
ewma_curve = P_initial * ((1 - beta) ** j_values) + P_received * (1 - ((1 - beta) ** j_values))

# ================================
# 繪圖
# ================================
fig, ax = plt.subplots(figsize=(10, 6))

# 繪製 EWMA 成長曲線 (不連線，使用星星符號)
ax.plot(j_values, ewma_curve, marker='*', markersize=10, linestyle='none', 
        color='#D32F2F', label=rf'Threshold ($\beta={beta}$)')

# 繪製 Detection Margin 輔助線 (原 initial state)
# ax.axhline(P_initial, color='#7F8C8D', linestyle=':', linewidth=2, 
#            label=f'Detection Margin ({P_initial} dB)')

# 設定 Margin 與畫出偵測邊界
margin = 12.0
detectable_boundary = ewma_curve + margin

# 畫出加上 margin 後的邊界線
ax.plot(j_values, detectable_boundary, color='#388E3C', linestyle='-', linewidth=2, alpha=0.8,
        label=f'Threshold + Margin ({margin} dB)')

# 上方的區域填綠色色塊 (Detectable)
ax.fill_between(j_values, detectable_boundary, 80, color='#C8E6C9', alpha=0.5)

# 下方的區域用不同顏色區分 (Undetectable)
ax.fill_between(j_values, 0, detectable_boundary, color='#FFCDD2', alpha=0.3)

# 找地方標註 Detectable / Undetectable
ax.text(total_times / 2, 72, 'Detectable', ha='center', va='center', fontsize=16, color='#2E7D32', fontweight='bold')
ax.text(total_times / 2, 25, 'Undetectable', ha='center', va='center', fontsize=16, color='#C62828', fontweight='bold')

# 標籤與細節美化
title_text = (
    'EWMA Threshold Progression\n'
    f'($P_{{int}} = {P_initial}$ dB, $P_{{recv}} = {P_received}$ dB, '
    f'Margin = {margin} dB, $\\beta = {beta}$)'
)
plt.title(title_text, fontweight='bold', pad=15, fontsize=15)
ax.set_xlabel('Number of Received Signals', fontweight='bold')
ax.set_ylabel('Power (dB)', fontweight='bold')

# 設定 Y 軸與格線
ax.set_ylim(0, 80)
ax.set_xticks(np.arange(0, total_times + 1, 5))
ax.grid(True, linestyle='--', alpha=0.6, color='gray')

ax.legend(loc='lower right', edgecolor='#E0E0E0', framealpha=0.9)

plt.tight_layout()
plt.savefig('EWMA-plot.png', dpi=300)
plt.show()

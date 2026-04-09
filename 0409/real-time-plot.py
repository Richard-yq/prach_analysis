import matplotlib.pyplot as plt
import numpy as np

# 設置字體與樣式，適合論文與圖表展示
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Liberation Sans', 'Helvetica']
plt.rcParams['font.size'] = 14

# ================================
# 參數設定區 (使用者可自行調整)
# ================================
# P_threshold 隨時間變動 (這裡以 50~55 dB 為例，可自由更改為 20~30 等)
min_threshold = 50.0
max_threshold = 55.0
margin = 12.0        # Detection Margin (dB)
total_times = 15     # 觀察的時間長度

# 計算：
# 產生 X 軸 (接收次數 j = 0, 1, 2... )
j_values = np.arange(0, total_times + 1)

# 隨時間變動的閾值與邊界
np.random.seed(42)  # 固定亂數種子，確保每次執行圖表一致
threshold_curve = np.random.uniform(min_threshold, max_threshold, size=len(j_values))
detectable_boundary = threshold_curve + margin

# ================================
# 繪圖
# ================================
fig, ax = plt.subplots(figsize=(10, 6))

# 繪製 固定 Threshold (跟 EWMA 版本一樣使用星星符號)
ax.plot(j_values, threshold_curve, marker='*', markersize=10, linestyle='none', 
        color='#D32F2F', label=f'Threshold')

# 畫出加上 margin 後的邊界線
ax.plot(j_values, detectable_boundary, color='#388E3C', linestyle='-', linewidth=2, alpha=0.8,
        label=f'Threshold + Margin ({margin} dB)')

# 上方的區域填綠色色塊 (Detectable)
ax.fill_between(j_values, detectable_boundary, 80, color='#C8E6C9', alpha=0.5)

# 下方的區域用淡紅色區分 (Undetectable)
ax.fill_between(j_values, 0, detectable_boundary, color='#FFCDD2', alpha=0.3)

# 標註區域 Detectable / Undetectable
# 高度依照 Y 軸配置稍微調低以置中
ax.text(total_times / 2, 70, 'Detectable', ha='center', va='center', fontsize=16, color='#2E7D32', fontweight='bold')
ax.text(total_times / 2, 25, 'Undetectable', ha='center', va='center', fontsize=16, color='#C62828', fontweight='bold')

# 標籤與細節美化
title_text = (
    'Real-time Detection Threshold\n'
    rf'($P_{{\mathrm{{th}}}} \in [{min_threshold:.0f}, {max_threshold:.0f}]$ dB, Margin = {margin} dB)'
)
plt.title(title_text, fontweight='bold', pad=15, fontsize=16)
ax.set_xlabel('Number of Received Signals', fontweight='bold')
ax.set_ylabel('Power (dB)', fontweight='bold')

# 設定 Y 軸與格線 (將視角放大以跟上一張圖對齊)
ax.set_ylim(0, 80)
ax.set_xticks(np.arange(0, total_times + 1, 5))
ax.grid(True, linestyle='--', alpha=0.6, color='gray')

ax.legend(loc='lower right', edgecolor='#E0E0E0', framealpha=0.9)

plt.tight_layout()
plt.savefig('real-time-plot.png', dpi=300)
plt.show()

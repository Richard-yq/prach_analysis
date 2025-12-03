import matplotlib.pyplot as plt
import numpy as np

# 數據定義
distances = [80, 150, 220, 350]
prach_configs = [157, 159, 146, 148, 145]

# 結果矩陣 (1 = 成功, 0 = 失敗, NaN = 未測試)
# 行: 距離 (80, 150, 220, 350)
# 列: PRACH config index (157, 159, 146, 148, 145)
results = np.array([
    [1, 1, 1, 1, 1],  # 80cm: 157✅, 159✅, 146✅, 148✅, 145未測試
    [1, 1, 1, 1, 1],       # 150cm: 全部✅
    [1, 1, 1, 1, 1],       # 220cm: 全部✅
    [0, 0, 0, 0, 0],       # 350cm: 全部❌
], dtype=float)

# 設置圖表
fig, ax = plt.subplots(figsize=(10, 6))

# 顏色映射 (包含灰色用於未測試)
colors = ['#ff6b6b', '#51cf66']  # 紅色=失敗, 綠色=成功
cmap = plt.cm.colors.ListedColormap(colors)
cmap.set_bad(color='#cccccc')  # 設置 NaN 為灰色

# 繪製熱力圖
im = ax.imshow(results, cmap=cmap, aspect='auto', vmin=0, vmax=1)

# 設置軸標籤
ax.set_xticks(np.arange(len(prach_configs)))
ax.set_yticks(np.arange(len(distances)))
ax.set_xticklabels(prach_configs)
ax.set_yticklabels(['80 cm', '150 cm', '220 cm', '350 cm (Non LOS)'])

ax.set_xlabel('PRACH Configuration Index', fontsize=12)
ax.set_ylabel('Distance', fontsize=12)
ax.set_title('PRACH Attack Results by Distance and Configuration', fontsize=14)

# 在每個格子中添加符號
for i in range(len(distances)):
    for j in range(len(prach_configs)):
        if np.isnan(results[i, j]):
            text = 'N/A'
            color = 'gray'
        elif results[i, j] == 1:
            text = '✅'
            color = 'white'
        else:
            text = '❌'
            color = 'white'
        ax.text(j, i, text, ha='center', va='center', fontsize=16, color=color)

# 添加網格線
ax.set_xticks(np.arange(len(prach_configs) + 1) - 0.5, minor=True)
ax.set_yticks(np.arange(len(distances) + 1) - 0.5, minor=True)
ax.grid(which='minor', color='white', linestyle='-', linewidth=2)

# 添加圖例
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#51cf66', edgecolor='black', label='Success (O)'),
    Patch(facecolor='#ff6b6b', edgecolor='black', label='Failed (X)')
]
ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.25, 1))

plt.tight_layout()
plt.savefig('/Users/yq/Documents/analysis/1203/distance_attack_results.png', dpi=150, bbox_inches='tight')
# plt.show()  # 使用 Agg 後端時不需要 show()

print("圖表已儲存至 distance_attack_results.png")

# 額外繪製：條形圖顯示各距離的成功率
fig2, ax2 = plt.subplots(figsize=(8, 5))

success_rates = []
for i, d in enumerate(distances):
    # 計算每個距離的成功率（排除未測試的項目）
    valid_results = results[i, ~np.isnan(results[i, :])]
    rate = np.sum(valid_results) / len(valid_results) * 100
    success_rates.append(rate)

bars = ax2.bar(range(len(distances)), success_rates, color=['#51cf66' if r > 50 else '#ff6b6b' for r in success_rates])

ax2.set_xticks(range(len(distances)))
ax2.set_xticklabels(['80 cm', '150 cm', '220 cm', '350 cm\n(Not LOS)'])
ax2.set_xlabel('Distance', fontsize=12)
ax2.set_ylabel('Success Rate (%)', fontsize=12)
ax2.set_title('PRACH Attack Success Rate by Distance', fontsize=14)
ax2.set_ylim(0, 110)

# 在條形上方添加百分比標籤
for bar, rate in zip(bars, success_rates):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, 
             f'{rate:.0f}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('/Users/yq/Documents/analysis/1203/distance_success_rate.png', dpi=150, bbox_inches='tight')
# plt.show()  # 使用 Agg 後端時不需要 show()

print("成功率圖表已儲存至 distance_success_rate.png")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ===== 1) 讀取 CSV 數據 =====
csv_dir = Path(__file__).parent

# 讀取整體 1000 筆測試結果
test_results_df = pd.read_csv(csv_dir / 'test_results.csv')
total_tests = len(test_results_df)
success_tests = (test_results_df['result'] == 'success').sum()
failed_tests = total_tests - success_tests
success_rate = success_tests / total_tests * 100

# 讀取重複測試的成功率
repeat_tests_df = pd.read_csv(csv_dir / 'repeat_tests.csv')
repeat_success_rate = repeat_tests_df['success_rate'].values
repeat_rounds = len(repeat_success_rate)
repeat_std = repeat_success_rate.std()
repeat_mean = repeat_success_rate.mean()

print(f"✓ 讀取成功：{total_tests} 筆測試結果 (成功: {success_tests}, 失敗: {failed_tests})")
print(f"✓ 讀取成功：{repeat_rounds} 次重複測試結果")

# ===== 2) 繪圖 =====
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)

# 折線圖：1~120 無攻擊，121~最後一輪 攻擊中
round_idx = np.arange(1, repeat_rounds + 1)
no_attack_mask = round_idx <= 120
attack_mask = round_idx > 120

ax.plot(
	round_idx[no_attack_mask],
	repeat_success_rate[no_attack_mask],
	color='#1f77b4',
	linewidth=2.0,
	marker='o',
	markersize=2.8,
	label='No Attack (Round 1-120)'
)
ax.plot(
	round_idx[attack_mask],
	repeat_success_rate[attack_mask],
	color='#d62728',
	linewidth=2.0,
	marker='o',
	markersize=2.8,
	label=f'Under Attack (Round 121-{repeat_rounds})'
)

no_attack_mean = repeat_success_rate[no_attack_mask].mean()
attack_mean = repeat_success_rate[attack_mask].mean()

ax.axhline(no_attack_mean, color='#1f77b4', linestyle='--', linewidth=1.6, alpha=0.7, label=f'No Attack Avg: {no_attack_mean:.2f}%')
ax.axhline(attack_mean, color='#d62728', linestyle='--', linewidth=1.6, alpha=0.7, label=f'Attack Avg: {attack_mean:.2f}%')
ax.axvline(120, color='#555555', linestyle=':', linewidth=1.8)
ax.axvspan(1, 120, color='#1f77b4', alpha=0.06)
ax.axvspan(120, repeat_rounds, color='#d62728', alpha=0.06)

# 區間標示 (i) / (ii)
ax.text(
	60,
	92,
	'(i) No Attack',
	color='#1f77b4',
	fontsize=11,
	ha='center',
	va='center',
	fontweight='bold',
	bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.75, edgecolor='none'),
)
ax.text(
	(120 + repeat_rounds) / 2,
	8,
	'(ii) Under Attack',
	color='#d62728',
	fontsize=11,
	ha='center',
	va='center',
	fontweight='bold',
	bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.75, edgecolor='none'),
)

ax.set_title(f'RACH Success Rate Across {repeat_rounds} Test Rounds (No Attack -> Under Attack)', fontsize=14, pad=15)
ax.set_xlabel('Test Round', fontsize=12)
ax.set_ylabel('RACH Success Rate (%)', fontsize=12)
ax.set_xlim(1, repeat_rounds)
ax.set_ylim(-1, 101)
ax.grid(True, linestyle='--', alpha=0.35)
ax.legend(loc='lower left', fontsize=11)

# # 右上角統計資訊框
# stats_text = (
# 	f'No Attack (1-120): avg={no_attack_mean:.2f}%\n'
# 	f'Under Attack (121-{repeat_rounds}): avg={attack_mean:.3f}%\n\n'
# 	f'Overall Mean: {repeat_mean:.2f}%\n'
# 	f'Std Dev: {repeat_std:.2f}%\n'
# 	f'Min: {repeat_success_rate.min():.3f}% | Max: {repeat_success_rate.max():.1f}%'
# )
# ax.text(
# 	0.98,
# 	0.97,
# 	stats_text,
# 	transform=ax.transAxes,
# 	fontsize=10,
# 	verticalalignment='top',
# 	horizontalalignment='right',
# 	bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3),
# )

fig.tight_layout()

# 儲存 PNG 到同目錄
output_path = Path(__file__).with_suffix('.png')
fig.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"PNG saved: {output_path}")

# 顯示（需要互動視窗時可取消註解）
# plt.show()
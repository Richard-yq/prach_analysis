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

# 折線圖：重複 120 次測試的成功率波動
round_idx = np.arange(1, repeat_rounds + 1)
ax.plot(round_idx, repeat_success_rate, color='#1f77b4', linewidth=2.2, marker='o', markersize=3.0, label='Test Round Success Rate')
ax.axhline(repeat_mean, color='#d62728', linestyle='--', linewidth=1.8, label=f'Average: {repeat_mean:.1f}%')
ax.fill_between(round_idx, 89, repeat_success_rate, alpha=0.1, color='#1f77b4')

ax.set_title('RACH Success Rate Across 120 Repeated Test Rounds', fontsize=14, pad=15)
ax.set_xlabel('Test Round', fontsize=12)
ax.set_ylabel('RACH Success Rate (%)', fontsize=12)
ax.set_ylim(87, 101)
ax.grid(True, linestyle='--', alpha=0.35)
ax.legend(loc='lower left', fontsize=11)

# # 右上角統計資訊框
# stats_text = (
# 	f'Overall Test: 1000 attempts\n'
# 	f'Success: 970 (97.0%) | Failure: 30 (3.0%)\n\n'
# 	f'Repeatability across {repeat_rounds} runs:\n'
# 	f'Mean RSR: {repeat_mean:.2f}%\n'
# 	f'Std Dev: {repeat_std:.2f}%\n'
# 	f'Min: {repeat_success_rate.min():.1f}% | Max: {repeat_success_rate.max():.1f}%'
# )
# ax.text(0.98, 0.97, stats_text, transform=ax.transAxes, fontsize=10, 
# 	verticalalignment='top', horizontalalignment='right',
# 	bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

fig.tight_layout()

# 儲存 PNG 到同目錄
output_path = Path(__file__).with_suffix('.png')
fig.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"PNG saved: {output_path}")

# 顯示（需要互動視窗時可取消註解）
# plt.show()
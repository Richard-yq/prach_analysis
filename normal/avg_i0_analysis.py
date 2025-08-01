import re
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
import numpy as np
import statistics
from datetime import datetime

# 設定中文字體支援
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']  # 設定字體優先順序
plt.rcParams['axes.unicode_minus'] = False  # 正確顯示負號

# 讀取日誌資料
with open('/Users/yq/Documents/analysis/avg-i0_normal.py', 'r', encoding='utf-8') as file:
    log_data = file.read()

# 使用正則表達式提取 avg_I0 和 prach_I0 數據
# 模式匹配: [frame.slot] NR gNB I0 measurements: avg_I0=XX dB, prach_I0=XX dB, measured_PRBs=XXX
pattern = r'\[(\d+\.\d+)\] NR gNB I0 measurements: avg_I0=(\d+) dB, prach_I0=([0-9.]+) dB, measured_PRBs=(\d+)'
matches = re.findall(pattern, log_data)

print(f"找到 {len(matches)} 個測量記錄")

if not matches:
    print("未找到匹配的資料，請檢查日誌格式")
    exit()

# 提取資料
frame_slots = []
avg_i0_values = []
prach_i0_values = []
measured_prbs = []

for match in matches:
    frame_slot = float(match[0])
    avg_i0 = int(match[1])
    prach_i0 = float(match[2])
    prb = int(match[3])
    
    frame_slots.append(frame_slot)
    avg_i0_values.append(avg_i0)
    prach_i0_values.append(prach_i0)
    measured_prbs.append(prb)

print(f"資料範圍: Frame {min(frame_slots):.2f} 到 {max(frame_slots):.2f}")
print(f"avg_I0 範圍: {min(avg_i0_values)} dB 到 {max(avg_i0_values)} dB")
print(f"prach_I0 範圍: {min(prach_i0_values):.1f} dB 到 {max(prach_i0_values):.1f} dB")

# 檢查重複的frame.slot
frame_count = {}
for frame in frame_slots:
    if frame in frame_count:
        frame_count[frame] += 1
    else:
        frame_count[frame] = 1

duplicated_frames = {k: v for k, v in frame_count.items() if v > 1}
if duplicated_frames:
    print(f"\n⚠️  發現重複的frame.slot: {len(duplicated_frames)} 個")
    print("前10個重複例子:")
    for i, (frame, count) in enumerate(list(duplicated_frames.items())[:10]):
        print(f"  Frame {frame}: {count} 筆資料")
else:
    print(f"\n✅ 無重複的frame.slot")

# 去除重複的frame.slot資料，保留每個frame的最後一筆資料
if duplicated_frames:
    print(f"正在去除重複資料...")
    # 使用字典來保存每個frame的最後一筆資料
    unique_data = {}
    
    for i, frame_slot in enumerate(frame_slots):
        unique_data[frame_slot] = {
            'avg_i0': avg_i0_values[i],
            'prach_i0': prach_i0_values[i],
            'measured_prb': measured_prbs[i]
        }
    
    # 重新建立資料列表
    frame_slots = sorted(unique_data.keys())
    avg_i0_values = [unique_data[frame]['avg_i0'] for frame in frame_slots]
    prach_i0_values = [unique_data[frame]['prach_i0'] for frame in frame_slots]
    measured_prbs = [unique_data[frame]['measured_prb'] for frame in frame_slots]
    
    print(f"去重後資料點數: {len(frame_slots)} (原: {len(matches)})")
    print(f"去除了 {len(matches) - len(frame_slots)} 個重複資料點")

# 重新計算統計分析（使用去重後的資料）
avg_i0_stats = {
    '平均值': statistics.mean(avg_i0_values),
    '中位數': statistics.median(avg_i0_values),
    '標準差': statistics.stdev(avg_i0_values) if len(avg_i0_values) > 1 else 0,
    '最小值': min(avg_i0_values),
    '最大值': max(avg_i0_values),
    '變化範圍': max(avg_i0_values) - min(avg_i0_values)
}

prach_i0_stats = {
    '平均值': statistics.mean(prach_i0_values),
    '中位數': statistics.median(prach_i0_values),
    '標準差': statistics.stdev(prach_i0_values) if len(prach_i0_values) > 1 else 0,
    '最小值': min(prach_i0_values),
    '最大值': max(prach_i0_values),
    '變化範圍': max(prach_i0_values) - min(prach_i0_values)
}


print("\n=== avg_I0 統計分析 ===")
for key, value in avg_i0_stats.items():
    print(f"{key}: {value:.2f} dB")

print("\n=== prach_I0 統計分析 ===")
for key, value in prach_i0_stats.items():
    print(f"{key}: {value:.2f} dB")

# 重新計算不同avg_I0值的分佈（使用去重後的資料）
avg_i0_distribution = {}
for value in avg_i0_values:
    if value in avg_i0_distribution:
        avg_i0_distribution[value] += 1
    else:
        avg_i0_distribution[value] = 1

print(f"\n=== avg_I0 值分佈 ===")
for value in sorted(avg_i0_distribution.keys()):
    percentage = (avg_i0_distribution[value] / len(avg_i0_values)) * 100
    print(f"{value} dB: {avg_i0_distribution[value]} 次 ({percentage:.1f}%)")

# 創建圖表
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('NR gNB I0 測量分析 - avg_I0 變化趨勢', fontsize=16, fontweight='bold')

# 1. avg_I0 時間序列 - 使用階梯圖更適合離散值
ax1.step(frame_slots, avg_i0_values, 'b-', linewidth=1.5, alpha=0.8, label='avg_I0', where='post')
ax1.set_xlabel('Frame.Slot')
ax1.set_ylabel('avg_I0 (dB)')
ax1.set_title('avg_I0 隨時間變化')
ax1.grid(True, alpha=0.3)

# 設定Y軸範圍顯示所有數據，包括極值
y_min = min(avg_i0_values) - 2
y_max = max(avg_i0_values) + 5  # 增加更多空間以清楚顯示最高值
ax1.set_ylim(y_min, y_max)

# 添加主要水平參考線
for value in [24, 27, 31]:
    if value in avg_i0_distribution:
        percentage = (avg_i0_distribution[value] / len(avg_i0_values)) * 100
        ax1.axhline(y=value, color='gray', linestyle='--', alpha=0.5, linewidth=0.8)
        ax1.text(0.02, (value-y_min)/(y_max-y_min), f'{value}dB ({percentage:.1f}%)', 
                transform=ax1.transAxes, fontsize=9, color='gray')

ax1.legend()

# 2. prach_I0 時間序列 - 使用平滑線條
ax2.plot(frame_slots, prach_i0_values, 'r-', linewidth=1, alpha=0.7, label='prach_I0')
ax2.set_xlabel('Frame.Slot')
ax2.set_ylabel('prach_I0 (dB)')
ax2.set_title('prach_I0 隨時間變化')
ax2.grid(True, alpha=0.3)

# 設定prach_I0的Y軸範圍顯示完整數據
y_min_prach = min(prach_i0_values) - 1
y_max_prach = max(prach_i0_values) + 2
ax2.set_ylim(y_min_prach, y_max_prach)

# 添加平均值參考線
mean_prach = statistics.mean(prach_i0_values)
ax2.axhline(y=mean_prach, color='darkred', linestyle='--', alpha=0.7, linewidth=1)
ax2.text(0.02, 0.95, f'平均值: {mean_prach:.1f} dB', transform=ax2.transAxes, 
         bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8), fontsize=9)

ax2.legend()

# 3. avg_I0 值分佈直方圖
unique_values = list(avg_i0_distribution.keys())
counts = list(avg_i0_distribution.values())
bars = ax3.bar(unique_values, counts, alpha=0.7, color='blue', edgecolor='black')
ax3.set_xlabel('avg_I0 (dB)')
ax3.set_ylabel('出現次數')
ax3.set_title('avg_I0 值分佈')
ax3.grid(True, alpha=0.3)

# 在每個柱狀圖上標註數值
for bar, count in zip(bars, counts):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
             f'{count}', ha='center', va='bottom', fontsize=10)

# 4. avg_I0 極值事件分析
extreme_threshold = 40  # 定義極值閾值
extreme_indices = [i for i, v in enumerate(avg_i0_values) if v >= extreme_threshold]
extreme_frames = [frame_slots[i] for i in extreme_indices]
extreme_values = [avg_i0_values[i] for i in extreme_indices]

if extreme_values:
    # 顯示極值事件
    ax4.scatter(extreme_frames, extreme_values, color='red', s=50, alpha=0.7, 
                label=f'極值事件 (≥{extreme_threshold}dB)')
    ax4.set_xlabel('Frame.Slot')
    ax4.set_ylabel('avg_I0 (dB)')
    ax4.set_title(f'avg_I0 極值事件 (共{len(extreme_values)}次)')
    ax4.grid(True, alpha=0.3)
    
    # 設定Y軸範圍只顯示極值範圍
    if extreme_values:
        y_min_extreme = min(extreme_values) - 2
        y_max_extreme = max(extreme_values) + 2
        ax4.set_ylim(y_min_extreme, y_max_extreme)
    
    # 添加統計資訊
    ax4.text(0.02, 0.95, f'極值次數: {len(extreme_values)}', transform=ax4.transAxes,
             bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.7), fontsize=9)
    ax4.text(0.02, 0.85, f'極值範圍: {min(extreme_values)}-{max(extreme_values)} dB', 
             transform=ax4.transAxes,
             bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.7), fontsize=9)
    
    ax4.legend()
else:
    ax4.text(0.5, 0.5, '無極值事件', transform=ax4.transAxes, 
             ha='center', va='center', fontsize=14)
    ax4.set_title('avg_I0 極值事件分析')
    ax4.set_xlabel('Frame.Slot')
    ax4.set_ylabel('avg_I0 (dB)')

plt.tight_layout()
plt.subplots_adjust(top=0.93)

# 儲存圖表
plt.savefig('/Users/yq/Documents/analysis/normal/avg_i0_analysis.png', dpi=300, bbox_inches='tight')
print(f"\n圖表已儲存為: avg_i0_analysis.png")

plt.show()

# 創建第二個圖表：詳細的avg_I0分析
fig2, ((ax5, ax6), (ax7, ax8)) = plt.subplots(2, 2, figsize=(15, 12))
fig2.suptitle('avg_I0 詳細分析', fontsize=16, fontweight='bold')

# 5. avg_I0和prach_I0的相關性散點圖
ax5.scatter(avg_i0_values, prach_i0_values, alpha=0.6, s=10)
ax5.set_xlabel('avg_I0 (dB)')
ax5.set_ylabel('prach_I0 (dB)')
ax5.set_title('avg_I0 vs prach_I0 相關性')
ax5.grid(True, alpha=0.3)

# 計算相關係數
correlation = np.corrcoef(avg_i0_values, prach_i0_values)[0, 1]
ax5.text(0.05, 0.95, f'相關係數: {correlation:.3f}', transform=ax5.transAxes, 
         bbox=dict(boxstyle="round", facecolor='wheat', alpha=0.5))

# 6. avg_I0變化事件檢測
avg_i0_changes = []
change_frames = []
for i in range(1, len(avg_i0_values)):
    if avg_i0_values[i] != avg_i0_values[i-1]:
        change = avg_i0_values[i] - avg_i0_values[i-1]
        avg_i0_changes.append(change)
        change_frames.append(frame_slots[i])

if avg_i0_changes:
    ax6.stem(change_frames, avg_i0_changes, basefmt=' ')
    ax6.set_xlabel('Frame.Slot')
    ax6.set_ylabel('avg_I0 變化量 (dB)')
    ax6.set_title('avg_I0 變化事件')
    ax6.grid(True, alpha=0.3)
    ax6.axhline(y=0, color='k', linestyle='-', alpha=0.3)
else:
    ax6.text(0.5, 0.5, '無avg_I0變化事件', transform=ax6.transAxes, 
             ha='center', va='center', fontsize=14)
    ax6.set_title('avg_I0 變化事件')

# 7. 移動平均分析
window_size = min(50, len(prach_i0_values) // 10)  # 動態窗口大小
if window_size > 1:
    prach_i0_ma = np.convolve(prach_i0_values, np.ones(window_size)/window_size, mode='valid')
    ma_frames = frame_slots[window_size-1:]
    
    ax7.plot(frame_slots, prach_i0_values, 'lightcoral', alpha=0.5, label='原始prach_I0')
    ax7.plot(ma_frames, prach_i0_ma, 'darkred', linewidth=2, label=f'{window_size}點移動平均')
    ax7.set_xlabel('Frame.Slot')
    ax7.set_ylabel('prach_I0 (dB)')
    ax7.set_title('prach_I0 移動平均趨勢')
    ax7.legend()
    ax7.grid(True, alpha=0.3)
else:
    ax7.plot(frame_slots, prach_i0_values, 'r-', linewidth=1)
    ax7.set_xlabel('Frame.Slot')
    ax7.set_ylabel('prach_I0 (dB)')
    ax7.set_title('prach_I0 趨勢（資料點不足進行移動平均）')
    ax7.grid(True, alpha=0.3)

# 8. 統計摘要表格
ax8.axis('tight')
ax8.axis('off')

# 準備表格資料
table_data = [
    ['參數', 'avg_I0', 'prach_I0'],
    ['平均值', f"{avg_i0_stats['平均值']:.2f} dB", f"{prach_i0_stats['平均值']:.2f} dB"],
    ['標準差', f"{avg_i0_stats['標準差']:.2f} dB", f"{prach_i0_stats['標準差']:.2f} dB"],
    ['最小值', f"{avg_i0_stats['最小值']:.2f} dB", f"{prach_i0_stats['最小值']:.2f} dB"],
    ['最大值', f"{avg_i0_stats['最大值']:.2f} dB", f"{prach_i0_stats['最大值']:.2f} dB"],
    ['變化範圍', f"{avg_i0_stats['變化範圍']:.2f} dB", f"{prach_i0_stats['變化範圍']:.2f} dB"],
    ['資料點數', f"{len(avg_i0_values)}", f"{len(prach_i0_values)}"],
    ['相關係數', f"{correlation:.3f}", ''],
]

table = ax8.table(cellText=table_data, cellLoc='center', loc='center',
                  colWidths=[0.3, 0.35, 0.35])
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2)

# 設定表格樣式
for i in range(len(table_data)):
    for j in range(len(table_data[i])):
        cell = table[(i, j)]
        if i == 0:  # 標題行
            cell.set_facecolor('#4CAF50')
            cell.set_text_props(weight='bold', color='white')
        else:
            cell.set_facecolor('#f0f0f0' if i % 2 == 0 else 'white')

ax8.set_title('統計摘要', fontweight='bold', pad=20)

plt.tight_layout()
plt.subplots_adjust(top=0.93)

# 儲存第二個圖表
plt.savefig('/Users/yq/Documents/analysis/normal/avg_i0_detailed_analysis.png', dpi=300, bbox_inches='tight')
print(f"詳細分析圖表已儲存為: avg_i0_detailed_analysis.png")

plt.show()

# 生成分析報告
print("\n" + "="*60)
print("             NR gNB I0 測量分析報告")
print("="*60)
print(f"分析時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"原始測量記錄: {len(matches)}")
print(f"去重後資料點: {len(frame_slots)}")
print(f"測量時間範圍: Frame {min(frame_slots):.2f} 到 {max(frame_slots):.2f}")
print(f"measured_PRBs: {measured_prbs[0]} (固定值)")

print(f"\n【avg_I0 分析結果】")
print(f"• 平均值: {avg_i0_stats['平均值']:.2f} dB")
print(f"• 標準差: {avg_i0_stats['標準差']:.2f} dB")
print(f"• 變化範圍: {avg_i0_stats['變化範圍']:.2f} dB ({avg_i0_stats['最小值']} ~ {avg_i0_stats['最大值']} dB)")
print(f"• 變化事件: {len(avg_i0_changes)} 次")

print(f"\n【prach_I0 分析結果】")
print(f"• 平均值: {prach_i0_stats['平均值']:.2f} dB")
print(f"• 標準差: {prach_i0_stats['標準差']:.2f} dB")
print(f"• 變化範圍: {prach_i0_stats['變化範圍']:.2f} dB ({prach_i0_stats['最小值']:.1f} ~ {prach_i0_stats['最大值']:.1f} dB)")

print(f"\n【相關性分析】")
print(f"• avg_I0 與 prach_I0 相關係數: {correlation:.3f}")
if abs(correlation) > 0.7:
    correlation_desc = "強相關"
elif abs(correlation) > 0.3:
    correlation_desc = "中等相關"
else:
    correlation_desc = "弱相關"
print(f"• 相關性強度: {correlation_desc}")

print(f"\n【關鍵觀察】")
if avg_i0_stats['變化範圍'] == 0:
    print("• avg_I0 值穩定，無變化")
else:
    print(f"• avg_I0 有變化，主要在 {min(avg_i0_values)} dB 和 {max(avg_i0_values)} dB 之間切換")

print(f"• prach_I0 變化相對平穩，標準差為 {prach_i0_stats['標準差']:.2f} dB")

if prach_i0_stats['平均值'] > 15:
    print("• prach_I0 平均值偏高，可能存在干擾")
else:
    print("• prach_I0 水平正常")

print("="*60)

#!/usr/bin/env python3
"""
將 MTKUE log 畫成 MATLAB 風格圖 (使用 matplotlib)
- x 軸: time (秒)
- y 軸: TX power (dBm)
- preamble index: 用顏色 (colorbar)，也可改成標記或標註

使用方式:
    python3 plot_mtkue_matlab_style.py

如果想改時間轉換常數 (frame/slot/symbol duration)，請修改 FRAMEDUR/SLOTDUR/SYMDUR
"""
import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.lines import Line2D

# 原始 log (從 MTKUE-rammping.py 拷貝)
raw = '''
604/9/1/2 | -19 dBm | 55 |
605/9/1/2 | -17 dBm | 31 |
606/9/1/2 | -15 dBm | 20 |
607/9/1/2 | -13 dBm | 4 |
609/9/1/2 | -9 dBm  | 53 |
610/9/1/2 | -8 dBm  | 27 |
611/9/1/2 | -6 dBm  | 0 |
612/9/1/2 | -3 dBm  | 41 |
613/9/1/2 | -1 dBm  | 6 |
614/9/1/2 | 1 dBm   | 50 |
615/9/1/2 | 3 dBm   | 59 |
616/9/1/2 | 4 dBm   | 5 |
617/9/1/2 | 6 dBm   | 47 |
618/9/1/2 | 9 dBm   | 11 |
619/9/1/2 | 11 dBm  | 50 |
620/9/1/2 | 13 dBm  | 9 |
621/9/1/2 | 15 dBm  | 42 |
622/9/1/2 | 17 dBm  | 41 |
623/9/1/2 | 19 dBm  | 33 |
624/9/1/2 | 20 dBm  | 29 |
625/9/1/2 | 20 dBm  | 28 |
626/9/1/2 | 20 dBm  | 6 |
627/9/1/2 | 20 dBm  | 11 |
628/9/1/2 | 20 dBm  | 28 |
629/9/1/2 | 20 dBm  | 31 |
630/9/1/2 | 20 dBm  | 54 |
631/9/1/2 | 20 dBm  | 9 |
632/9/1/2 | 20 dBm  | 7 |
633/9/1/2 | 20 dBm  | 32 |
634/9/1/2 | 20 dBm  | 26 |
635/9/1/2 | 20 dBm  | 58 |
636/9/1/2 | 20 dBm  | 32 |
637/9/1/2 | 20 dBm  | 27 |
638/9/1/2 | 20 dBm  | 28 |
639/9/1/2 | 20 dBm  | 1 |
640/9/1/2 | 20 dBm  | 51 |
'''

# 參數: 時間換算常數（可根據實際系統調整）
FRAMEDUR = 0.01        # frame (SFN) 長度 (s) -> 10 ms
SLOTDUR  = 0.0005      # slot 長度 (s) -> 0.5 ms
SYMDUR   = 0.0000714286 # symbol 長度 (s) -> 約 71.4286 us (14 symbols/1ms)

pattern = re.compile(r"(\d+)/(\d+)/(\d+)/(\d+)\s*\|\s*([+-]?\d+)\s*dBm\s*\|\s*(\d+)")
rows = []
for m in pattern.finditer(raw):
    sfn, sfn2, slot, sym, power, pre = m.groups()
    # 解析為數值
    sfn = int(sfn)
    slot = int(slot)
    sym = int(sym)
    power = int(power)
    pre = int(pre)
    # 同時保留 SFN, slot, sym 與實際時間
    t = sfn * FRAMEDUR + slot * SLOTDUR + sym * SYMDUR
    label = f"{sfn}/{sfn2}/{slot}/{sym}"
    # 儲存為 (sfn, slot, sym, time, power, preamble, label)
    rows.append((sfn, slot, sym, t, power, pre, label))

if not rows:
    raise SystemExit("找不到可解析的資料，請檢查 raw 內容格式")

# 依 SFN/slot/symbol 做排序，確保順序正確
rows = sorted(rows, key=lambda x: (x[0], x[1], x[2]))

# 建立陣列
SFN = np.array([r[0] for r in rows])
T = np.array([r[3] for r in rows])  # 若仍需時間可以使用
P = np.array([r[4] for r in rows])
PRE = np.array([r[5] for r in rows])
labels = [r[6] for r in rows]

# 將時間轉為相對時間（秒）從 0 開始，也可以轉為 ms（保留，但這次 x 軸會使用 SFN）
T0 = T[0]
Trel = T - T0
Tms = Trel * 1000.0

# 使用 SFN 作為 x 軸
X = SFN

plt.style.use('classic')  # 類似 MATLAB 的風格
fig, ax = plt.subplots(figsize=(11,4))

# 判定哪些為 failed / success (預設所有為 failed)
# 若要修改，請調整 failed_mask，例如: failed_mask = np.array([True, False, True, ...])
failed_mask = np.ones(len(P), dtype=bool)  # 這幾筆資料都是 failed
success_mask = ~failed_mask

# 連線顯示變化趨勢
ax.plot(X, P, color='gray', alpha=0.3, linewidth=1)

# 分別繪製 success (綠) 與 failed (紅)，以便顯示 legend
sc_success = None
if np.any(success_mask):
    sc_success = ax.scatter(X[success_mask], P[success_mask], color='green', edgecolors='k', s=90, label='success')
sc_failed = None
if np.any(failed_mask):
    sc_failed = ax.scatter(X[failed_mask], P[failed_mask], color='red', edgecolors='k', s=90, label='failed at RAR')

# 建立 legend（總是顯示紅/綠說明，即便綠色點不存在）
failed_handle = Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markeredgecolor='k', markersize=8)
success_handle = Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markeredgecolor='k', markersize=8)
ax.legend([failed_handle, success_handle], ['failed at RAR', 'success'], loc='best')

# 在每個點上標註 preamble 值（白底以提升可讀性）
for i, txt in enumerate(PRE):
    ax.annotate(str(txt), (X[i], P[i]), textcoords="offset points", xytext=(0,6), ha='center', fontsize=8,
                bbox=dict(boxstyle='round,pad=0.1', fc='white', alpha=0.8))

ax.set_xlabel('Time (SFN)')
ax.set_ylabel('TX power (dBm)')
ax.set_title('MTKUE TX power vs time (preamble index as color)')
ax.grid(True, which='both', linestyle='--', alpha=0.4)

# x 軸格式化（每 50 ms 標刻度，可依資料長度調整）
ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=10))

plt.tight_layout()
plt.savefig('MTKUE_tx_power_matlab_style.png', dpi=200)
print('圖已存為 MTKUE_tx_power_matlab_style.png')
plt.show()

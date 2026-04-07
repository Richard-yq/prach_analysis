import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# 設置字體與樣式
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Liberation Sans']
plt.rcParams['font.size'] = 12

# --- 參數設定 ---
slots_per_frame = 20  # 每個 Frame 有幾個 Slot (配合你的示意圖，畫密一點)
num_frames = 5        # 總共畫幾個 Frame
total_slots = slots_per_frame * num_frames
ro_offset = 19        # 設定 RO 在 Frame 中的哪個 Slot 發生 (第20個)

Ta = 2  # 攻擊者週期 (每 2 個 RO 攻擊一次)
j = 3   # 提前量 (UE 在第 3 個 RO 才到達)

fig, ax = plt.subplots(figsize=(14, 6))

# ==========================================
# 1. 繪製最上層：Frame 與 Slot 結構 (物理時間)
# ==========================================
y_frame = 5.5
y_slot = 3.0

# 畫 Frame
for f in range(num_frames):
    start_x = f * slots_per_frame
    ax.add_patch(patches.Rectangle((start_x, y_frame), slots_per_frame, 0.8, fill=False, edgecolor='black', lw=1.5))
    ax.text(start_x + slots_per_frame/2, y_frame + 0.4, f'Frame {f}', ha='center', va='center', fontweight='bold')

# 畫 Slot 與標示 RO (灰色)
ro_positions = []
for s in range(total_slots):
    is_ro = (s % slots_per_frame) == ro_offset
    facecolor = '#a0a0a0' if is_ro else 'white'
    ax.add_patch(patches.Rectangle((s, y_slot), 1, 0.5, facecolor=facecolor, edgecolor='black', lw=0.5))
    
    if is_ro:
        ro_positions.append(s)
        i_index = len(ro_positions) - 1
        # 標示 RO index (變數 i)
        ax.text(s + 0.5, y_slot + 1.0, f'RO #{i_index}\n($i={i_index}$)', ha='center', va='bottom', color='blue', fontweight='bold', fontsize=10)

# 標示 RO Interval
if len(ro_positions) >= 2:
    ax.annotate('', xy=(ro_positions[0]+0.5, y_slot+0.8), xytext=(ro_positions[1]+0.5, y_slot+0.8),
                arrowprops=dict(arrowstyle='<->', color='blue', lw=1.5))
    ax.text((ro_positions[0] + ro_positions[1])/2 + 0.5, y_slot+0.9, 'RO interval', ha='center', va='bottom', color='blue')

# ==========================================
# 2. 繪製 Attacker 排程 (嚴格對齊時間軸)
# ==========================================
y_atk = 1.5
ax.plot([-1, total_slots + 1], [y_atk, y_atk], color='black', lw=1)
ax.text(-2, y_atk+0.4, 'Attacker', ha='right', va='center', fontweight='bold', fontsize=12)

atk_ro_indices = [i for i in range(len(ro_positions)) if i % Ta == 0]
for idx in atk_ro_indices:
    pos = ro_positions[idx]
    ax.add_patch(patches.Rectangle((pos, y_atk), 1, 0.8, facecolor='#ff6666', edgecolor='black', lw=1.2))
    ax.text(pos + 0.5, y_atk + 0.4, 'MSG1', ha='center', va='center', fontsize=9, rotation=90)

# 標示 Ta
if len(atk_ro_indices) >= 2:
    pos1 = ro_positions[atk_ro_indices[0]]
    pos2 = ro_positions[atk_ro_indices[1]]
    ax.annotate('', xy=(pos1+0.5, y_atk+1.0), xytext=(pos2+0.5, y_atk+1.0),
                arrowprops=dict(arrowstyle='<->', color='#d62728', lw=2))
    ax.text((pos1+pos2)/2 + 0.5, y_atk+1.1, f'Attack Period ($T_a={Ta}$)', ha='center', va='bottom', color='#d62728', fontweight='bold')

# ==========================================
# 3. 繪製 UE 排程 (嚴格對齊時間軸)
# ==========================================
y_ue = 0.0
ax.plot([-1, total_slots + 2], [y_ue, y_ue], color='black', lw=1)
ax.text(-2, y_ue+0.4, 'Legitimate UE', ha='right', va='center', fontweight='bold', fontsize=12)

# UE 從第 j 個 RO 開始發送
for idx in range(j, len(ro_positions)):
    pos = ro_positions[idx]
    ax.add_patch(patches.Rectangle((pos, y_ue), 1, 0.8, facecolor='#66cc66', edgecolor='black', lw=1.2))
    ax.text(pos + 0.5, y_ue + 0.4, 'MSG1', ha='center', va='center', fontsize=9, rotation=90)

# 標示 j (從 RO#0 到 RO#j)
if j < len(ro_positions):
    pos0 = ro_positions[0]
    pos_j = ro_positions[j]
    ax.annotate('', xy=(pos0+0.5, y_ue+1.0), xytext=(pos_j+0.5, y_ue+1.0),
                arrowprops=dict(arrowstyle='<->', color='#ff7f0e', lw=2))
    ax.text((pos0+pos_j)/2 + 0.5, y_ue+1.1, f'Head Start ($j={j}$)', ha='center', va='bottom', color='#ff7f0e', fontweight='bold')

# ==========================================
# 4. 圖表美化
# ==========================================
ax.set_xlim(-20, total_slots + 4)
ax.set_ylim(-1.0, 7.5)

# 繪製絕對時間軸的箭頭
ax.annotate('Absolute Time (Slots)', xy=(total_slots + 3, -0.5), xytext=(-18, -0.5),
            arrowprops=dict(arrowstyle='->', color='black', lw=2), va='center', fontweight='bold')

# 隱藏預設座標軸
ax.axis('off')
plt.title(f'Physical Timeline of RACH Jamming (Example: $T_a={Ta}, j={j}$)', fontweight='bold', pad=20, fontsize=16)

plt.tight_layout()
plt.savefig('RO-draw2_corrected.png', dpi=300)
plt.show()
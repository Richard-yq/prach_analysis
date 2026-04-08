import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# 設置字體與樣式
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Liberation Sans']
plt.rcParams['font.size'] = 12

# --- 參數設定 ---
slots_per_frame = 20  
display_frames = 4  
ro_offset = 9  # 移出邊緣，改至中間 (第10個 slot) 以避免被誤以為 RO 都在固定結尾
gap_width = 8  # 每個 Frame 之間的空白斷層寬度
visual_stride = slots_per_frame + gap_width

# 預設繪圖內部依靠這些變數安排位置，文字會全面抽象化
Ta = 1
j = 2   

fig, ax = plt.subplots(figsize=(15, 8))

# ==========================================
# 1. 繪製最上層：Frame 與 Slot 結構 (加入斷層)
# ==========================================
y_frame = 5.5
y_slot = 3.0

ro_positions_logical = []
gap_centers = []

for k in range(display_frames):
    visual_start = k * visual_stride
    visual_end = visual_start + slots_per_frame
    
    # 計算這個 Frame 右側 Gap 的中心點 (最後一個 Frame 的右側為尾端延伸)
    cx = visual_end + gap_width / 2
    gap_centers.append(cx)
    
    # 畫出 Frame 邊框
    ax.add_patch(patches.Rectangle((visual_start, y_frame), slots_per_frame, 0.8, fill=False, edgecolor='black', lw=1.5))
    
    if k == 0:
        f_label = r'Frame $f$'
    elif k == 1:
        f_label = r'Frame $f+N$'
    else:
        f_label = rf'Frame $f+{k}N$'

    ax.text(visual_start + slots_per_frame/2, y_frame + 0.4, f_label, ha='center', va='center', fontweight='bold')
    
    # 不再畫滿 20 個 slot，單純在設定的位置畫一個代表性的 RO 區塊
    visual_s = visual_start + ro_offset
    ax.add_patch(patches.Rectangle((visual_s, y_slot), 1, 0.8, facecolor='#a0a0a0', edgecolor='black', lw=0.5))
    
    i_index = k
    ro_positions_logical.append((i_index, visual_s))
    if i_index == 0:
        ro_label = r'RO $i$'
    else:
        ro_label = rf'RO $i+{i_index}$'
    # 將文字標籤從原本的 y_slot + 1.0 上移至 1.4，讓出空間給箭頭
    ax.text(visual_s + 0.5, y_slot + 1.4, ro_label, 
            ha='center', va='bottom', color='blue', fontweight='bold', fontsize=11)

ro_logical_dict = {i: vis_s for i, vis_s in ro_positions_logical}

# RO Interval annotation
if 0 in ro_logical_dict and 1 in ro_logical_dict:
    pos_start = ro_logical_dict[0]
    pos_end = ro_logical_dict[1]
    # 箭頭上推至 y_slot+1.1，虛線從方塊頂部 (0.8) 拉升至箭頭高度 (1.1)
    ax.annotate('', xy=(pos_start, y_slot+1.1), xytext=(pos_end, y_slot+1.1),
                arrowprops=dict(arrowstyle='<->', color='blue', lw=1.5))
    ax.text((pos_start + pos_end)/2, y_slot+1.2, r'$\Delta t_{\mathrm{RO}}$', 
            ha='center', va='bottom', color='blue')
    ax.plot([pos_start, pos_start], [y_slot+0.8, y_slot+1.1], ls='--', color='blue', lw=1)
    ax.plot([pos_end, pos_end], [y_slot+0.8, y_slot+1.1], ls='--', color='blue', lw=1)

# ==========================================
# 2. 繪製 Attacker 排程 
# ==========================================
max_visual = (display_frames - 1) * visual_stride + slots_per_frame

y_atk = 1.5
# 第一底線 (Attacker)
ax.plot([-1, max_visual + gap_width], [y_atk, y_atk], color='black', lw=1, zorder=1)
ax.text(-2, y_atk+0.4, 'Attacker', ha='right', va='center', fontweight='bold', fontsize=12)

# 攻擊者在 i (0) 首次出現後，每隔 Ta 送出一次
atk_indices = [i for i in ro_logical_dict.keys() if i >= 0 and i % Ta == 0]
for i in atk_indices:
    if i in ro_logical_dict:
        vis_s = ro_logical_dict[i]
        ax.add_patch(patches.Rectangle((vis_s, y_atk), 1, 0.8, facecolor='#ff6666', edgecolor='black', lw=1.2))
        ax.text(vis_s + 0.5, y_atk + 0.4, 'MSG1', ha='center', va='center', fontsize=9, rotation=90)

if 0 in ro_logical_dict and Ta in ro_logical_dict:
    pos1 = ro_logical_dict[0]
    pos2 = ro_logical_dict[Ta]
    ax.annotate('', xy=(pos1, y_atk+1.0), xytext=(pos2, y_atk+1.0),
                arrowprops=dict(arrowstyle='<->', color='#d62728', lw=2))
    ax.text((pos1+pos2)/2, y_atk+1.1, r'$\Delta t_{\mathrm{Attack}}$', ha='center', va='bottom', color='#d62728', fontweight='bold')
    ax.plot([pos1, pos1], [y_atk+0.8, y_atk+1.0], ls='--', color='#d62728', lw=1)
    ax.plot([pos2, pos2], [y_atk+0.8, y_atk+1.0], ls='--', color='#d62728', lw=1)

# ==========================================
# 3. 繪製 UE 排程 
# ==========================================
y_ue = 0.0
# 第一底線 (UE)
ax.plot([-1, max_visual + gap_width], [y_ue, y_ue], color='black', lw=1, zorder=1)
ax.text(-2, y_ue+0.4, 'Commercial UE', ha='right', va='center', fontweight='bold', fontsize=12)

# UE 在 i+j (j) 出現後，後續的每個 RO 也都會有送出 MSG1 (模擬重傳或連續行為)
ue_indices = [i for i in ro_logical_dict.keys() if i >= j]
for i in ue_indices:
    if i in ro_logical_dict:
        vis_s = ro_logical_dict[i]
        ax.add_patch(patches.Rectangle((vis_s, y_ue), 1, 0.8, facecolor='#66cc66', edgecolor='black', lw=1.2))
        ax.text(vis_s + 0.5, y_ue + 0.4, 'MSG1', ha='center', va='center', fontsize=9, rotation=90)

if 0 in ro_logical_dict and j in ro_logical_dict:
    pos0 = ro_logical_dict[0]
    pos_j = ro_logical_dict[j]
    ax.annotate('', xy=(pos0, y_ue+1.0), xytext=(pos_j, y_ue+1.0),
                arrowprops=dict(arrowstyle='<->', color='#ff7f0e', lw=2))
    ax.text((pos0+pos_j)/2, y_ue+1.1, r'$\Delta t_{\mathrm{UE}}$', ha='center', va='bottom', color='#ff7f0e', fontweight='bold')
    ax.plot([pos0, pos0], [y_ue+0.8, y_ue+1.0], ls='--', color='#ff7f0e', lw=1)
    ax.plot([pos_j, pos_j], [y_ue+0.8, y_ue+1.0], ls='--', color='#ff7f0e', lw=1)

# ==========================================
# 4. 圖表美化 與 參數定義區
# ==========================================
y_time = -1.0
ax.set_xlim(-20, max_visual + gap_width + 4)
ax.set_ylim(-2.0, 10.5)

# 加入各個變數的定義說明
def_text = (
    r"$\mathbf{Definitions:}$" + "\n"
    r"$\Delta t_{\mathrm{RO}}$ : RO Interval ($N$ Frames)" + "\n"
    r"    where $N \in \{1, 2, 4, 8, 16\}$, determined by PRACH Configuration Index" + "\n"
    r"$\Delta t_{\mathrm{Attack}}$ : Attack Interval" + "\n"
    r"$\Delta t_{\mathrm{UE}}$ : Commercial UE Arrival Delay"
)
props = dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.9, edgecolor='gray')
ax.text(-18, 10.0, def_text, fontsize=14, linespacing=1.8, va='top', ha='left', bbox=props, zorder=5)

# -----------------
# 繪製 Gap Slashes (//) 及 ...
# -----------------
# 遍歷所有的 gap 中心 cx 
for cx in gap_centers:
    # 遮罩線條背景的白底
    ax.add_patch(patches.Rectangle((cx - 4, -2.0), 8, 9.5, facecolor='white', edgecolor='none', zorder=2))
    
    # 針對沒有連續橫線的地方 (Frame 與 Slot)，加入 ...
    # 根據反饋，移除了 y_atk 和 y_ue 的 ...，讓它們只依賴 //
    for level in [y_frame + 0.4, y_slot + 0.25]:
        ax.text(cx, level, '...', ha='center', va='center', fontweight='bold', color='gray', fontsize=16, zorder=3)

    # 在連續橫線的地方 (UE底線、Attacker底線、時間軸) 加入 //
    for level in [y_ue, y_atk, y_time]:
        h = 0.3
        d = 0.5
        ax.plot([cx - d, cx + d], [level - h, level + h], color='black', lw=1.5, zorder=3)
        ax.plot([cx - d + 0.8, cx + d + 0.8], [level - h, level + h], color='black', lw=1.5, zorder=3)

# Time axis (箭頭延伸跨過最後一個 ...)
final_cx = gap_centers[-1]
ax.annotate('Time', xy=(final_cx + 3, y_time), xytext=(-18, y_time),
            arrowprops=dict(arrowstyle='->', color='black', lw=2), va='center', fontweight='bold', zorder=1)

ax.axis('off')
plt.title('Definition of RACH Jamming Timeline Parameters', fontweight='bold', pad=20, fontsize=16)

plt.tight_layout()
plt.savefig('RO-draw2_corrected.png', dpi=300)
plt.show()
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# 設置字體與樣式
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Liberation Sans']
plt.rcParams['font.size'] = 12

# --- 參數設定 ---
slots_per_frame = 20  
display_frames = [0, 1, 2, 3, 1023]  # 加入 1023 做縮時圖
ro_offset = 19  
N = 1  # RO 週期為 N 個 Frame

Ta = 2  
j = 3   

fig, ax = plt.subplots(figsize=(15, 6))

gap_logical_start = 4 * slots_per_frame  
gap_logical_end = 1023 * slots_per_frame  
gap_visual_width = 8
gap_visual_start = gap_logical_start
gap_visual_end = gap_visual_start + gap_visual_width

def get_visual_x(logical_x):
    if logical_x <= gap_logical_start:
        return logical_x
    elif logical_x >= gap_logical_end:
        return logical_x - gap_logical_end + gap_visual_end
    else:
        return gap_visual_start + gap_visual_width / 2

# ==========================================
# 1. 繪製最上層：Frame 與 Slot 結構 (物理時間)
# ==========================================
y_frame = 5.5
y_slot = 3.0

ro_positions_logical = []

for f in display_frames:
    logical_start = f * slots_per_frame
    visual_start = get_visual_x(logical_start)
    
    # Draw Frame box
    ax.add_patch(patches.Rectangle((visual_start, y_frame), slots_per_frame, 0.8, fill=False, edgecolor='black', lw=1.5))
    ax.text(visual_start + slots_per_frame/2, y_frame + 0.4, f'Frame {f}', ha='center', va='center', fontweight='bold')
    
    # Draw Slots for this frame
    for s_in_frame in range(slots_per_frame):
        logical_s = logical_start + s_in_frame
        visual_s = get_visual_x(logical_s)
        
        is_ro = (s_in_frame == ro_offset) and (f % N == 0)
        facecolor = '#a0a0a0' if is_ro else 'white'
        ax.add_patch(patches.Rectangle((visual_s, y_slot), 1, 0.5, facecolor=facecolor, edgecolor='black', lw=0.5))
        
        if is_ro:
            i_index = f // N
            ro_positions_logical.append((i_index, logical_s))
            ax.text(visual_s + 0.5, y_slot + 1.0, f'RO #{i_index}\n($i={i_index}$)', 
                    ha='center', va='bottom', color='blue', fontweight='bold', fontsize=10)

ro_logical_dict = {i: log_s for i, log_s in ro_positions_logical}

# RO Interval annotation (between RO#0 and RO#1)
if 0 in ro_logical_dict and 1 in ro_logical_dict:
    pos_start = get_visual_x(ro_logical_dict[0])
    pos_end = get_visual_x(ro_logical_dict[1])
    ax.annotate('', xy=(pos_start, y_slot+0.8), xytext=(pos_end, y_slot+0.8),
                arrowprops=dict(arrowstyle='<->', color='blue', lw=1.5))
    # 將標籤文字依要求調整為 N 個 Frame
    ax.text((pos_start + pos_end)/2, y_slot+0.9, r'$\Delta t_{\mathrm{RO}}$', 
            ha='center', va='bottom', color='blue')
    ax.plot([pos_start, pos_start], [y_slot+0.5, y_slot+0.8], ls='--', color='blue', lw=1)
    ax.plot([pos_end, pos_end], [y_slot+0.5, y_slot+0.8], ls='--', color='blue', lw=1)

# ==========================================
# 計算最大座標
# ==========================================
max_logical = max(display_frames) * slots_per_frame + slots_per_frame
max_visual = get_visual_x(max_logical)

# ==========================================
# 2. 繪製 Attacker 排程 
# ==========================================
y_atk = 1.5
ax.plot([-1, max_visual + 1], [y_atk, y_atk], color='black', lw=1, zorder=1)
ax.text(-2, y_atk+0.4, 'Attacker', ha='right', va='center', fontweight='bold', fontsize=12)

atk_indices = [i for i in ro_logical_dict.keys() if i % Ta == 0]
for i in atk_indices:
    log_s = ro_logical_dict[i]
    vis_s = get_visual_x(log_s)
    ax.add_patch(patches.Rectangle((vis_s, y_atk), 1, 0.8, facecolor='#ff6666', edgecolor='black', lw=1.2))
    ax.text(vis_s + 0.5, y_atk + 0.4, 'MSG1', ha='center', va='center', fontsize=9, rotation=90)

if len(atk_indices) >= 2:
    idx0, idx1 = atk_indices[0], atk_indices[1]
    pos1 = get_visual_x(ro_logical_dict[idx0])
    pos2 = get_visual_x(ro_logical_dict[idx1])
    ax.annotate('', xy=(pos1, y_atk+1.0), xytext=(pos2, y_atk+1.0),
                arrowprops=dict(arrowstyle='<->', color='#d62728', lw=2))
    ax.text((pos1+pos2)/2, y_atk+1.1, r'$\Delta t_{\mathrm{Attack}}$', ha='center', va='bottom', color='#d62728', fontweight='bold')
    ax.plot([pos1, pos1], [y_atk+0.8, y_atk+1.0], ls='--', color='#d62728', lw=1)
    ax.plot([pos2, pos2], [y_atk+0.8, y_atk+1.0], ls='--', color='#d62728', lw=1)

# ==========================================
# 3. 繪製 UE 排程 
# ==========================================
y_ue = 0.0
ax.plot([-1, max_visual + 2], [y_ue, y_ue], color='black', lw=1, zorder=1)
ax.text(-2, y_ue+0.4, 'Commercial UE', ha='right', va='center', fontweight='bold', fontsize=12)

ue_indices = [i for i in ro_logical_dict.keys() if i >= j]
for i in ue_indices:
    log_s = ro_logical_dict[i]
    vis_s = get_visual_x(log_s)
    facecolor = '#66cc66' if i == j else '#ffcc66'  # 區分首發跟後續？依舊統一用綠色即可
    ax.add_patch(patches.Rectangle((vis_s, y_ue), 1, 0.8, facecolor='#66cc66', edgecolor='black', lw=1.2))
    ax.text(vis_s + 0.5, y_ue + 0.4, 'MSG1', ha='center', va='center', fontsize=9, rotation=90)

if 0 in ro_logical_dict and j in ro_logical_dict:
    pos0 = get_visual_x(ro_logical_dict[0])
    pos_j = get_visual_x(ro_logical_dict[j])
    ax.annotate('', xy=(pos0, y_ue+1.0), xytext=(pos_j, y_ue+1.0),
                arrowprops=dict(arrowstyle='<->', color='#ff7f0e', lw=2))
    ax.text((pos0+pos_j)/2, y_ue+1.1, r'$\Delta t_{\mathrm{UE}}$', ha='center', va='bottom', color='#ff7f0e', fontweight='bold')
    ax.plot([pos0, pos0], [y_ue+0.8, y_ue+1.0], ls='--', color='#ff7f0e', lw=1)
    ax.plot([pos_j, pos_j], [y_ue+0.8, y_ue+1.0], ls='--', color='#ff7f0e', lw=1)

# ==========================================
# 縮時斷裂符號 (Break Lines)
# ==========================================
cx = gap_visual_start + gap_visual_width / 2

y_time = -1.0

# 用白色塊遮住背後穿過的實線
ax.add_patch(patches.Rectangle((gap_visual_start, -2.0), gap_visual_width, 9.5, facecolor='white', edgecolor='none', zorder=2))

# 統一在各個有方塊的層級放上省略號 ... 以保持視覺一致性
for text_y in [y_frame + 0.4, y_slot + 0.25]:
    ax.text(cx, text_y, '...', ha='center', va='center', fontweight='bold', color='gray', fontsize=16, zorder=3)

# 在跨越斷層的連續線上繪製平行的雙斜線 (//) 表示斷開
for level in [y_ue, y_atk, y_time]:
    h = 0.3
    d = 0.5
    ax.plot([cx - d, cx + d], [level - h, level + h], color='black', lw=1.5, zorder=3)
    ax.plot([cx - d + 0.8, cx + d + 0.8], [level - h, level + h], color='black', lw=1.5, zorder=3)

# ==========================================
# 4. 圖表美化
# ==========================================
ax.set_xlim(-20, max_visual + 4)
ax.set_ylim(-2.0, 7.5)

# 繪製絕對時間軸的箭頭，將 zorder 設為 1 讓它可以被白色遮罩遮斷
ax.annotate('Absolute Time (ms)', xy=(max_visual + 3, y_time), xytext=(-18, y_time),
            arrowprops=dict(arrowstyle='->', color='black', lw=2), va='center', fontweight='bold', zorder=1)

ax.axis('off')
plt.title(f'Physical Timeline of RACH Jamming (Example: $T_a={Ta}, j={j}$)', fontweight='bold', pad=20, fontsize=16)

plt.tight_layout()
plt.savefig('RO-draw2_corrected.png', dpi=300)
plt.show()
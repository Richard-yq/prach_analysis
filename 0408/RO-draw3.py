import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# 設置字體與樣式
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Liberation Sans']
plt.rcParams['font.size'] = 12

# --- 參數設定 ---
display_ROs = 5  # 我們改為畫 5 個連續的 RO 塊
ro_width = 1.0
gap_width = 3.0  # RO 與 RO 之間的極小留白
visual_stride = ro_width + gap_width

# 預設繪圖內部依靠這些變數安排位置
Ta = 1
j = 2   

fig, ax = plt.subplots(figsize=(10, 5))

# ==========================================
# 1. 繪製最上層：僅保留 RO 塊 (完全移除 Frame)
# ==========================================
y_slot = 3.0

ro_positions_logical = []
gap_centers = []

for k in range(display_ROs):
    visual_s = k * visual_stride
    
    # 計算這個 RO 右側 Gap 的中心點
    cx = visual_s + ro_width + gap_width / 2
    gap_centers.append(cx)
    
    # 畫出代表 RO 的方塊 (依需求加高至 1.2)
    ax.add_patch(patches.Rectangle((visual_s, y_slot), ro_width, 1.2, facecolor='#a0a0a0', edgecolor='black', lw=1.0))
    
    # 依賴 UE 出現的設定作為原點 i，而不是左邊第一個框
    i_index = k - j
    ro_positions_logical.append((i_index, visual_s))
    if i_index == 0:
        ro_label = r'RO $i$'
    elif i_index < 0:
        ro_label = rf'RO $i-{abs(i_index)}$'
    else:
        ro_label = rf'RO $i+{i_index}$'
        
    ax.text(visual_s + ro_width/2, y_slot + 2.1, ro_label, 
            ha='center', va='bottom', color='blue', fontweight='bold', fontsize=11)

ro_logical_dict = {i: vis_s for i, vis_s in ro_positions_logical}

# RO Interval annotation (以第一個和第二個塊為主)
first_idx = -j
next_idx = -j + 1
if first_idx in ro_logical_dict and next_idx in ro_logical_dict:
    pos_start = ro_logical_dict[first_idx]
    pos_end = ro_logical_dict[next_idx]
    # 箭頭標示推昇至方塊上方 (1.5)
    ax.annotate('', xy=(pos_start, y_slot+1.5), xytext=(pos_end, y_slot+1.5),
                arrowprops=dict(arrowstyle='<->', color='blue', lw=1.5))
    ax.text((pos_start + pos_end)/2, y_slot+1.6, r'RO interval', 
            ha='center', va='bottom', color='blue', fontweight='bold')
    ax.plot([pos_start, pos_start], [y_slot+1.2, y_slot+1.5], ls='--', color='blue', lw=1)
    ax.plot([pos_end, pos_end], [y_slot+1.2, y_slot+1.5], ls='--', color='blue', lw=1)

# ==========================================
# 2. 繪製 Attacker 排程 
# ==========================================
max_visual = (display_ROs - 1) * visual_stride + ro_width

y_atk = 1.5
# 第一底線 (Attacker)
ax.plot([-1, max_visual + gap_width], [y_atk, y_atk], color='black', lw=1, zorder=1)
ax.text(-2, y_atk+0.4, 'Attacker', ha='right', va='center', fontweight='bold', fontsize=12)

# 攻擊者在 -j 首次出現後，每隔 Ta 送出一次
atk_indices = [i for i in ro_logical_dict.keys() if i >= -j and (i - (-j)) % Ta == 0]
for i in atk_indices:
    if i in ro_logical_dict:
        vis_s = ro_logical_dict[i]
        ax.add_patch(patches.Rectangle((vis_s, y_atk), ro_width, 0.8, facecolor='#ff6666', edgecolor='black', lw=1.2))
        ax.text(vis_s + ro_width/2, y_atk + 0.4, 'MSG1', ha='center', va='center', fontsize=9, rotation=90)

if -j in ro_logical_dict and (-j + Ta) in ro_logical_dict:
    pos1 = ro_logical_dict[-j]
    pos2 = ro_logical_dict[-j + Ta]
    ax.annotate('', xy=(pos1, y_atk+1.0), xytext=(pos2, y_atk+1.0),
                arrowprops=dict(arrowstyle='<->', color='#d62728', lw=2))
    ax.text((pos1+pos2)/2, y_atk+1.1, r'$\Delta t_{\mathrm{Attack}}$', ha='center', va='bottom', color='#d62728', fontweight='bold')
    ax.plot([pos1, pos1], [y_atk+0.8, y_atk+1.0], ls='--', color='#d62728', lw=1)
    ax.plot([pos2, pos2], [y_atk+0.8, y_atk+1.0], ls='--', color='#d62728', lw=1)

# ==========================================
# 3. 繪製 UE 排程 
# ==========================================
y_ue = 0.0
# 第二底線 (UE)
ax.plot([-1, max_visual + gap_width], [y_ue, y_ue], color='black', lw=1, zorder=1)
ax.text(-2, y_ue+0.4, 'Commercial UE', ha='right', va='center', fontweight='bold', fontsize=12)

# UE 在 0 出現後，後續的每個 RO 也都會有送出 MSG1
ue_indices = [i for i in ro_logical_dict.keys() if i >= 0]
for i in ue_indices:
    if i in ro_logical_dict:
        vis_s = ro_logical_dict[i]
        ax.add_patch(patches.Rectangle((vis_s, y_ue), ro_width, 0.8, facecolor='#66cc66', edgecolor='black', lw=1.2))
        ax.text(vis_s + ro_width/2, y_ue + 0.4, 'MSG1', ha='center', va='center', fontsize=9, rotation=90)

if -j in ro_logical_dict and 0 in ro_logical_dict:
    pos0 = ro_logical_dict[-j]
    pos_j = ro_logical_dict[0]
    ax.annotate('', xy=(pos0, y_ue+1.0), xytext=(pos_j, y_ue+1.0),
                arrowprops=dict(arrowstyle='<->', color='#ff7f0e', lw=2))
    ax.text((pos0+pos_j)/2, y_ue+1.1, r'$\Delta t_{\mathrm{UE}}$', ha='center', va='bottom', color='#ff7f0e', fontweight='bold')
    ax.plot([pos0, pos0], [y_ue+0.8, y_ue+1.0], ls='--', color='#ff7f0e', lw=1)
    ax.plot([pos_j, pos_j], [y_ue+0.8, y_ue+1.0], ls='--', color='#ff7f0e', lw=1)

# ==========================================
# 4. 圖表美化
# ==========================================
ax.set_xlim(-6, max_visual + gap_width + 2)
# 把頂部推高一點點避免藍色的 i 標籤吃緊
ax.set_ylim(-2.0, 5.5)

y_time = -1.0

# -----------------
# 繪製 Gap Slashes (//) 及 ...
# -----------------
# 遍歷所有的 gap 中心 cx 
for cx in gap_centers:
    # 遮罩線條背景的白底，寬度設為稍微覆蓋
    ax.add_patch(patches.Rectangle((cx - 1.5, -2.0), 3.0, 7.5, facecolor='white', edgecolor='none', zorder=2))
    
    # 在 RO 層，加入 ...
    # 配合高度 1.2，將 ... 推移到 Y=0.6 處
    ax.text(cx, y_slot + 0.6, '...', ha='center', va='center', fontweight='bold', color='gray', fontsize=16, zorder=3)

    # 在連續橫線的地方 (UE底線、Attacker底線、時間軸) 加入 //
    for level in [y_ue, y_atk, y_time]:
        h = 0.2
        d = 0.4
        ax.plot([cx - d, cx + d], [level - h, level + h], color='black', lw=1.5, zorder=3)
        ax.plot([cx - d + 0.6, cx + d + 0.6], [level - h, level + h], color='black', lw=1.5, zorder=3)

# Time axis (箭頭延伸跨過最後一個 ...)
final_cx = gap_centers[-1]
# 文字起點拉近設定在 x = -5
ax.annotate('Time', xy=(final_cx + 1, y_time), xytext=(-5, y_time),
            arrowprops=dict(arrowstyle='->', color='black', lw=2), ha='left', va='center', fontweight='bold', zorder=1)

ax.axis('off')
plt.title('Definition of RACH Jamming Timeline Parameters', fontweight='bold', pad=20, fontsize=16)

plt.tight_layout()
plt.savefig('RO-draw3_corrected.png', dpi=300)
plt.show()
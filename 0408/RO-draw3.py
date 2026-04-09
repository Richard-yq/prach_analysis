import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as path_effects
import numpy as np

# 設置字體與樣式
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Liberation Sans', 'Helvetica']
plt.rcParams['font.size'] = 12

# --- 參數設定 ---
display_ROs = 7  # 我們改為畫 7 個連續的 RO 塊
ro_width = 1.0
ro_height = 1.2
gap_width = 3.0  # RO 與 RO 之間的極小留白
visual_stride = ro_width + gap_width

# 預設繪圖內部依靠這些變數安排位置
Ta = 1
j = 3   

fig, ax = plt.subplots(figsize=(15, 6))

# 定義陰影效果，讓方塊更有立體層次感
shadow_effect = [path_effects.SimplePatchShadow(offset=(1.5, -1.5), shadow_rgbFace='#b0b0b0', alpha=0.4),
                 path_effects.Normal()]

# 分配更寬裕的 Y 軸高度給不同層級，避免互相擠壓
y_ue = 0.0
y_atk = 3.0
y_slot = 6.0

# ==========================================
# 1. 繪製最上層：僅保留 RO 塊 (完全移除 Frame)
# ==========================================
ro_positions_logical = []
gap_centers = []

for k in range(display_ROs):
    visual_s = k * visual_stride
    cx = visual_s + ro_width + gap_width / 2
    gap_centers.append(cx)
    
    # 畫出代表 RO 的方塊 (height = ro_height)
    rect = patches.Rectangle((visual_s, y_slot), ro_width, ro_height, 
                             facecolor='#E8EDF2', edgecolor='#7C93A7', lw=1.5)
    rect.set_path_effects(shadow_effect)
    ax.add_patch(rect)
    
    i_index = k - j
    ro_positions_logical.append((i_index, visual_s))
    if i_index == 0:
        ro_label = r'RO $i$'
    elif i_index < 0:
        ro_label = rf'RO $i-{abs(i_index)}$'
    else:
        ro_label = rf'RO $i+{i_index}$'
        
    ax.text(visual_s + ro_width/2, y_slot + ro_height + 0.3, ro_label, 
            ha='center', va='bottom', color='#264E70', fontweight='bold', fontsize=11)

ro_logical_dict = {i: vis_s for i, vis_s in ro_positions_logical}

# RO Interval annotation 
first_idx = -j
next_idx = -j + 1
if first_idx in ro_logical_dict and next_idx in ro_logical_dict:
    pos_start = ro_logical_dict[first_idx]
    pos_end = ro_logical_dict[next_idx]
    arr_y = y_slot + ro_height + 1.2
    
    ax.annotate('', xy=(pos_start, arr_y), xytext=(pos_end, arr_y),
                arrowprops=dict(arrowstyle='<|-|>', color='#264E70', lw=1.8, mutation_scale=12))
    ax.text((pos_start + pos_end)/2, arr_y + 0.1, r'RO interval', 
            ha='center', va='bottom', color='#264E70', fontweight='bold', fontsize=11)
    ax.plot([pos_start, pos_start], [y_slot + ro_height + 0.1, arr_y], ls=':', color='#264E70', lw=1.2)
    ax.plot([pos_end, pos_end], [y_slot + ro_height + 0.1, arr_y], ls=':', color='#264E70', lw=1.2)

# ==========================================
# 2. 繪製 Attacker 排程 
# ==========================================
max_visual = (display_ROs - 1) * visual_stride + ro_width

# 第一底線 (Attacker)
ax.plot([-1, max_visual + gap_width], [y_atk, y_atk], color='#404040', lw=1.2, zorder=1)
ax.text(-1.5, y_atk + ro_height/2, 'Attacker', ha='right', va='center', fontweight='bold', fontsize=12, color='#A63D40')

atk_indices = [i for i in ro_logical_dict.keys() if i >= -j and (i - (-j)) % Ta == 0]
for i in atk_indices:
    if i in ro_logical_dict:
        vis_s = ro_logical_dict[i]
        # 與 RO 一模一樣的高度與寬度設定
        rect = patches.Rectangle((vis_s, y_atk), ro_width, ro_height, 
                                 facecolor='#FAD4D4', edgecolor='#D9534F', lw=1.5)
        rect.set_path_effects(shadow_effect)
        ax.add_patch(rect)
        ax.text(vis_s + ro_width/2, y_atk + ro_height/2, 'MSG1', ha='center', va='center', 
                fontsize=10, rotation=90, color='#900000', fontweight='bold')

if -j in ro_logical_dict and (-j + Ta) in ro_logical_dict:
    pos1 = ro_logical_dict[-j]
    pos2 = ro_logical_dict[-j + Ta]
    arr_y = y_atk + ro_height + 0.4
    ax.annotate('', xy=(pos1, arr_y), xytext=(pos2, arr_y),
                arrowprops=dict(arrowstyle='<|-|>', color='#D9534F', lw=1.8, mutation_scale=12))
    ax.text((pos1+pos2)/2, arr_y + 0.1, r'1 RO interval', ha='center', va='bottom', color='#D9534F', fontweight='bold')
    ax.plot([pos1, pos1], [y_atk + ro_height + 0.1, arr_y], ls=':', color='#D9534F', lw=1.2)
    ax.plot([pos2, pos2], [y_atk + ro_height + 0.1, arr_y], ls=':', color='#D9534F', lw=1.2)

# ==========================================
# 3. 繪製 UE 排程 
# ==========================================
# 第二底線 (UE)
ax.plot([-1, max_visual + gap_width], [y_ue, y_ue], color='#404040', lw=1.2, zorder=1)
ax.text(-1.5, y_ue + ro_height/2, 'Commercial UE', ha='right', va='center', fontweight='bold', fontsize=12, color='#388E3C')

ue_indices = [i for i in ro_logical_dict.keys() if i >= 0]
for i in ue_indices:
    if i in ro_logical_dict:
        vis_s = ro_logical_dict[i]
        # 與 RO 一模一樣的高度與寬度設定
        rect = patches.Rectangle((vis_s, y_ue), ro_width, ro_height, 
                                 facecolor='#DDF0D6', edgecolor='#66BB6A', lw=1.5)
        rect.set_path_effects(shadow_effect)
        ax.add_patch(rect)
        ax.text(vis_s + ro_width/2, y_ue + ro_height/2, 'MSG1', ha='center', va='center', 
                fontsize=10, rotation=90, color='#1B5E20', fontweight='bold')

if -j in ro_logical_dict and 0 in ro_logical_dict:
    pos0 = ro_logical_dict[-j]
    pos_j = ro_logical_dict[0]
    arr_y = y_ue + ro_height + 0.4
    ax.annotate('', xy=(pos0, arr_y), xytext=(pos_j, arr_y),
                arrowprops=dict(arrowstyle='<|-|>', color='#F57C00', lw=1.8, mutation_scale=12))
    ax.text((pos0+pos_j)/2, arr_y + 0.1, r'3 RO intervals', ha='center', va='bottom', color='#F57C00', fontweight='bold')
    ax.plot([pos0, pos0], [y_ue + ro_height + 0.1, arr_y], ls=':', color='#F57C00', lw=1.2)
    ax.plot([pos_j, pos_j], [y_ue + ro_height + 0.1, arr_y], ls=':', color='#F57C00', lw=1.2)

# ==========================================
# 4. 圖表美化
# ==========================================
ax.set_xlim(-5, max_visual + gap_width + 1)
ax.set_ylim(-1.5, y_slot + ro_height + 2.5)

y_time = -1.0

# -----------------
# 繪製 Gap Slashes (//) 及 ...
# -----------------
for cx in gap_centers:
    # 遮罩線條背景的白底
    bg_rect = patches.Rectangle((cx - 1.5, -2.0), 3.0, 12.0, facecolor='white', edgecolor='none', zorder=2)
    ax.add_patch(bg_rect)
    
    # 在 RO 層，加入 ...
    ax.text(cx, y_slot + ro_height/2, '...', ha='center', va='center', fontweight='bold', color='#B0B0B0', fontsize=18, zorder=3)

    # 在連續橫線的地方 (UE底線、Attacker底線、時間軸) 加入乾淨的 //
    for level in [y_ue, y_atk, y_time]:
        h = 0.25
        d = 0.25
        # 第一條斜線
        ax.plot([cx - d - 0.1, cx + d - 0.1], [level - h, level + h], color='#606060', lw=1.5, zorder=3)
        # 第二條斜線
        ax.plot([cx - d + 0.3, cx + d + 0.3], [level - h, level + h], color='#606060', lw=1.5, zorder=3)

# Time axis (箭頭延伸跨過最後一個 ...)
final_cx = gap_centers[-1]
ax.annotate('Time', xy=(final_cx + 1, y_time), xytext=(-4, y_time),
            arrowprops=dict(arrowstyle='-|>', color='#404040', lw=2, mutation_scale=15), 
            ha='left', va='center', fontweight='bold', zorder=1, color='#404040')

ax.axis('off')

# Title 
plt.title('Definition of RACH Jamming Timeline Parameters', 
          fontweight='bold', pad=20, fontsize=18, color='#303030')

plt.tight_layout()
plt.savefig('RO-draw3_corrected.png', dpi=300, bbox_inches='tight')
plt.show()
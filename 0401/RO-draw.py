import matplotlib.pyplot as plt
import matplotlib.patches as patches

# =====================================================================
# 參數設置區 (可調整)
# =====================================================================
TOTAL_ROS = 7               # 總共有幾個 RO 區間 (預設 10)

# 第二層：紅色 MSG1 的設置
RED_MSG1_INTERVAL = 1        # 每隔幾格 RO 出現一次紅色 MSG1 (例如 2 代表每 2 個 RO 區間出現一次)
RED_MSG1_OFFSET = 0          # 從第幾格 RO 開始出現紅色 MSG1 (0 表示對齊 RO#1，1 表示對齊 RO#2...)

# 第三層：綠色 MSG1 的設置
GREEN_MSG1_INTERVAL = 1      # 每隔幾格 RO 出現一次綠色 MSG1 
GREEN_MSG1_OFFSET = 3        # 從第幾格 RO 開始出現綠色 MSG1 (1 表示對齊 RO#2...)
# =====================================================================

def draw_timing_diagram():
    fig, ax = plt.subplots(figsize=(12, 4))
    
    # 隱藏外框 (上、右、左)，只保留底部的 X 軸
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    # 設定 Y 軸的三個層級高度
    layer_ro_y = 2
    layer_red_y = 1
    layer_green_y = 0
    
    # 方塊的寬度與高度 (每個區間的寬度為 1，0.8 代表方塊佔 80% 的寬度，兩側留白)
    box_width = 0.8
    box_height = 0.6
    
    # 設定 X 軸與 Y 軸的範圍
    ax.set_xlim(0, TOTAL_ROS)
    ax.set_ylim(-0.5, 3)
    
    # 設定 Y 軸刻度的顯示名稱與位置，讓它恰好對齊方塊的中心
    ax.set_yticks([layer_green_y + box_height/2, 
                   layer_red_y + box_height/2, 
                   layer_ro_y + box_height/2])
    ax.set_yticklabels(["UE", "Attacker", "RO"])
    ax.tick_params(axis='y', length=0) # 隱藏 Y 軸的刻度線
    
    # 設定 X 軸的格線，對齊每一個區間的邊界
    ax.set_xticks(range(TOTAL_ROS + 1))
    ax.set_xticklabels([])  # 隱藏 X 軸的數字
    ax.grid(True, axis='x', linestyle='--', alpha=0.5)
    
    # 開始繪製每一欄 (區間)
    for i in range(TOTAL_ROS):
        # x 座標加上偏移，使得方塊置中於每個寬度為 1 的區間內
        x = i + (1 - box_width) / 2
        
        # 第一層：繪製 RO 方塊 (白色)
        rect_ro = patches.Rectangle((x, layer_ro_y), box_width, box_height, 
                                    linewidth=1.5, edgecolor='black', facecolor='white')
        ax.add_patch(rect_ro)
        ax.text(x + box_width/2, layer_ro_y + box_height/2, f"RO#{i+1}", 
                ha='center', va='center', fontsize=10, weight='bold')

        # 第二層：繪製紅色的 MSG1
        # 判斷當前的 RO 是否滿足 紅色 MSG1 的起始位置與間隔
        if i >= RED_MSG1_OFFSET and (i - RED_MSG1_OFFSET) % RED_MSG1_INTERVAL == 0:
            rect_red = patches.Rectangle((x, layer_red_y), box_width, box_height, 
                                         linewidth=1.5, edgecolor='black', facecolor='#ff6666') # 紅色
            ax.add_patch(rect_red)
            ax.text(x + box_width/2, layer_red_y + box_height/2, "MSG1", 
                    ha='center', va='center', fontsize=10, weight='bold', color='white')

        # 第三層：繪製綠色的 MSG1
        # 判斷當前的 RO 是否滿足 綠色 MSG1 的起始位置與間隔
        if i >= GREEN_MSG1_OFFSET and (i - GREEN_MSG1_OFFSET) % GREEN_MSG1_INTERVAL == 0:
            rect_green = patches.Rectangle((x, layer_green_y), box_width, box_height, 
                                           linewidth=1.5, edgecolor='black', facecolor='#66cc66') # 綠色
            ax.add_patch(rect_green)
            ax.text(x + box_width/2, layer_green_y + box_height/2, "MSG1", 
                    ha='center', va='center', fontsize=10, weight='bold', color='white')

    ax.set_xlabel("Time (Slots)", fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    # 儲存與顯示圖片
    output_filename = "RO_MSG1_diagram.png"
    plt.savefig(output_filename, dpi=300)
    print(f"圖片已產生並儲存為: {output_filename}")
    plt.show()

if __name__ == "__main__":
    draw_timing_diagram()

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# =====================================================================
# 繪製美觀的系統架構圖 (自動儲存為 proposed_setup_diagram.png)
# =====================================================================

def create_block_diagram():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(-1.5, 8.5)
    ax.axis('off')  # 隱藏座標軸
    
    # 輔助函式：繪製帶有陰影的圓角方塊
    def draw_box(x, y, w, h, text, bg_color, border_color, text_color, fontsize=13, weight='bold'):
        # 陰影
        shadow = patches.FancyBboxPatch((x+0.1, y-0.1), w, h,
                                        boxstyle="round,pad=0.1,rounding_size=0.2",
                                        facecolor='black', alpha=0.15, edgecolor='none')
        ax.add_patch(shadow)
        
        # 主方塊
        box = patches.FancyBboxPatch((x, y), w, h,
                                     boxstyle="round,pad=0.1,rounding_size=0.2",
                                     facecolor=bg_color, edgecolor=border_color, linewidth=2)
        ax.add_patch(box)
        
        # 顯示文字
        ax.text(x + w/2, y + h/2, text, ha='center', va='center',
                color=text_color, fontsize=fontsize, weight=weight, zorder=10)

    # 輔助函式：繪製虛線群組外框
    def draw_group_box(x, y, w, h, label):
        box = patches.FancyBboxPatch((x, y), w, h,
                                     boxstyle="round,pad=0.2,rounding_size=0.2",
                                     facecolor='#F8F9FA', alpha=0.6, 
                                     edgecolor='#9CA3AF', linewidth=2, linestyle='--')
        ax.add_patch(box)
        # 群組標題置於框的上方
        ax.text(x + w/2, y + h + 0.5, label, ha='center', va='center',
                color='#4B5563', fontsize=14, weight='bold')

    # 1. 繪製群組外框
    # 右側：gNB 系統
    draw_group_box(7.5, 2.0, 4.0, 5.0, "Next Generation NodeB (gNB)")
    # 左下：Attacker 系統
    draw_group_box(0.5, -0.5, 4.0, 4.5, "Attacker Setup")
    
    # 2. 繪製有線連接 (Wired / USB / Ethernet)
    # gNB 內部有線連接 (USRP to OAI gNB)
    ax.plot([9.5, 9.5], [4.0, 5.0], color='#4B5563', linewidth=3.5, zorder=1)
    # Attacker 內部有線連接 (Modified UE to USRP)
    ax.plot([2.5, 2.5], [1.5, 2.5], color='#4B5563', linewidth=3.5, zorder=1)
    
    # 3. 繪製各個節點 (Nodes)
    # gNB 系統的元件
    draw_box(8.0, 2.5, 3.0, 1.5, "USRP\n(SDR Hardware)", '#E8F5E9', '#388E3C', '#1B5E20')
    draw_box(8.0, 5.0, 3.0, 1.5, "OAI gNB / srsRAN\n(Base Station Software)", '#E8F5E9', '#388E3C', '#1B5E20')
    
    # Attacker 系統的元件
    draw_box(1.0, 2.5, 3.0, 1.5, "USRP\n(SDR Hardware)", '#FFEBEE', '#D32F2F', '#B71C1C')
    draw_box(1.0, 0.0, 3.0, 1.5, "Modified OAI nrUE\n(Attacker Software)", '#FFEBEE', '#D32F2F', '#B71C1C')
    
    # COTS UE 元件 (左上)
    draw_box(1.0, 5.0, 3.0, 1.5, "COTS UE\n(Legitimate User)", '#E3F2FD', '#1976D2', '#0D47A1')
    
    # 4. 繪製無線天線連接線 (Wireless Links)
    def draw_wireless_link(start, end, color, label, label_pos='top', rad=0.0):
        # 使用 annotate 繪製漂亮的弧形虛線箭頭
        ax.annotate('', xy=end, xytext=start,
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=2.5, linestyle='--',
                                    connectionstyle=f"arc3,rad={rad}", mutation_scale=20))
        
        # 決定文字的中心點座標 (簡單的曲線中點估算)
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2
        
        if rad != 0:
            # 微調標籤的曲線偏移
            mid_y += rad * 2
            
        mid_y += 0.4 if label_pos == 'top' else -0.4
        
        # 添加標籤文字，加上白色半透明背景以便閱讀
        ax.text(mid_x, mid_y, label, ha='center', va='center', color=color, 
                fontsize=12, weight='bold',
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.9, pad=2))

    # 合法連接: COTS UE (4.2, 5.75) 連接到 gNB USRP (7.8, 3.5)
    draw_wireless_link((4.2, 5.75), (7.8, 3.5), '#1976D2', "Legitimate Request\n(MSG1)", 'top', rad=0.2)
    
    # 攻擊者連接: Attacker USRP (4.2, 3.25) 連接到 gNB USRP (7.8, 3.0)
    draw_wireless_link((4.2, 3.25), (7.8, 3.0), '#D32F2F', "Malicious RO Jamming", 'bottom', rad=-0.1)

    # 5. 添加主標題
    plt.title("Experimental Setup Architecture", fontsize=20, weight='bold', color='#1F2937', y=0.95)

    # 儲存圖片
    plt.tight_layout()
    output_filename = "proposed_setup_diagram.png"
    plt.savefig(output_filename, dpi=300, transparent=False, bbox_inches='tight')
    print(f"✅ 美觀的系統架構圖已產生並儲存為: {output_filename}")
    
    # 若需在有 GUI 的環境中即時檢視，可取消註解下方
    # plt.show()

if __name__ == "__main__":
    create_block_diagram()

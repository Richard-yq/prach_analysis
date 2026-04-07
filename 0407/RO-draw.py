import matplotlib.pyplot as plt
import numpy as np

# 設置字體與樣式，適合 IEEE 簡報
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Liberation Sans']
plt.rcParams['font.size'] = 14

# --- 變數設定 (可自行修改) ---
max_ROs = 8  # 顯示幾個 RO

def draw_scenario(ax, Ta, j, title):
    # 1. 繪製時間軸與 RO 區塊 (變數 i)
    i_vals = np.arange(max_ROs)
    for i in i_vals:
        # 畫 RO 分隔線
        ax.axvline(x=i, color='gray', linestyle='--', alpha=0.3)
        ax.axvline(x=i+1, color='gray', linestyle='--', alpha=0.3)
        # 標示 RO 標籤ㄑ
        ax.text(i + 0.5, 3.2, f'RO #{i}', ha='center', va='center', 
                bbox=dict(facecolor='#f0f0f0', edgecolor='black', boxstyle='round,pad=0.3'))

    # 2. 繪製 Attacker 發送排程 (變數 Ta)
    for i in range(0, max_ROs, Ta):
        ax.add_patch(plt.Rectangle((i+0.1, 1.6), 0.8, 0.8, facecolor='#ff6666', edgecolor='black', lw=1.5))
        ax.text(i+0.5, 2.0, 'MSG1\n(Attack)', ha='center', va='center', color='black', fontweight='bold', fontsize=10)

    # 標示 Ta 的箭頭與文字
    ax.annotate('', xy=(0.5, 2.6), xytext=(0.5 + Ta, 2.6), 
                arrowprops=dict(arrowstyle='<->', color='#d62728', lw=2.5))
    ax.text(0.5 + Ta / 2, 2.7, f'Attack Period ($T_a={Ta}$)', ha='center', va='bottom', color='#d62728', fontweight='bold')

    # 3. 繪製 UE 發送排程 (變數 j)
    # 假設 UE 在 j 到達後，每個 RO 都嘗試發送 (或者你也可以只畫一個框)
    for i in range(j, max_ROs):
        ax.add_patch(plt.Rectangle((i+0.1, 0.1), 0.8, 0.8, facecolor='#66cc66', edgecolor='black', lw=1.5))
        ax.text(i+0.5, 0.5, 'MSG1\n(UE)', ha='center', va='center', color='black', fontweight='bold', fontsize=10)

    # 標示 j 的箭頭與文字
    if j > 0:
        ax.annotate('', xy=(0, 1.1), xytext=(j, 1.1), 
                    arrowprops=dict(arrowstyle='<->', color='#ff7f0e', lw=2.5))
        ax.text(j / 2, 1.2, f'Attack Head Start ($j={j}$)', ha='center', va='bottom', color='#ff7f0e', fontweight='bold')

    # 4. 圖表美化與座標軸設定
    ax.set_xlim(0, max_ROs)
    ax.set_ylim(0, 3.6)
    ax.set_yticks([0.5, 2.0])
    ax.set_yticklabels(['Commercial UE', 'Attacker'], fontweight='bold')

    # 最重要的：標示 X 軸就是變數 i
    ax.set_xlabel('Current Random Access Occasion Index (variable $i$)', fontweight='bold', fontsize=14)
    ax.set_xticks(np.arange(max_ROs + 1)) # 顯示刻度線
    ax.xaxis.set_tick_params(length=5)

    # 隱藏上、右、左邊框，讓畫面更乾淨
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.yaxis.set_tick_params(length=0) # 隱藏 Y 軸刻度線

    ax.set_title(title, fontweight='bold', pad=20)

fig, axes = plt.subplots(2, 1, figsize=(10, 8))

draw_scenario(axes[0], Ta=2, j=3, title='Case 1: $T_a=2$, head start $j=3$')
draw_scenario(axes[1], Ta=1, j=4, title='Case 2: $T_a=1$, head start $j=4$')

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_attack_concept():
    # Setup plot
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.axis('off')
    
    # Title
    plt.title('RACH Msg1 Attack Implementation: UE State', fontsize=16, fontweight='bold', pad=20)
    
    # Helper to draw boxes
    def draw_box(ax, x, y, width, height, text, facecolor, edgecolor, alpha=1.0, linestyle='-'):
        box = patches.FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.1", 
                                     facecolor=facecolor, edgecolor=edgecolor, 
                                     alpha=alpha, linewidth=2, linestyle=linestyle)
        ax.add_patch(box)
        # Add text
        ax.text(x + width/2, y + height/2, text, ha='center', va='center', 
                fontsize=11, fontweight='bold', color='black', wrap=True)
        return box

    # Coordinates
    box_w = 2.5
    box_h = 1.0
    
    # --- Legitimate UE (Top Row) ---
    ax.text(0.5, 3.8, 'Normal UE Behavior:', fontsize=12, fontweight='bold', color='gray')
    
    # Box 1
    draw_box(ax, 1, 2.5, box_w, box_h, "Generate\nPreamble", '#d9ead3', '#38761d')
    # Arrow 1
    ax.annotate('', xy=(4.5, 3.0), xytext=(3.5, 3.0), arrowprops=dict(arrowstyle="->", lw=2, color='#38761d'))
    ax.text(4.0, 3.1, 'Tx Msg1', ha='center', va='bottom', fontsize=10, color='#38761d')
    
    # Box 2
    draw_box(ax, 4.5, 2.5, box_w, box_h, "Start RAR\nReception Window", '#cfe2f3', '#0b5394')
    # Arrow 2
    ax.annotate('', xy=(8.0, 3.0), xytext=(7.0, 3.0), arrowprops=dict(arrowstyle="->", lw=2, color='#0b5394'))
    ax.text(7.5, 3.1, 'Wait Msg2', ha='center', va='bottom', fontsize=10, color='#0b5394')


    # --- Attacker UE (Bottom Row) ---
    ax.text(0.5, 1.8, 'Attacker UE Behavior:', fontsize=12, fontweight='bold', color='#cc0000')
    
    # Box 1
    draw_box(ax, 1, 0.5, box_w, box_h, "1. Keep State:\nGenerate Preamble", '#fce5cd', '#b45f06')
    
    # The Loop Arrow to represent "Keep RA state"
    ax.annotate('', xy=(1.5, 0.5), xytext=(3.0, 0.5), 
                arrowprops=dict(arrowstyle="->", lw=2.5, color='#cc0000', connectionstyle="arc3,rad=-0.5"))
    ax.text(2.25, -0.1, 'Continuous Tx Msg1', ha='center', va='top', fontsize=10, color='#cc0000', fontweight='bold')
    
    # Ghost Arrow
    ax.annotate('', xy=(4.5, 1.0), xytext=(3.5, 1.0), arrowprops=dict(arrowstyle="->", lw=2, color='gray', linestyle='dashed'))
    
    # Box 2 (Ghosted / Canceled)
    draw_box(ax, 4.5, 0.5, box_w, box_h, "2. DO NOT Start\nRAR Window Timer", '#eeeeee', 'gray', alpha=0.5, linestyle='--')
    
    # Big Red X on the second box
    ax.plot([4.8, 6.7], [0.7, 1.3], color='red', lw=4, alpha=0.8)
    ax.plot([4.8, 6.7], [1.3, 0.7], color='red', lw=4, alpha=0.8)
    
    # Set limits
    ax.set_xlim(0, 8.5)
    ax.set_ylim(-0.5, 4.5)
    
    plt.tight_layout()
    plt.savefig('attack_concept_diagram.png', dpi=300)
    print("Image saved as 'attack_concept_diagram.png'")
    # plt.show()

if __name__ == '__main__':
    draw_attack_concept()

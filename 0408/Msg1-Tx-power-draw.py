import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_rach_power():
    fig, ax = plt.subplots(figsize=(10, 5))

    # Disable axes frames
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])

    # 1. Coordinate Definitions
    Y_AXIS = 0
    Y_STEP1 = 1.5
    Y_PMAX = 5.5

    # Set limits
    ax.set_xlim(-0.5, 11)
    ax.set_ylim(-0.5, 6.5)

    X_STEPS_START = 1.5
    STEP_WIDTH = 0.8
    N_STEPS = 7
    STEP_HEIGHT = (Y_PMAX - Y_STEP1) / (N_STEPS - 1)  # 4.0 / 6 = 0.666
    
    X_MSG1_TX_ARROW = X_STEPS_START + N_STEPS * STEP_WIDTH + 0.3

    # 2. Draw Main Axes
    ax.annotate('', xy=(10.5, Y_AXIS), xytext=(0, Y_AXIS), arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
    ax.annotate('', xy=(0, 6.0), xytext=(0, Y_AXIS), arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
    ax.text(10.6, Y_AXIS, 'Time', va='center', fontsize=12)
    ax.text(0, 6.1, 'Power', ha='center', fontsize=12)

    # 3. p-Max Line
    ax.plot([0.5, 10.0], [Y_PMAX, Y_PMAX], 'k-', lw=3)
    ax.text(10.1, Y_PMAX, 'p-Max', va='center', fontsize=12)

    # 5. Dotted Base Line for Step 1
    ax.plot([0.5, X_MSG1_TX_ARROW + 0.5], [Y_STEP1, Y_STEP1], 'k:', lw=2)

    # 6. Steps 1 to 7
    for i in range(N_STEPS):
        x_i = X_STEPS_START + i * STEP_WIDTH
        y_i = Y_STEP1 + i * STEP_HEIGHT
        
        # Horizontal step line
        ax.plot([x_i, x_i + STEP_WIDTH], [y_i, y_i], 'k-', lw=1.5)
        
        # Vertical dotted line down to axis
        ax.plot([x_i, x_i], [Y_AXIS, Y_PMAX], color='gray', linestyle=':', lw=1)
        
        # Step Numbering
        ax.text(x_i + STEP_WIDTH/2, y_i + 0.1, str(i+1), ha='center', va='bottom', fontsize=12)
        
        # Blue UP arrow for ramping step
        if i > 0:
            prev_y = Y_STEP1 + (i-1) * STEP_HEIGHT
            ax.annotate('', xy=(x_i, y_i), xytext=(x_i, prev_y),
                        arrowprops=dict(arrowstyle="-|>", lw=1.5, color='#2980b9', mutation_scale=15))
            
    # Vertical line at the very end of Step 7
    ax.plot([X_STEPS_START + N_STEPS*STEP_WIDTH, X_STEPS_START + N_STEPS*STEP_WIDTH], 
            [Y_AXIS, Y_PMAX], color='gray', linestyle=':', lw=1)

    # Power Ramping Step label with curly brace
    y_brace_center = Y_STEP1 + STEP_HEIGHT/2
    x_brace = X_STEPS_START + STEP_WIDTH + 0.1
    ax.text(x_brace, y_brace_center, r'$\}$', fontsize=26, color='gray', va='center', ha='left')
    ax.text(x_brace + 0.2, y_brace_center, 'powerRampingStep', color='gray', va='center', ha='left', fontsize=11)

    # 7. Msg1 Tx Power red arrow on the right of steps
    ax.annotate('', xy=(X_MSG1_TX_ARROW, Y_PMAX), xytext=(X_MSG1_TX_ARROW, Y_STEP1),
                arrowprops=dict(arrowstyle="<|-|>", lw=1.5, color='#c0392b', mutation_scale=15))
    ax.text(X_MSG1_TX_ARROW + 0.1, (Y_PMAX + Y_STEP1)/2, 'Msg1 Tx power', color='#c0392b', va='center', ha='left', fontsize=11)

    # Save and Show
    plt.tight_layout()
    plt.savefig('power_ramping_detailed.png', dpi=300)
    print("Saved as 'power_ramping_detailed.png'")

if __name__ == '__main__':
    draw_rach_power()

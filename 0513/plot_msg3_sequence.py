import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 7.5), facecolor='#f8fafc')
ax.set_xlim(0.5, 3.5)
ax.set_ylim(0, 11)
ax.axis('off')

# Colors matching the presentation style
COLOR_UE = '#2563eb'       # Primary Blue
COLOR_GNB = '#475569'      # Secondary Slate
COLOR_ATTACKER = '#ef4444' # Accent Red
COLOR_TEXT = '#1e293b'     # Main Text

# Draw Entity lines
entities = {
    'Legitimate UE': (1, COLOR_UE),
    'gNB': (2, COLOR_GNB),
    'Msg3 Attacker UE\n(Parasitic)': (3, COLOR_ATTACKER)
}

for name, (x, color) in entities.items():
    # Vertical dashed lines
    ax.plot([x, x], [1, 10], color=color, linestyle='-', linewidth=2, alpha=0.2)
    # Node boxes at the top
    ax.text(x, 10.5, name, ha='center', va='center', fontsize=12, fontweight='bold', 
            color='white', bbox=dict(facecolor=color, edgecolor='none', boxstyle='round,pad=0.7'))

def draw_msg(y, x_start, x_end, text, color, ls='-', lw=2, offset=0.2):
    """Helper function to draw sequence arrows and text"""
    # Draw Arrow
    ax.annotate('', xy=(x_end, y), xytext=(x_start, y),
                arrowprops=dict(arrowstyle='-|>', color=color, lw=lw, ls=ls, mutation_scale=15))
    
    # Draw Text
    mid_x = (x_start + x_end) / 2
    # Add a small background color to text so it doesn't clash with vertical lines
    ax.text(mid_x, y + offset, text, ha='center', va='bottom', color=color, fontsize=11, fontweight='bold',
            bbox=dict(facecolor='#f8fafc', edgecolor='none', pad=2))

# --- Timeline Sequence ---

# 1. Msg1 (PRACH Preamble)
draw_msg(9, 1, 2, '1. Msg1 (PRACH Preamble)', COLOR_UE)

# 2. Msg2 (RAR)
draw_msg(7.5, 2, 1, '2. Msg2 (RAPID + UL Grant)', COLOR_GNB)
# Attacker intercepts the RAR!
draw_msg(7.5, 2, 3, '2. Msg2 Intercepted!\n(Accepts any RAPID)', COLOR_ATTACKER, ls='--')

# 3. Msg3 Attack vs Normal Msg3
# Attacker acts fast and sends corrupted Msg3 using the intercepted grant
draw_msg(5.5, 3, 2, '3. Msg3 (Corrupted Payload & CRC)', COLOR_ATTACKER, lw=2.5)
# Legitimate UE also attempts to send Msg3
draw_msg(4.7, 1, 2, '3. Msg3 (Normal Transmission)', COLOR_UE, ls=':', lw=1.5)

# 4. gNB Processing Result (Collision / CRC Failure)
# Draw an error box at gNB
bbox_props = dict(boxstyle="round4,pad=0.8", fc="#fee2e2", ec=COLOR_ATTACKER, lw=2)
ax.text(2, 3.2, '[X] CRC Failure!\nCollision / PUSCH Wasted', ha='center', va='center', 
        color=COLOR_ATTACKER, fontsize=11, fontweight='bold', bbox=bbox_props)

# 5. Timeout / Failure
draw_msg(1.5, 2, 1, '4. HARQ NACK / Timeout\n(RACH Procedure Failed)', '#64748b', ls='-.')


# Title
plt.title('Msg3 Opportunistic Attack Sequence Diagram', fontsize=18, fontweight='900', color=COLOR_TEXT, pad=15)
plt.tight_layout()

# Save the plot
output_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(output_dir, 'msg3_attack_sequence.png')
plt.savefig(output_file, dpi=300, bbox_inches='tight')

print(f"✅ Sequence diagram saved successfully to: {output_file}")
# plt.show() # If running locally in IDE, uncomment to preview

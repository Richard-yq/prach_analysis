import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(script_dir, "oai-msg3.log")
output_file = "msg3_victim_data.png"

# Data arrays
line_numbers = []
cumulative_failures = []
alarms_x = []
alarms_y = []

count = 0
try:
    with open(log_file, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if "RA failed at state WAIT_Msg3" in line:
                count += 1
                line_numbers.append(i)
                cumulative_failures.append(count)
                
            if "MSG3 ATTACK DETECTED" in line:
                alarms_x.append(i)
                alarms_y.append(count)
except FileNotFoundError:
    print(f"Error: Could not find {log_file}")
    exit(1)

# Ensure the lists are not empty to avoid plotting errors
if not line_numbers:
    line_numbers = [0]
    cumulative_failures = [0]

# --- Plotting ---
fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f8fafc')

# Draw the step line for cumulative failures
ax.step(line_numbers, cumulative_failures, where='post', color='#2563eb', linewidth=2.5, label='Msg3 HARQ Failures (Cumulative)')

# Draw the markers for attack detection
ax.scatter(alarms_x, alarms_y, color='#ef4444', s=120, zorder=5, marker='X', label='Alarm Triggered: Msg3 Attack Detected')

# Fill area under the curve for better visual impact
ax.fill_between(line_numbers, cumulative_failures, step="post", alpha=0.15, color='#2563eb')

# Formatting
ax.set_title("Msg3 Resource Exhaustion & Alarm Trigger (no Mitigation rApp)", fontsize=16, fontweight='900', pad=15, color='#1e293b')
ax.set_xlabel("Time Progression (Log Line Sequence)", fontsize=12, fontweight='bold', color='#475569', labelpad=10)
ax.set_ylabel("Cumulative Msg3 Failures", fontsize=12, fontweight='bold', color='#475569', labelpad=10)

ax.grid(True, linestyle='--', alpha=0.5)

# Styling the legend
legend = ax.legend(loc='upper left', fontsize=11, framealpha=0.9, edgecolor='#e2e8f0')
legend.get_frame().set_linewidth(1.5)



plt.tight_layout()

# Save the plot
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), output_file)
plt.savefig(output_path, dpi=300, bbox_inches='tight')

print(f"✅ Victim side data plot saved successfully to: {output_path}")

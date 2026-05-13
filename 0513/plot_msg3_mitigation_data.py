import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(script_dir, "OAI_msg3_mitigation.log")
output_file = "msg3_mitigation_data.png"

# Data arrays
line_numbers = []
cumulative_failures = []
alarms_x = []
alarms_y = []
restart_x = None

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
                
            if "RESTARTING OAI gNB" in line:
                restart_x = i
                
        # Append the final line number to extend the step plot to the end of the log
        line_numbers.append(i)
        cumulative_failures.append(count)
except FileNotFoundError:
    print(f"Error: Could not find {log_file}")
    exit(1)

if not line_numbers:
    line_numbers = [0]
    cumulative_failures = [0]

# --- Plotting ---
fig, ax = plt.subplots(figsize=(11, 6), facecolor='#f8fafc')

# Draw the step line for cumulative failures
ax.step(line_numbers, cumulative_failures, where='post', color='#2563eb', linewidth=2.5, label='Msg3 HARQ Failures (Cumulative)')

# Draw the markers for attack detection
if alarms_x:
    ax.scatter(alarms_x, alarms_y, color='#ef4444', s=120, zorder=5, marker='X', label='Alarm Triggered: Msg3 Attack Detected')

# Fill area under the curve
ax.fill_between(line_numbers, cumulative_failures, step="post", alpha=0.15, color='#2563eb')

# Add Restart vertical line if it exists
if restart_x is not None:
    ax.axvline(x=restart_x, color='#10b981', linestyle='--', linewidth=2.5, label='Mitigation Action: gNB Restarted')
    
    # Add a shaded region for the "Mitigated State" after the restart
    ax.axvspan(restart_x, max(line_numbers), color='#d1fae5', alpha=0.4, label='Secure State (Attack Mitigated)')
    
    # Add annotation for the flat line
    ax.annotate('Mitigation Active:\nNo further Msg3 failures', 
                xy=(restart_x + (max(line_numbers) - restart_x)*0.4, cumulative_failures[-1]), 
                xytext=(restart_x + (max(line_numbers) - restart_x)*0.4, 13),
                arrowprops=dict(facecolor='#059669', shrink=0.05, width=1.5, headwidth=8, edgecolor='none'),
                fontsize=11, fontweight='bold', color='#059669',
                ha='center',
                bbox=dict(facecolor='#a7f3d0', edgecolor='none', boxstyle='round,pad=0.5'))

# Formatting
ax.set_title("Msg3 Attack Mitigation Effectiveness (with rApp)", fontsize=16, fontweight='900', pad=15, color='#1e293b')
ax.set_xlabel("Time Progression (Log Line Sequence)", fontsize=12, fontweight='bold', color='#475569', labelpad=10)
ax.set_ylabel("Cumulative Msg3 Failures", fontsize=12, fontweight='bold', color='#475569', labelpad=10)

ax.grid(True, linestyle='--', alpha=0.5)

# Styling the legend
legend = ax.legend(loc='upper left', fontsize=11, framealpha=0.9, edgecolor='#e2e8f0')
legend.get_frame().set_linewidth(1.5)

plt.tight_layout()

# Save the plot
output_path = os.path.join(script_dir, output_file)
plt.savefig(output_path, dpi=300, bbox_inches='tight')

print(f"✅ Mitigation data plot saved successfully to: {output_path}")
print(f"Total Failures: {count}, Alarms: {len(alarms_x)}, Restart Line: {restart_x}")

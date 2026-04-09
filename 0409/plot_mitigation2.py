import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Create stylistic settings suitable for academic papers
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12

# System parameters timeline
attack_start_time = 20
mitigation_trigger_time = 32.5
analysis_window = 9.5
gnb_restarting_time = 8.0
restart_complete_time = mitigation_trigger_time + analysis_window + gnb_restarting_time

# Generate simulation data
t_normal = np.arange(0, attack_start_time)
t_attack = np.arange(attack_start_time, mitigation_trigger_time)
t_analysis = np.arange(mitigation_trigger_time, mitigation_trigger_time + analysis_window)
t_restarting = np.arange(mitigation_trigger_time + analysis_window, restart_complete_time)
t_mitigate = np.arange(restart_complete_time, 90)

# Success rates (%)
np.random.seed(42) # For reproducible results
rate_normal = np.random.uniform(99.5, 100, size=len(t_normal))
rate_attack = np.zeros(len(t_attack))  # Drops exactly to zero
rate_analysis = np.zeros(len(t_analysis)) # Still zero during analysis
rate_restarting = np.zeros(len(t_restarting)) # Still zero during restarting
rate_mitigate = np.random.uniform(99.5, 100, size=len(t_mitigate))

time = np.concatenate([t_normal, t_attack, t_analysis, t_restarting, t_mitigate])
success_rate = np.concatenate([rate_normal, rate_attack, rate_analysis, rate_restarting, rate_mitigate])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the main line
ax.plot(time, success_rate, color='#1f77b4', linewidth=2.5, marker='o', markersize=4, label='RA Success Rate')

# Add background color spans for different phases
ax.axvspan(0, attack_start_time, color='#2ca02c', alpha=0.15)       # Green for normal
ax.axvspan(attack_start_time, mitigation_trigger_time, color='#d62728', alpha=0.15)      # Red for attack
ax.axvspan(mitigation_trigger_time, mitigation_trigger_time + analysis_window, color='#ff7f0e', alpha=0.2)       # Orange for analysis
ax.axvspan(mitigation_trigger_time + analysis_window, restart_complete_time, color='#808080', alpha=0.3)       # Grey for restarting
ax.axvspan(restart_complete_time, 90, color='#2ca02c', alpha=0.3)       # Darker green for mitigated

# Add vertical dashed lines for event markers
ax.axvline(x=attack_start_time, color='#d62728', linestyle='--', linewidth=2, ymin=0, ymax=1)
ax.axvline(x=mitigation_trigger_time, color='#ff7f0e', linestyle='--', linewidth=2, ymin=0, ymax=1)
ax.axvline(x=mitigation_trigger_time + analysis_window, color='#808080', linestyle='--', linewidth=2, ymin=0, ymax=1)
ax.axvline(x=restart_complete_time, color='#2ca02c', linestyle='--', linewidth=2, ymin=0, ymax=1)

# Add text annotations at the top center of each region
ax.text(10, 50, 'Normal\nOperation', ha='center', va='center', fontsize=14, fontweight='bold', color='#1d6b1d')
ax.text(attack_start_time + (mitigation_trigger_time - attack_start_time)/2, 60, 'Under RA Attack\n(Success Rate = 0%)', ha='center', va='center', fontsize=9.5, fontweight='bold', color='#a11a1a')
ax.text(mitigation_trigger_time + analysis_window/2, 50, 'Analysis\nWindow', ha='center', va='center', fontsize=11, fontweight='bold', color='#cc5500')
ax.text(mitigation_trigger_time + analysis_window + gnb_restarting_time/2, 50, 'gNB\nRestarting', ha='center', va='center', fontsize=11, fontweight='bold', color='#404040')
ax.text(70, 50, 'Mitigation Applied\n(Success Rate Restored)', ha='center', va='center', fontsize=14, fontweight='bold', color='#1d6b1d')

# Annotate the specific events
ax.annotate('Attack Initiated', xy=(attack_start_time, 0), xytext=(attack_start_time - 2, 25),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
            fontsize=12, fontweight='bold', ha='right')

ax.annotate('Mitigation Triggered', xy=(mitigation_trigger_time, 0), xytext=(mitigation_trigger_time, 25),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8, alpha=0.8),
            fontsize=12, fontweight='bold', ha='center')

ax.annotate('gNB Restarted', xy=(restart_complete_time, 0), xytext=(restart_complete_time + 12, 15),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
            fontsize=12, fontweight='bold')

# Set labels and title
ax.set_xlabel('Time', fontweight='bold', labelpad=15)
ax.set_ylabel('RACH Success Rate (%)', fontweight='bold')
ax.set_title('Impact of Proposed Mitigation Strategy on RACH Success Rate', pad=20)

# Set limits
ax.set_xlim(0, 90)
ax.set_ylim(-5, 105)

# Remove numeric x-axis ticks to represent abstract/configurable time
ax.set_xticks([])

# Add grid for y-axis only
ax.grid(axis='y', linestyle=':', alpha=0.7)

# Handle legend for background regions
custom_lines = [
    plt.Line2D([0], [0], color='#1f77b4', lw=2.5, marker='o'),
    Patch(facecolor='#2ca02c', alpha=0.2, label='gNB Normal / Secured'),
    Patch(facecolor='#d62728', alpha=0.15, label='gNB Compromised'),
    Patch(facecolor='#ff7f0e', alpha=0.2, label='Analysis Window'),
    Patch(facecolor='#808080', alpha=0.3, label='gNB Restarting')
]
ax.legend(handles=custom_lines, labels=['RA Success Rate', 'gNB Normal / Secured', 'gNB Compromised', 'Analysis Window', 'gNB Restarting'], loc='upper right')

# Tight layout
plt.tight_layout()

# Save the figure
output_file = 'mitigation_success_rate.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
print(f"Plot successfully generated and saved as '{output_file}'")

# plt.show() # Uncomment if you want to display the plot interactively in a Jupyter notebook or GUI

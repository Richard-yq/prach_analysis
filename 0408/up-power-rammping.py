import matplotlib.pyplot as plt
import numpy as np

def plot_power_ramping():
    # Parameters defined by the user
    initial_power = -21     # dBm
    power_ramping_step = 2  # dB
    max_power = 20          # dBm
    preambleTransMax = 30   # Example max attempts
    
    # Calculate power for each attempt
    attempts = np.arange(1, preambleTransMax + 1)
    powers = []
    
    curr_power = initial_power
    for i in range(preambleTransMax):
        powers.append(curr_power)
        # Power increases for the next attempt, but cannot exceed max_power
        curr_power = min(curr_power + power_ramping_step, max_power)
        
    # Create the plot
    plt.figure(figsize=(10, 6))
    
    # We use both lines and markers to clearly show the steps
    plt.plot(attempts, powers, marker='o', markersize=6, color='#1f77b4', linestyle='-', linewidth=2, label='UE Transmit Power')
    
    # Highlight the max power limit
    plt.axhline(y=max_power, color='#d62728', linestyle='--', alpha=0.7, linewidth=2, label=f'Max Power ({max_power} dBm)')
    
    # Annotate the start and max point
    plt.annotate(f'Start: {initial_power} dBm', 
                 xy=(1, initial_power), xytext=(2, initial_power - 2),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6))
                 
    # Find the attempt where max power is first reached
    max_power_attempt = attempts[powers.index(max_power)]
    plt.annotate('Reaches Max Power', 
                 xy=(max_power_attempt, max_power), 
                 xytext=(max_power_attempt - 6, max_power + 2.5),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6))

    # Formatting
    plt.title('UE Power Ramping', fontsize=15, fontweight='bold')
    plt.xlabel('Preamble Transmission Counter', fontsize=12)
    plt.ylabel('Transmit Power (dBm)', fontsize=12)
    
    plt.xlim(0, preambleTransMax + 1)
    plt.ylim(initial_power - 5, max_power + 5)
    
    plt.xticks(np.arange(1, preambleTransMax + 1, 2))
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=12, loc='lower right')
    
    plt.tight_layout()
    
    # Save and show
    plt.savefig('power_ramping_concept.png', dpi=300)
    print("Image saved as 'power_ramping_concept.png'")
    plt.show()

if __name__ == '__main__':
    plot_power_ramping()

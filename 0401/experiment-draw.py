import numpy as np
import matplotlib.pyplot as plt

def generate_plots():
    # Parameters derived from image analysis
    J_MAX = 15
    j_values = np.arange(0, J_MAX + 1)
    
    beta_values = [0.24, 0.12, 0.06, 0]
    beta_labels = ['0.24', '0.12', '0.06', '0']
    
    P_th_0 = 16.5
    P_J = 52.0
    p_UE_delta = 44.4
    
    # Styles
    colors = ['#1f77b4', 'orange', 'green', 'red']  # blue, orange, green, red
    line_styles = ['-', ':', '--', '-.']
    markers = ['3', '4', '+', 'o']
    
    # Enable LaTeX math font similar to publication quality (optional but looks good)
    plt.rcParams.update({'font.size': 12})
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6.5))
    
    # ---- Left Subplot: P_{S,j} ----
    ax1 = axes[0]
    
    # Step 1: Draw lines first
    for i, beta in enumerate(beta_values):
        P_th_j = P_th_0 * (1 - beta)**j_values + P_J * (1 - (1 - beta)**j_values)
        P_S_j = np.where(P_th_j <= p_UE_delta, 1.0, 0.0)
        ax1.plot(j_values, P_S_j, color=colors[i], linestyle=line_styles[i], 
                 label=f'$\\beta = {beta_labels[i]}$', linewidth=1.5)

    # Step 2: Draw scatters (Expe) so they appear below the lines in legend as required
    for i, beta in enumerate(beta_values):
        P_th_j = P_th_0 * (1 - beta)**j_values + P_J * (1 - (1 - beta)**j_values)
        P_S_j = np.where(P_th_j <= p_UE_delta, 1.0, 0.0)
        
        # We use explicit colors to match standard matplotlib palette if we want,
        # but the defined colors array works well.
        if markers[i] == 'o':
            ax1.scatter(j_values, P_S_j, facecolors='none', edgecolors=colors[i], 
                        marker=markers[i], s=250, linewidths=1.5,
                        label=f'$\\beta = {beta_labels[i]}$ (Expe)', zorder=3)
        else:
            ax1.scatter(j_values, P_S_j, color=colors[i], marker=markers[i], s=250, 
                        linewidths=1.5, label=f'$\\beta = {beta_labels[i]}$ (Expe)', zorder=3)
            
    ax1.set_title('$P_{S,j}$ vs $j$ for Different $\\beta$ Values')
    ax1.set_xlabel('$j$ (Attacker No. of RAO Early Start)')
    ax1.set_ylabel('$P_{S,j}$ (UE Msg1 Success Probability at $j$)')
    ax1.set_xticks(np.arange(0, 16, 2))
    ax1.set_yticks(np.arange(0.0, 1.2, 0.2))
    ax1.grid(True)
    ax1.legend(loc='lower left')
    
    # ---- Right Subplot: p_th,j ----
    ax2 = axes[1]
    
    # Draw lines
    for i, beta in enumerate(beta_values):
        P_th_j = P_th_0 * (1 - beta)**j_values + P_J * (1 - (1 - beta)**j_values)
        ax2.plot(j_values, P_th_j, color=colors[i], linestyle=line_styles[i], 
                 label=f'$\\beta = {beta_labels[i]}$', linewidth=1.5)
                 
    # Draw scatters
    for i, beta in enumerate(beta_values):
        P_th_j = P_th_0 * (1 - beta)**j_values + P_J * (1 - (1 - beta)**j_values)
        
        if markers[i] == 'o':
            ax2.scatter(j_values, P_th_j, facecolors='none', edgecolors=colors[i], 
                        marker=markers[i], s=250, linewidths=1.5,
                        label=f'$\\beta = {beta_labels[i]}$ (Expe)', zorder=3)
        else:
            ax2.scatter(j_values, P_th_j, color=colors[i], marker=markers[i], s=250, 
                        linewidths=1.5, label=f'$\\beta = {beta_labels[i]}$ (Expe)', zorder=3)

    # Plot p_UE - \delta
    # Use dashdot but looser as in the image
    ax2.axhline(y=p_UE_delta, color='purple', linestyle=(0, (3, 5, 1, 5)), 
                label='$p_{UE} - \\delta$', linewidth=1.5)
                
    ax2.set_title('$p_{th,j}$ vs $j$ for Different $\\beta$ Values')
    ax2.set_xlabel('$j$ (Attacker No. of RAO Early Start)')
    ax2.set_ylabel('$p_{th,j}$ (gNB\'s Noise Threshold at $j$)')
    ax2.set_xticks(np.arange(0, 16, 2))
    ax2.set_yticks(np.arange(15, 55, 5))
    ax2.grid(True)
    ax2.legend(loc='upper left')
    
    plt.tight_layout()
    
    # Save the files
    output_filename1 = '/Users/yq/Documents/analysis/0401/experiment_corrected.png'
    output_filename2 = '/Users/yq/Documents/analysis/0401/image.png'
    plt.savefig(output_filename1, dpi=300, bbox_inches='tight')
    plt.savefig(output_filename2, dpi=300, bbox_inches='tight')
    print(f"✅ Plots generated successfully:\\n- {output_filename1}\\n- {output_filename2}")

if __name__ == "__main__":
    generate_plots()

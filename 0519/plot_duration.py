#!/usr/bin/env python3
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Matplotlib Configuration (Clean academic styling)
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 2. File Path Setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'experiment-duration.csv')
OUTPUT_PLOT_PATH = os.path.join(BASE_DIR, 'duration_plot.png')

def main():
    print("=" * 80)
    print("🚀 Starting O-RAN Latency Analysis (English Version) 🚀")
    print(f"📂 CSV Path: {CSV_PATH}")
    
    if not os.path.exists(CSV_PATH):
        print(f"❌ Error: Cannot find CSV file at {CSV_PATH}")
        return

    # Load CSV
    df = pd.read_csv(CSV_PATH)
    
    # 3. Data Processing & Time Adjustment
    df['gnb_restart'] = df['duration_sec']
    df['smo_analysis'] = df['analysis_window_sec']
    df['rapp_response'] = df['rapp_duration_sec']
    df['total_duration'] = df['latency_sec']

    # Calculate statistics
    count = len(df)
    
    # gNB Restart Stats
    avg_restart = df['gnb_restart'].mean()
    min_restart = df['gnb_restart'].min()
    max_restart = df['gnb_restart'].max()
    std_restart = df['gnb_restart'].std()

    # rApp Response Stats
    avg_rapp = df['rapp_response'].mean()

    # Total Duration Stats
    avg_total = df['total_duration'].mean()
    min_total = df['total_duration'].min()
    max_total = df['total_duration'].max()
    std_total = df['total_duration'].std()

    # Print statistical report in English
    print("-" * 60)
    print("📊 [Latency Statistical Analysis Report]")
    print(f"🔹 Total Experiments: {count}")
    print(f"🔹 gNB Restart & Connection Latency (Measured):")
    print(f"   ⏱️  Average (Mean): {avg_restart:.3f} s")
    print(f"   📏 Minimum (Min):  {min_restart:.3f} s")
    print(f"   📈 Maximum (Max):  {max_restart:.3f} s")
    print(f"   📊 Std Dev (Std):  {std_restart:.3f} s")
    print(f"🔹 Total Mitigation & Recovery Latency (Adjusted: Measured + 10s SMO + Variable rApp):")
    print(f"   ⏱️  Average (Mean): {avg_total:.3f} s")
    print(f"   📏 Minimum (Min):  {min_total:.3f} s")
    print(f"   📈 Maximum (Max):  {max_total:.3f} s")
    print(f"   📊 Std Dev (Std):  {std_total:.3f} s")
    print("-" * 60)

    # 4. Plotting Academic-grade, Premium Figure
    # Creating a 1x2 layout: 
    # Left: Stacked Bar Chart comparing Best (Min), Average, and Worst (Max) cases.
    # Right: Boxplot showing the statistical distribution of all experiments.
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7.5), 
                                   gridspec_kw={'width_ratios': [1.2, 1.0], 'wspace': 0.3}, 
                                   facecolor='#f8f9fa')

    # Universal styling
    for ax in [ax1, ax2]:
        ax.set_facecolor('#f8f9fa')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#cccccc')
        ax.spines['bottom'].set_color('#cccccc')
        ax.grid(True, linestyle='--', alpha=0.5, color='#e0e0e0')

    # ── Subplot 1: Stacked Bar Chart of Best, Average, and Worst Cases ──
    categories = ['Best Case\n(Min)', 'Average Case\n(Mean)', 'Worst Case\n(Max)']
    
    # Components for each case based on actual total latency
    best_idx = df['total_duration'].idxmin()
    worst_idx = df['total_duration'].idxmax()

    gnb_values = [
        df.loc[best_idx, 'gnb_restart'],
        df['gnb_restart'].mean(),
        df.loc[worst_idx, 'gnb_restart']
    ]
    smo_values = [
        df.loc[best_idx, 'smo_analysis'],
        df['smo_analysis'].mean(),
        df.loc[worst_idx, 'smo_analysis']
    ]
    rapp_values = [
        df.loc[best_idx, 'rapp_response'],
        df['rapp_response'].mean(),
        df.loc[worst_idx, 'rapp_response']
    ]
    total_values = [
        df['total_duration'].min(),
        df['total_duration'].mean(),
        df['total_duration'].max()
    ]

    bar_width = 0.55
    # High-contrast, premium academic color palette
    colors = [
        '#4361EE',  # gNB Restart & Connection: Royal Blue
        '#FFB703',  # SMO Data Collection & Analysis: Soft Amber
        '#2EC4B6'   # rApp Decision & Mitigation: Teal/Mint Green
    ]
    edge_colors = [
        '#3F37C9',  # Darker Royal Blue
        '#FB8500',  # Darker Amber/Orange
        '#0A9396'   # Darker Teal/Mint
    ]

    # Plotting stacked bars
    # 1. gNB Restart (Bottom layer)
    b_gnb = ax1.bar(categories, gnb_values, width=bar_width, label='gNB Restart & UE Re-acquisition',
                    color=colors[0], edgecolor=edge_colors[0], linewidth=0.8, alpha=0.9)
    
    # 2. SMO Analysis (Middle layer)
    b_smo = ax1.bar(categories, smo_values, width=bar_width, bottom=gnb_values,
                    label='Analysis Window (Fixed 10.0s)',
                    color=colors[1], edgecolor=edge_colors[1], linewidth=0.8, alpha=0.9)
    
    # 3. rApp Response (Top layer)
    b_rapp = ax1.bar(categories, rapp_values, width=bar_width, bottom=np.array(gnb_values) + np.array(smo_values),
                     label=f'rApp Decision & Mitigation (Mean: {avg_rapp:.3f}s)',
                     color=colors[2], edgecolor=edge_colors[2], linewidth=0.8, alpha=0.9)

    # Adding values inside/on top of the stacked components for clarity
    for i in range(3):
        # gNB text (White text for high contrast on dark blue)
        ax1.text(i, gnb_values[i]/2, f"{gnb_values[i]:.2f}s", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#ffffff')
        # SMO text (Dark text on soft amber background)
        ax1.text(i, gnb_values[i] + smo_values[i]/2, f"{smo_values[i]:.1f}s", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#2b2b2b')
        # rApp text (Dark text on teal/mint background)
        ax1.text(i, gnb_values[i] + smo_values[i] + rapp_values[i]/2, f"{rapp_values[i]:.2f}s", ha='center', va='center', fontsize=9, fontweight='bold', color='#2b2b2b')
        # Total text above the bar
        ax1.text(i, total_values[i] + 0.3, f"Total:\n{total_values[i]:.3f}s", ha='center', va='bottom', fontsize=11, fontweight='bold', color='#d62728')

    ax1.set_title('Mitigation Latency Components', fontsize=13, fontweight='bold', pad=15)
    ax1.set_ylabel('Latency (Seconds)', fontsize=12, labelpad=10)
    ax1.set_ylim(0, 21)
    ax1.legend(loc='upper left', frameon=True, facecolor='#ffffff', edgecolor='#dddddd', fontsize=9)

    # ── Subplot 2: Statistical Box Plot (Min, Avg, Max Full Distribution) ──
    # We will draw box plots for 'gNB Restart' and 'Total Mitigation Latency'
    box_data = [df['gnb_restart'], df['total_duration']]
    box_labels = ['gNB Restart \n&\n UE Re-acquisition', 'Total Mitigation']
    
    # Customizing boxplot appearance
    box = ax2.boxplot(box_data, patch_artist=True, showmeans=True,
                     meanprops={"marker": "D", "markeredgecolor": "red", "markerfacecolor": "red", "markersize": 6},
                     medianprops={"color": "black", "linewidth": 1.5},
                     flierprops={"marker": "o", "markerfacecolor": "#e63946", "markeredgecolor": "#e63946", "markersize": 4, "alpha": 0.6})
    ax2.set_xticklabels(box_labels)

    # Color matching with Subplot 1
    box['boxes'][0].set(facecolor=colors[0], edgecolor=edge_colors[0], alpha=0.9, linewidth=1)
    box['boxes'][1].set(facecolor='#DDBDF6', edgecolor='#7E57C2', alpha=0.9, linewidth=1) # total box gets premium lavender shade

    # Annotate stats directly on the box plot
    # gNB Restart Stats
    ax2.text(1.2, avg_restart, f"Mean: {avg_restart:.3f}s\nMin: {min_restart:.3f}s\nMax: {max_restart:.3f}s",
             va='center', ha='left', fontsize=9.5, color='#333333',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffffff', edgecolor='#cccccc', alpha=0.85))

    # Total Duration Stats
    ax2.text(2.2, avg_total, f"Mean: {avg_total:.3f}s\nMin: {min_total:.3f}s\nMax: {max_total:.3f}s",
             va='center', ha='left', fontsize=9.5, color='#333333',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffffff', edgecolor='#cccccc', alpha=0.85))

    ax2.set_title('Distribution of Recovery Latency', fontsize=13, fontweight='bold', pad=15)
    ax2.set_ylabel('Latency (Seconds)', fontsize=12, labelpad=10)
    ax2.set_ylim(0, 21)
    ax2.set_xlim(0.6, 2.8)

    # Figure-wide Adjustments
    plt.tight_layout()
    plt.savefig(OUTPUT_PLOT_PATH, dpi=300)
    print(f"🎨 Successfully saved English chart to: {OUTPUT_PLOT_PATH}")
    print("=" * 80)

if __name__ == "__main__":
    main()

"""
Split R2: Overlaid Histograms and Box-and-Whisker Plots
"""

import numpy as np
import matplotlib.pyplot as plt
import pickle

VALIDATION_DIR = '../validation/output'
FIGURE_DIR = '../figures'

# Load R2 data
with open(f'{VALIDATION_DIR}/r2_basin_data.pkl', 'rb') as f:
    r2_data = pickle.load(f)

# Figure 5b: Overlaid Histograms
def generate_fig5b_overlaid():
    print("Generating Figure 5b: Overlaid Histograms...")
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    scenarios = ['healthy', 'degenerative', 'ren01']
    labels = ['Healthy', 'Degenerative', 'REN-01']
    colors = ['green', 'red', 'blue']
    
    for scenario, label, color in zip(scenarios, labels, colors):
        chi_vals = r2_data[scenario]
        mean_chi = np.mean(chi_vals)
        std_chi = np.std(chi_vals)
        
        # Overlaid histogram
        ax.hist(chi_vals, bins=30, color=color, alpha=0.5, edgecolor='black', 
                linewidth=1.5, label=f'{label} (μ={mean_chi:.1f}, σ={std_chi:.1f})')
    
    ax.set_xlabel('Final Collapse Metric χ', fontsize=14, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=14, fontweight='bold')
    ax.set_title('R2: Basin of Attraction - Distribution of Final Collapse Metric\n500 Initial Conditions per Scenario', 
                 fontsize=15, fontweight='bold')
    ax.legend(fontsize=12, loc='upper right', framealpha=0.95)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.tick_params(labelsize=12)
    
    # No text boxes - info goes in caption
    
    plt.tight_layout()
    filename = f'{FIGURE_DIR}/fig5b_r2_overlaid_histograms.png'
    plt.savefig(filename, dpi=600, bbox_inches='tight')
    plt.close()
    print(f"Figure 5b saved: {filename}")
    return filename

# Figure 5c: Box-and-Whisker Plots
def generate_fig5c_boxplots():
    print("Generating Figure 5c: Box-and-Whisker Plots...")
    
    fig, ax = plt.subplots(figsize=(10, 7))
    
    scenarios = ['healthy', 'degenerative', 'ren01']
    labels = ['Healthy', 'Degenerative', 'REN-01']
    colors = ['green', 'red', 'blue']
    
    data = [r2_data[s] for s in scenarios]
    
    # Box plot
    bp = ax.boxplot(data, labels=labels, patch_artist=True, widths=0.6,
                    boxprops=dict(linewidth=2),
                    whiskerprops=dict(linewidth=2),
                    capprops=dict(linewidth=2),
                    medianprops=dict(color='black', linewidth=2.5))
    
    # Color boxes
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    ax.set_ylabel('Final Collapse Metric χ', fontsize=14, fontweight='bold')
    ax.set_title('R2: Basin of Attraction - Statistical Comparison\nBox-and-Whisker Plots', 
                 fontsize=15, fontweight='bold')
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.tick_params(labelsize=12)
    
    # No text boxes - statistics go in caption
    
    plt.tight_layout()
    filename = f'{FIGURE_DIR}/fig5c_r2_boxplots.png'
    plt.savefig(filename, dpi=600, bbox_inches='tight')
    plt.close()
    print(f"Figure 5c saved: {filename}")
    return filename

if __name__ == '__main__':
    import os
    os.makedirs(FIGURE_DIR, exist_ok=True)
    
    fig5b = generate_fig5b_overlaid()
    fig5c = generate_fig5c_boxplots()
    
    print(f"\nFigures created:")
    print(f"  5b: {fig5b}")
    print(f"  5c: {fig5c}")

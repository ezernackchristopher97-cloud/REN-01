"""
Regenerate Ablation Ladder: 2 on top, 1 centered below
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pickle

VALIDATION_DIR = '../validation/output'
FIGURE_DIR = '../figures'

# Load ablation data
with open(f'{VALIDATION_DIR}/ablation_data.pkl', 'rb') as f:
    ablation_data = pickle.load(f)

def generate_fig5d_layout():
    """Generate ablation ladder with 2+1 layout"""
    print("Generating Figure 5d: Ablation Ladder (2+1 layout)...")
    
    # Create figure with gridspec
    fig = plt.figure(figsize=(16, 10))
    gs = gridspec.GridSpec(2, 4, figure=fig, hspace=0.35, wspace=0.3)
    
    # Top row: 2 line plots
    ax1 = fig.add_subplot(gs[0, 0:2])
    ax2 = fig.add_subplot(gs[0, 2:4])
    # Bottom row: 1 centered bar chart
    ax3 = fig.add_subplot(gs[1, 1:3])
    
    configs = ablation_data['configs']
    labels_short = ablation_data['labels']
    colors = plt.cm.viridis(np.linspace(0, 1, len(configs)))
    
    # Plot 1: Final chi comparison (line plot showing ordering)
    final_chis = ablation_data['chi_final']
    x_pos = np.arange(len(configs))
    ax1.plot(x_pos, final_chis, 'o-', color='darkblue', 
             linewidth=3, markersize=10, markerfacecolor='lightblue', 
             markeredgecolor='darkblue', markeredgewidth=2)
    
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(labels_short, rotation=45, ha='right', fontsize=10)
    ax1.set_ylabel('Final Collapse Metric χ', fontsize=12, fontweight='bold')
    ax1.set_title('Final χ: Component Contribution Ordering', fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.axhline(y=1.0, color='red', linestyle=':', linewidth=2, alpha=0.7, label='Collapse threshold')
    ax1.legend(fontsize=10)
    
    # Plot 2: Dopamine and entropy fields
    psi_D_vals = ablation_data['psi_D_final']
    phi_E_vals = ablation_data['phi_E_final']
    
    ax2_twin = ax2.twinx()
    ax2.bar(x_pos - 0.2, psi_D_vals, width=0.4, color='blue', alpha=0.6, label='ψ_D (Dopamine)', edgecolor='black', linewidth=1.5)
    ax2_twin.bar(x_pos + 0.2, phi_E_vals, width=0.4, color='red', alpha=0.6, label='φ_E (Entropy)', edgecolor='black', linewidth=1.5)
    
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(labels_short, rotation=45, ha='right', fontsize=10)
    ax2.set_ylabel('Dopamine Field ψ_D', fontsize=11, fontweight='bold', color='blue')
    ax2_twin.set_ylabel('Entropy Field φ_E', fontsize=11, fontweight='bold', color='red')
    ax2.set_title('Dopamine vs Entropy: Ablation Effects', fontsize=13, fontweight='bold')
    ax2.legend(loc='upper left', fontsize=9)
    ax2_twin.legend(loc='upper right', fontsize=9)
    ax2.grid(True, alpha=0.3, linestyle='--')
    
    # Plot 3: Bar chart with component breakdown
    ax3.bar(x_pos, final_chis, color=colors, alpha=0.7, edgecolor='black', linewidth=2)
    ax3.set_xticks(x_pos)
    ax3.set_xticklabels(labels_short, fontsize=11, fontweight='bold')
    ax3.set_ylabel('Final Collapse Metric χ', fontsize=13, fontweight='bold')
    ax3.set_title('Ablation Ladder: Component Contributions', fontsize=14, fontweight='bold')
    ax3.grid(axis='y', alpha=0.3, linestyle='--')
    ax3.axhline(y=1.0, color='red', linestyle=':', linewidth=2.5, alpha=0.7)
    
    # Add values on bars
    for i, (val, label) in enumerate(zip(final_chis, labels_short)):
        ax3.text(i, val + 0.5, f'{val:.1f}', ha='center', va='bottom', 
                fontsize=10, fontweight='bold')
    
    plt.suptitle('Ablation Study: Systematic Component Removal\nIdentifies MOR Agonism as Dominant Mechanism', 
                 fontsize=16, fontweight='bold', y=0.98)
    
    filename = f'{FIGURE_DIR}/fig5d_ablation_ladder.png'
    plt.savefig(filename, dpi=600, bbox_inches='tight')
    plt.close()
    
    print(f"Figure 5d saved: {filename}")
    return filename

if __name__ == '__main__':
    import os
    os.makedirs(FIGURE_DIR, exist_ok=True)
    
    fig5d = generate_fig5d_layout()
    print(f"\nFigure 5d created: {fig5d}")

"""
Split Ablation into 3 Separate Figures
"""

import numpy as np
import matplotlib.pyplot as plt
import pickle

VALIDATION_DIR = '../validation/output'
FIGURE_DIR = '../figures'

# Load ablation data
with open(f'{VALIDATION_DIR}/ablation_data.pkl', 'rb') as f:
    ablation_data = pickle.load(f)

configs = ablation_data['configs']
labels_short = ablation_data['labels']
final_chis = ablation_data['chi_final']
psi_D_vals = ablation_data['psi_D_final']
phi_E_vals = ablation_data['phi_E_final']
x_pos = np.arange(len(configs))
colors = plt.cm.viridis(np.linspace(0, 1, len(configs)))

# Figure 5d: Final χ ordering (line plot)
def generate_fig5d():
    print("Generating Figure 5d: Final χ Ordering...")
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    ax.plot(x_pos, final_chis, 'o-', color='darkblue', 
            linewidth=3.5, markersize=12, markerfacecolor='lightblue', 
            markeredgecolor='darkblue', markeredgewidth=2.5)
    
    ax.set_xticks(x_pos)
    ax.set_xticklabels(labels_short, rotation=45, ha='right', fontsize=12, fontweight='bold')
    ax.set_ylabel('Final Collapse Metric χ', fontsize=14, fontweight='bold')
    ax.set_title('Ablation Study: Component Contribution Ordering', fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.axhline(y=1.0, color='red', linestyle=':', linewidth=2.5, alpha=0.7, label='Collapse threshold (χ=1)')
    ax.legend(fontsize=12, loc='best')
    ax.tick_params(labelsize=11)
    
    # Add values
    for i, val in enumerate(final_chis):
        ax.text(i, val + 1, f'{val:.1f}', ha='center', va='bottom', 
                fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    filename = f'{FIGURE_DIR}/fig5d_ablation_ordering.png'
    plt.savefig(filename, dpi=600, bbox_inches='tight')
    plt.close()
    print(f"Figure 5d saved: {filename}")
    return filename

# Figure 5e: Dopamine vs Entropy (dual bar chart)
def generate_fig5e():
    print("Generating Figure 5e: Dopamine vs Entropy Effects...")
    
    fig, ax1 = plt.subplots(figsize=(12, 7))
    ax2 = ax1.twinx()
    
    width = 0.35
    ax1.bar(x_pos - width/2, psi_D_vals, width, color='blue', alpha=0.7, 
            label='ψ_D (Dopamine)', edgecolor='black', linewidth=2)
    ax2.bar(x_pos + width/2, phi_E_vals, width, color='red', alpha=0.7, 
            label='φ_E (Entropy)', edgecolor='black', linewidth=2)
    
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(labels_short, rotation=45, ha='right', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Dopamine Field ψ_D', fontsize=14, fontweight='bold', color='blue')
    ax2.set_ylabel('Entropy Field φ_E', fontsize=14, fontweight='bold', color='red')
    ax1.set_title('Ablation Study: Dopamine vs Entropy Field Effects', fontsize=16, fontweight='bold')
    ax1.legend(loc='upper left', fontsize=12, framealpha=0.95)
    ax2.legend(loc='upper right', fontsize=12, framealpha=0.95)
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.tick_params(labelsize=11, colors='blue')
    ax2.tick_params(labelsize=11, colors='red')
    
    plt.tight_layout()
    filename = f'{FIGURE_DIR}/fig5e_ablation_fields.png'
    plt.savefig(filename, dpi=600, bbox_inches='tight')
    plt.close()
    print(f"Figure 5e saved: {filename}")
    return filename

# Figure 5f: Component breakdown (bar chart)
def generate_fig5f():
    print("Generating Figure 5f: Component Breakdown...")
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    bars = ax.bar(x_pos, final_chis, color=colors, alpha=0.75, 
                  edgecolor='black', linewidth=2.5)
    
    ax.set_xticks(x_pos)
    ax.set_xticklabels(labels_short, fontsize=12, fontweight='bold')
    ax.set_ylabel('Final Collapse Metric χ', fontsize=14, fontweight='bold')
    ax.set_title('Ablation Ladder: Systematic Component Removal\nMOR Agonism Identified as Dominant Mechanism', 
                 fontsize=16, fontweight='bold')
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.axhline(y=1.0, color='red', linestyle=':', linewidth=2.5, alpha=0.7)
    ax.tick_params(labelsize=11)
    
    # Add values on bars
    for i, (bar, val) in enumerate(zip(bars, final_chis)):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{val:.1f}', ha='center', va='bottom', 
                fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    filename = f'{FIGURE_DIR}/fig5f_ablation_summary.png'
    plt.savefig(filename, dpi=600, bbox_inches='tight')
    plt.close()
    print(f"Figure 5f saved: {filename}")
    return filename

if __name__ == '__main__':
    import os
    os.makedirs(FIGURE_DIR, exist_ok=True)
    
    fig5d = generate_fig5d()
    fig5e = generate_fig5e()
    fig5f = generate_fig5f()
    
    print(f"\nFigures created:")
    print(f"  5d: {fig5d}")
    print(f"  5e: {fig5e}")
    print(f"  5f: {fig5f}")

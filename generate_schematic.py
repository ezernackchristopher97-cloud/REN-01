"""
Generate REN-01 System Schematic
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

FIGURE_DIR = '../figures'

def generate_schematic():
    print("Generating system schematic...")
    
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(8, 9.5, 'REN-01 Mechanism of Action', fontsize=22, fontweight='bold', ha='center')
    
    # Three main components boxes
    # MOR Agonism (left)
    mor_box = FancyBboxPatch((0.5, 5.5), 4.5, 3, boxstyle="round,pad=0.1", 
                             edgecolor='darkblue', facecolor='lightblue', linewidth=3, alpha=0.8)
    ax.add_patch(mor_box)
    ax.text(2.75, 8.2, 'MOR Agonism', fontsize=16, fontweight='bold', ha='center')
    ax.text(2.75, 7.6, 'α_D = 0.667', fontsize=13, ha='center', family='monospace')
    ax.text(2.75, 7.1, 'Ki ~ 5 nM', fontsize=12, ha='center')
    ax.text(2.75, 6.5, 'Dopamine', fontsize=13, ha='center')
    ax.text(2.75, 6.1, 'Restoration', fontsize=13, ha='center')
    
    # CB2 Binding (middle)
    cb2_box = FancyBboxPatch((5.75, 5.5), 4.5, 3, boxstyle="round,pad=0.1",
                             edgecolor='darkgreen', facecolor='lightgreen', linewidth=3, alpha=0.8)
    ax.add_patch(cb2_box)
    ax.text(8, 8.2, 'CB2 Binding', fontsize=16, fontweight='bold', ha='center')
    ax.text(8, 7.6, 'α_A = 0.167', fontsize=13, ha='center', family='monospace')
    ax.text(8, 7.1, 'Ki ~ 50 nM', fontsize=12, ha='center')
    ax.text(8, 6.5, 'Astrocyte', fontsize=13, ha='center')
    ax.text(8, 6.1, 'Modulation', fontsize=13, ha='center')
    
    # Entropy Suppression (right)
    ent_box = FancyBboxPatch((11, 5.5), 4.5, 3, boxstyle="round,pad=0.1",
                             edgecolor='darkred', facecolor='lightcoral', linewidth=3, alpha=0.8)
    ax.add_patch(ent_box)
    ax.text(13.25, 8.2, 'Entropy Suppression', fontsize=16, fontweight='bold', ha='center')
    ax.text(13.25, 7.6, 'β_E = 0.269', fontsize=13, ha='center', family='monospace')
    ax.text(13.25, 7.1, 'MW = 386.6 g/mol', fontsize=12, ha='center')
    ax.text(13.25, 6.5, 'Information', fontsize=13, ha='center')
    ax.text(13.25, 6.1, 'Coherence', fontsize=13, ha='center')
    
    # Quaternion field box (center bottom)
    quat_box = FancyBboxPatch((4, 2), 8, 2.5, boxstyle="round,pad=0.1",
                              edgecolor='black', facecolor='wheat', linewidth=3, alpha=0.9)
    ax.add_patch(quat_box)
    ax.text(8, 4, 'Quaternionic Field Dynamics', fontsize=16, fontweight='bold', ha='center')
    ax.text(8, 3.4, 'Q = q₀ + q₁i + q₂j + q₃k', fontsize=14, ha='center', family='serif')
    ax.text(8, 2.8, 'ψ_D = q₀²  (dopamine)', fontsize=12, ha='center')
    ax.text(8, 2.4, 'φ_E = q₁² + q₂² + q₃²  (entropy)', fontsize=12, ha='center')
    
    # Arrows from components to quaternion field
    arrow1 = FancyArrowPatch((2.75, 5.4), (6, 4.6), arrowstyle='->', 
                            mutation_scale=30, linewidth=3, color='darkblue')
    ax.add_patch(arrow1)
    ax.text(4, 5.2, 'q₀', fontsize=13, fontweight='bold', color='darkblue')
    
    arrow2 = FancyArrowPatch((8, 5.4), (8, 4.6), arrowstyle='->', 
                            mutation_scale=30, linewidth=3, color='darkgreen')
    ax.add_patch(arrow2)
    ax.text(8.3, 5, 'q₂', fontsize=13, fontweight='bold', color='darkgreen')
    
    arrow3 = FancyArrowPatch((13.25, 5.4), (10, 4.6), arrowstyle='->', 
                            mutation_scale=30, linewidth=3, color='darkred')
    ax.add_patch(arrow3)
    ax.text(12, 5.2, 'q₁, q₃', fontsize=13, fontweight='bold', color='darkred')
    
    # Outcome box (bottom)
    outcome_box = FancyBboxPatch((3, 0.3), 10, 1.2, boxstyle="round,pad=0.1",
                                 edgecolor='purple', facecolor='lavender', linewidth=3, alpha=0.9)
    ax.add_patch(outcome_box)
    ax.text(8, 1.1, 'Therapeutic Outcome: χ = 6.9  (Regime Stability)', 
            fontsize=15, fontweight='bold', ha='center')
    ax.text(8, 0.6, 'Collapse metric exceeds healthy baseline (χ_healthy = 5.2)', 
            fontsize=12, ha='center')
    
    # Arrow from quaternion to outcome
    arrow_out = FancyArrowPatch((8, 1.9), (8, 1.6), arrowstyle='->', 
                               mutation_scale=30, linewidth=3, color='purple')
    ax.add_patch(arrow_out)
    
    plt.tight_layout()
    filename = f'{FIGURE_DIR}/system_schematic.png'
    plt.savefig(filename, dpi=600, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f"Schematic saved: {filename}")
    return filename

if __name__ == '__main__':
    import os
    os.makedirs(FIGURE_DIR, exist_ok=True)
    
    schematic = generate_schematic()
    print(f"\nSchematic created: {schematic}")

"""
Recreate Original REN-01 System Schematic from Manuscript
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

FIGURE_DIR = '../figures'

def generate_original_schematic():
    print("Generating original system schematic...")
    
    fig, ax = plt.subplots(figsize=(22, 15))
    ax.set_xlim(0, 22)
    ax.set_ylim(0, 15)
    ax.axis('off')
    
    # Title with background
    title_box = FancyBboxPatch((2, 13.8), 18, 0.8, boxstyle="round,pad=0.1",
                              edgecolor='darkblue', facecolor='lightcyan', linewidth=3)
    ax.add_patch(title_box)
    ax.text(11, 14.2, 'REN-01: Complete Blood Brain Barrier Drug Delivery System', 
            fontsize=20, fontweight='bold', ha='center')
    
    # Left column boxes (formulation/delivery)
    left_boxes = [
        (1, 11, 4, 1.2, 'lightblue', 'A. MIF Stealth Complex', 
         ['Receptor + Nanocarrier', 'Stealth + Facile Biosensors', 'Minimal + Immune Activation']),
        (1, 9.3, 4, 1.2, 'lightblue', 'B. PEGylated Lipid Bilayer',
         ['Lipid Bilayer Core (DSPE-PEG)', 'Stealth Coating (PEG Layer)', 'Active Targeting (Transferrin)']),
        (1, 7.6, 4, 1.2, 'lightblue', 'B. PEGylated Lipid Bilayer',
         ['Lipid Bilayer Core (DSPE-PEG)', 'Stealth Coating (PEG Layer)', 'Active Targeting (Transferrin)']),
        (1, 5.9, 4, 1.2, 'lightgreen', 'D. Transferrin Linker System',
         ['Surface Transferrin Conjugation', 'BBB Receptor Targeting', 'Receptor-Ligand Uptake']),
        (1, 4.2, 4, 1.2, 'lightgreen', 'E. BBB Penetration Matrix',
         ['Permeability Coefficient', 'Receptor Saturation', 'Uptake Efficiency']),
        (1, 2.5, 4, 1.2, 'lightyellow', 'F. CSF Barrier Protocol',
         ['Clearance + CSF Efflux', 'Penetration Mechanism', 'Protein Binding'])
    ]
    
    for x, y, w, h, color, title, items in left_boxes:
        box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05",
                            edgecolor='black', facecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x + w/2, y + h - 0.15, title, fontsize=10, fontweight='bold', ha='center', va='top')
        for i, item in enumerate(items):
            ax.text(x + w/2, y + h - 0.35 - i*0.25, item, fontsize=8, ha='center', va='top')
    
    # Right column boxes (targets/mechanisms)
    right_boxes = [
        (15, 11, 4, 1.2, 'lightpink', '1. Enhanced Drugs',
         ['Nrf2-mediated uptake', 'Glutathione + Lysosomal', 'Astrocyte Targeting']),
        (15, 9.3, 4, 1.2, 'lightpink', '2. Activation Trigger',
         ['Dual Ligand + MOR Activation', 'Entropy Modulation', 'Integrated Feedback Loop']),
        (15, 7.6, 4, 1.2, 'lightblue', '3. Dual Target Release',
         ['Dopaminergic Activation', 'Astrocyte Modulation', 'Neuronal-Glial Coupling']),
        (15, 4.2, 4, 1.2, 'lightgreen', '5. Neuronal Circuitry',
         ['Dopaminergic Restoration', 'Neuronal Glial Coupling', 'Entropy Stabilization']),
        (15, 2.5, 4, 1.2, 'lightgreen', '6. Therapeutic Outcomes',
         ['Symptom Alleviation', 'Dopamine Axis Stability', 'Neuronal Circuit Integrity'])
    ]
    
    for x, y, w, h, color, title, items in right_boxes:
        box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05",
                            edgecolor='black', facecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x + w/2, y + h - 0.15, title, fontsize=10, fontweight='bold', ha='center', va='top')
        for i, item in enumerate(items):
            ax.text(x + w/2, y + h - 0.35 - i*0.25, item, fontsize=8, ha='center', va='top')
    
    # Two side by side boxes for row 4
    box4a = FancyBboxPatch((15, 5.9), 1.9, 1.2, boxstyle="round,pad=0.05",
                          edgecolor='black', facecolor='lightblue', linewidth=2)
    ax.add_patch(box4a)
    ax.text(15.95, 6.95, '4A. MOR-biased Core Packaging', fontsize=9, fontweight='bold', ha='center', va='top')
    for i, item in enumerate(['Selective Receptor Activation', 'Dopamine Pathway Engagement', 'Reduced Beta-Arrestin']):
        ax.text(15.95, 6.7 - i*0.25, item, fontsize=7, ha='center', va='top')
    
    box4b = FancyBboxPatch((17.1, 5.9), 1.9, 1.2, boxstyle="round,pad=0.05",
                          edgecolor='black', facecolor='plum', linewidth=2)
    ax.add_patch(box4b)
    ax.text(18.05, 6.95, '4B. CB2 Ligand Pathways', fontsize=9, fontweight='bold', ha='center', va='top')
    for i, item in enumerate(['CB2 Receptor Targeting', 'Anti-inflammatory Response', 'Neuroprotective Signaling']):
        ax.text(18.05, 6.7 - i*0.25, item, fontsize=7, ha='center', va='top')
    
    # BBB barrier (center red dashed line with gradient effect)
    ax.plot([11, 11], [2, 13], 'r--', linewidth=5, alpha=0.8, zorder=1)
    ax.fill_between([10.8, 11.2], 2, 13, color='red', alpha=0.1, zorder=0)
    
    # Vertical BBB label
    bbb_box = FancyBboxPatch((10.3, 6.5), 1.4, 1.2, boxstyle="round,pad=0.1",
                            edgecolor='darkred', facecolor='mistyrose', linewidth=3, alpha=0.95)
    ax.add_patch(bbb_box)
    ax.text(11, 7.3, 'BLOOD-BRAIN', fontsize=12, fontweight='bold', ha='center', color='darkred')
    ax.text(11, 6.9, 'BARRIER', fontsize=12, fontweight='bold', ha='center', color='darkred')
    
    # Arrows from left to right with better styling
    arrow_ys = [11.6, 9.9, 8.2, 6.5, 4.8, 3.1]
    for i, y in enumerate(arrow_ys):
        arrow = FancyArrowPatch((5.3, y), (15.8, y), arrowstyle='->', 
                               mutation_scale=25, linewidth=3, color='steelblue', alpha=0.7,
                               connectionstyle="arc3,rad=0.1")
        ax.add_patch(arrow)
    
    # Vertical arrows on right side with better styling
    for i in range(len(right_boxes)-1):
        y_start = right_boxes[i][1]
        y_end = right_boxes[i+1][1] + right_boxes[i+1][3]
        arrow = FancyArrowPatch((18, y_start), (18, y_end), arrowstyle='->', 
                               mutation_scale=25, linewidth=3, color='darkgreen', alpha=0.7)
        ax.add_patch(arrow)
    
    # Bottom box with better styling
    bottom_box = FancyBboxPatch((1, 0.3), 20, 1.7, boxstyle="round,pad=0.1",
                               edgecolor='darkgoldenrod', facecolor='wheat', linewidth=3, alpha=0.95)
    ax.add_patch(bottom_box)
    ax.text(10, 1.7, 'Key Interventions: MIF-Targeted Nanocarrier Framework - BBB-Based Drug Delivery - Proof-of-Concept', 
            fontsize=10, fontweight='bold', ha='center')
    ax.text(10, 1.35, 'MIF-Stabilization - BBB-Receptor-Ligand Uptake - PEGylation-Linker - Transferrin-Mediated Transport', 
            fontsize=8, ha='center')
    ax.text(10, 1.05, 'Entropy-Modulation - Astrocyte-Neuronal Coupling - Dopaminergic-Restoration - Therapeutic-Outcomes', 
            fontsize=8, ha='center')
    ax.text(10, 0.75, 'EntPTC2-Framework - MOR-CB2-Ligand-Pairing - TRV130-Derivative-Variant', 
            fontsize=8, ha='center')
    
    plt.tight_layout()
    filename = f'{FIGURE_DIR}/system_schematic.png'
    plt.savefig(filename, dpi=600, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f"Schematic saved: {filename}")
    return filename

if __name__ == '__main__':
    import os
    os.makedirs(FIGURE_DIR, exist_ok=True)
    
    schematic = generate_original_schematic()
    print(f"\nSchematic created: {schematic}")

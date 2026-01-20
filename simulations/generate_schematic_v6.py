#!/usr/bin/env python3
"""Generate system schematic - MUCH LARGER TEXT."""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(1, 1, figsize=(48, 36), dpi=300)
ax.set_xlim(0, 48)
ax.set_ylim(0, 36)
ax.axis('off')
ax.set_facecolor('#F5F5DC')

# Title box at top
title_box = FancyBboxPatch((1, 33), 46, 2.5, boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#E8F5E9', edgecolor='#2E7D32', linewidth=4)
ax.add_patch(title_box)
ax.text(24, 34.25, 'REN-01: Complete Blood Brain Barrier Drug Delivery System', 
        fontsize=36, fontweight='bold', ha='center', va='center')

# BBB vertical dashed line
bbb_x = 18
ax.plot([bbb_x, bbb_x], [4, 32], color='#D32F2F', linestyle='--', linewidth=6, alpha=0.8)

# BBB label
ax.text(18, 18, 'BLOOD-BRAIN\nBARRIER', fontsize=24, fontweight='bold', ha='center', va='center', 
        color='#D32F2F', bbox=dict(boxstyle='round', facecolor='#FFCDD2', edgecolor='#D32F2F', linewidth=4, pad=0.8))

# LEFT COLUMN
left_x = 8
left_width = 12
box_height = 4.5
left_right_edge = left_x + left_width/2

left_boxes = [
    ('A. MIF Stealth Complex', ['Receptor + Nanocarrier', 'Stealth + Facile Biosensors', 'Minimal + Immune Activation'], 29),
    ('B. PEGylated Lipid Bilayer', ['Lipid Bilayer Core (DSPE-PEG)', 'Stealth Coating (PEG Layer)', 'Active Targeting (Transferrin)'], 23),
    ('C. PEGylated Lipid Bilayer', ['Lipid Bilayer Core (DSPE-PEG)', 'Stealth Coating (PEG Layer)', 'Active Targeting (Transferrin)'], 17),
    ('D. Transferrin Linker System', ['Surface Transferrin Conjugation', 'BBB Receptor Targeting', 'Receptor-Ligand Uptake'], 11),
    ('E. BBB Penetration Matrix', ['Permeability Coefficient', 'Receptor Saturation', 'Uptake Efficiency'], 5),
]

for title, items, y in left_boxes:
    box = FancyBboxPatch((left_x - left_width/2, y - box_height/2), left_width, box_height,
                          boxstyle="round,pad=0.02,rounding_size=0.08",
                          facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=3)
    ax.add_patch(box)
    ax.text(left_x, y + 1.3, title, fontsize=20, fontweight='bold', ha='center', va='center')
    for i, item in enumerate(items):
        ax.text(left_x, y + 0.3 - i*0.9, item, fontsize=16, ha='center', va='center')

# RIGHT COLUMN
right_x = 40
right_width = 12
right_left_edge = right_x - right_width/2

right_boxes = [
    ('1. Enhanced Drugs', ['Nrf2-mediated uptake', 'Glutathione + Lysosomal', 'Astrocyte Targeting'], 29, '#E8F5E9', '#388E3C'),
    ('2. Activation Trigger', ['Dual Ligand + MOR Activation', 'Entropy Modulation', 'Integrated Feedback Loop'], 23, '#FCE4EC', '#C2185B'),
    ('3. Dual Target Release', ['Dopaminergic Activation', 'Astrocyte Modulation', 'Neuronal-Glial Coupling'], 17, '#E8F5E9', '#388E3C'),
    ('5. Neuronal Circuitry', ['Dopaminergic Restoration', 'Neuronal Glial Coupling', 'Entropy Stabilization'], 5, '#E8F5E9', '#388E3C'),
]

for title, items, y, facecolor, edgecolor in right_boxes:
    box = FancyBboxPatch((right_left_edge, y - box_height/2), right_width, box_height,
                          boxstyle="round,pad=0.02,rounding_size=0.08",
                          facecolor=facecolor, edgecolor=edgecolor, linewidth=3)
    ax.add_patch(box)
    ax.text(right_x, y + 1.3, title, fontsize=20, fontweight='bold', ha='center', va='center')
    for i, item in enumerate(items):
        ax.text(right_x, y + 0.3 - i*0.9, item, fontsize=16, ha='center', va='center')

# 4A and 4B boxes
box_4a = FancyBboxPatch((24, 9.25), 8, 4.5, boxstyle="round,pad=0.02,rounding_size=0.08",
                         facecolor='#FCE4EC', edgecolor='#C2185B', linewidth=3)
ax.add_patch(box_4a)
ax.text(28, 12.8, '4A. MOR-biased Core', fontsize=18, fontweight='bold', ha='center', va='center')
ax.text(28, 11.7, 'Selective Receptor Activation', fontsize=14, ha='center', va='center')
ax.text(28, 10.8, 'Dopamine Pathway Engagement', fontsize=14, ha='center', va='center')
ax.text(28, 9.9, 'Reduced Beta-Arrestin', fontsize=14, ha='center', va='center')

box_4b = FancyBboxPatch((33, 9.25), 8, 4.5, boxstyle="round,pad=0.02,rounding_size=0.08",
                         facecolor='#E8F5E9', edgecolor='#388E3C', linewidth=3)
ax.add_patch(box_4b)
ax.text(37, 12.8, '4B. CB2 Ligand Pathways', fontsize=18, fontweight='bold', ha='center', va='center')
ax.text(37, 11.7, 'CB2 Receptor Targeting', fontsize=14, ha='center', va='center')
ax.text(37, 10.8, 'Anti-inflammatory Response', fontsize=14, ha='center', va='center')
ax.text(37, 9.9, 'Neuroprotective Signaling', fontsize=14, ha='center', va='center')

# HORIZONTAL ARROWS - in gaps between rows
arrow_gap_y = [26, 20, 14, 8, 2]

for y in arrow_gap_y:
    ax.annotate('', xy=(right_left_edge - 0.5, y), xytext=(left_right_edge + 0.5, y),
                arrowprops=dict(arrowstyle='->', color='#1976D2', lw=4))

# VERTICAL ARROWS on right side - outside boxes
arrow_x_right = 47

vertical_arrows = [
    (29 - box_height/2 - 0.3, 23 + box_height/2 + 0.3),
    (23 - box_height/2 - 0.3, 17 + box_height/2 + 0.3),
    (17 - box_height/2 - 0.3, 11 + box_height/2 + 0.3),
    (11 - box_height/2 - 0.3, 5 + box_height/2 + 0.3),
]

for y_start, y_end in vertical_arrows:
    ax.annotate('', xy=(arrow_x_right, y_end), xytext=(arrow_x_right, y_start),
                arrowprops=dict(arrowstyle='->', color='#388E3C', lw=4))

# Bottom summary box
summary_box = FancyBboxPatch((1, 0.3), 46, 3, boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor='#FFF8E1', edgecolor='#FF8F00', linewidth=4)
ax.add_patch(summary_box)
ax.text(24, 2.5, 'Key Interventions: MIF-Targeted Nanocarrier Framework - BBB-Based Drug Delivery - Proof-of-Concept', 
        fontsize=22, fontweight='bold', ha='center', va='center')
ax.text(24, 1.5, 'MIF-Stabilization - BBB-Receptor-Ligand Uptake - PEGylation-Linker - Transferrin-Mediated Transport', 
        fontsize=18, ha='center', va='center')
ax.text(24, 0.7, 'Entropy-Modulation - Astrocyte-Neuronal Coupling - Dopaminergic-Restoration - TRV130-Derivative', 
        fontsize=18, ha='center', va='center')

plt.tight_layout()
plt.savefig('/home/ubuntu/REN-01-repo/figures/system_schematic.png', dpi=300, bbox_inches='tight',
            facecolor='#F5F5DC', edgecolor='none')
plt.close()

print("Schematic v6 generated: figures/system_schematic.png")

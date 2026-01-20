#!/usr/bin/env python3
"""Generate system schematic - LARGE TEXT, no overlapping."""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(1, 1, figsize=(36, 26), dpi=300)
ax.set_xlim(0, 36)
ax.set_ylim(0, 26)
ax.axis('off')
ax.set_facecolor('#F5F5DC')

# Title box at top
title_box = FancyBboxPatch((1, 24), 34, 1.8, boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#E8F5E9', edgecolor='#2E7D32', linewidth=3)
ax.add_patch(title_box)
ax.text(18, 24.9, 'REN-01: Complete Blood Brain Barrier Drug Delivery System', 
        fontsize=24, fontweight='bold', ha='center', va='center')

# BBB vertical dashed line
bbb_x = 14
ax.plot([bbb_x, bbb_x], [3, 23], color='#D32F2F', linestyle='--', linewidth=5, alpha=0.8)

# BBB label
ax.text(14, 13, 'BLOOD-BRAIN\nBARRIER', fontsize=16, fontweight='bold', ha='center', va='center', 
        color='#D32F2F', bbox=dict(boxstyle='round', facecolor='#FFCDD2', edgecolor='#D32F2F', linewidth=3, pad=0.6))

# LEFT COLUMN
left_x = 6
left_width = 8
box_height = 3
left_right_edge = left_x + left_width/2

left_boxes = [
    ('A. MIF Stealth Complex', ['Receptor + Nanocarrier', 'Stealth + Facile Biosensors', 'Minimal + Immune Activation'], 21),
    ('B. PEGylated Lipid Bilayer', ['Lipid Bilayer Core (DSPE-PEG)', 'Stealth Coating (PEG Layer)', 'Active Targeting (Transferrin)'], 17),
    ('C. PEGylated Lipid Bilayer', ['Lipid Bilayer Core (DSPE-PEG)', 'Stealth Coating (PEG Layer)', 'Active Targeting (Transferrin)'], 13),
    ('D. Transferrin Linker System', ['Surface Transferrin Conjugation', 'BBB Receptor Targeting', 'Receptor-Ligand Uptake'], 9),
    ('E. BBB Penetration Matrix', ['Permeability Coefficient', 'Receptor Saturation', 'Uptake Efficiency'], 5),
]

for title, items, y in left_boxes:
    box = FancyBboxPatch((left_x - left_width/2, y - box_height/2), left_width, box_height,
                          boxstyle="round,pad=0.02,rounding_size=0.08",
                          facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=2)
    ax.add_patch(box)
    ax.text(left_x, y + 0.9, title, fontsize=14, fontweight='bold', ha='center', va='center')
    for i, item in enumerate(items):
        ax.text(left_x, y + 0.2 - i*0.55, item, fontsize=12, ha='center', va='center')

# RIGHT COLUMN
right_x = 30
right_width = 8
right_left_edge = right_x - right_width/2

right_boxes = [
    ('1. Enhanced Drugs', ['Nrf2-mediated uptake', 'Glutathione + Lysosomal', 'Astrocyte Targeting'], 21, '#E8F5E9', '#388E3C'),
    ('2. Activation Trigger', ['Dual Ligand + MOR Activation', 'Entropy Modulation', 'Integrated Feedback Loop'], 17, '#FCE4EC', '#C2185B'),
    ('3. Dual Target Release', ['Dopaminergic Activation', 'Astrocyte Modulation', 'Neuronal-Glial Coupling'], 13, '#E8F5E9', '#388E3C'),
    ('5. Neuronal Circuitry', ['Dopaminergic Restoration', 'Neuronal Glial Coupling', 'Entropy Stabilization'], 5, '#E8F5E9', '#388E3C'),
]

for title, items, y, facecolor, edgecolor in right_boxes:
    box = FancyBboxPatch((right_left_edge, y - box_height/2), right_width, box_height,
                          boxstyle="round,pad=0.02,rounding_size=0.08",
                          facecolor=facecolor, edgecolor=edgecolor, linewidth=2)
    ax.add_patch(box)
    ax.text(right_x, y + 0.9, title, fontsize=14, fontweight='bold', ha='center', va='center')
    for i, item in enumerate(items):
        ax.text(right_x, y + 0.2 - i*0.55, item, fontsize=12, ha='center', va='center')

# 4A and 4B boxes
box_4a = FancyBboxPatch((18, 7.5), 5.5, 3, boxstyle="round,pad=0.02,rounding_size=0.08",
                         facecolor='#FCE4EC', edgecolor='#C2185B', linewidth=2)
ax.add_patch(box_4a)
ax.text(20.75, 9.9, '4A. MOR-biased Core', fontsize=12, fontweight='bold', ha='center', va='center')
ax.text(20.75, 9.2, 'Selective Receptor Activation', fontsize=10, ha='center', va='center')
ax.text(20.75, 8.6, 'Dopamine Pathway Engagement', fontsize=10, ha='center', va='center')
ax.text(20.75, 8.0, 'Reduced Beta-Arrestin', fontsize=10, ha='center', va='center')

box_4b = FancyBboxPatch((24, 7.5), 5.5, 3, boxstyle="round,pad=0.02,rounding_size=0.08",
                         facecolor='#E8F5E9', edgecolor='#388E3C', linewidth=2)
ax.add_patch(box_4b)
ax.text(26.75, 9.9, '4B. CB2 Ligand Pathways', fontsize=12, fontweight='bold', ha='center', va='center')
ax.text(26.75, 9.2, 'CB2 Receptor Targeting', fontsize=10, ha='center', va='center')
ax.text(26.75, 8.6, 'Anti-inflammatory Response', fontsize=10, ha='center', va='center')
ax.text(26.75, 8.0, 'Neuroprotective Signaling', fontsize=10, ha='center', va='center')

# HORIZONTAL ARROWS - in gaps between rows
arrow_gap_y = [19, 15, 11, 7, 3]

for y in arrow_gap_y:
    ax.annotate('', xy=(right_left_edge - 0.3, y), xytext=(left_right_edge + 0.3, y),
                arrowprops=dict(arrowstyle='->', color='#1976D2', lw=3))

# VERTICAL ARROWS on right side - outside boxes
arrow_x_right = 35

vertical_arrows = [
    (21 - box_height/2 - 0.2, 17 + box_height/2 + 0.2),
    (17 - box_height/2 - 0.2, 13 + box_height/2 + 0.2),
    (13 - box_height/2 - 0.2, 9 + box_height/2 + 0.2),
    (9 - box_height/2 - 0.2, 5 + box_height/2 + 0.2),
]

for y_start, y_end in vertical_arrows:
    ax.annotate('', xy=(arrow_x_right, y_end), xytext=(arrow_x_right, y_start),
                arrowprops=dict(arrowstyle='->', color='#388E3C', lw=3))

# Bottom summary box
summary_box = FancyBboxPatch((1, 0.3), 34, 2.2, boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor='#FFF8E1', edgecolor='#FF8F00', linewidth=3)
ax.add_patch(summary_box)
ax.text(18, 2.0, 'Key Interventions: MIF-Targeted Nanocarrier Framework - BBB-Based Drug Delivery - Proof-of-Concept', 
        fontsize=16, fontweight='bold', ha='center', va='center')
ax.text(18, 1.2, 'MIF-Stabilization - BBB-Receptor-Ligand Uptake - PEGylation-Linker - Transferrin-Mediated Transport', 
        fontsize=13, ha='center', va='center')
ax.text(18, 0.6, 'Entropy-Modulation - Astrocyte-Neuronal Coupling - Dopaminergic-Restoration - TRV130-Derivative', 
        fontsize=13, ha='center', va='center')

plt.tight_layout()
plt.savefig('/home/ubuntu/REN-01-repo/figures/system_schematic.png', dpi=300, bbox_inches='tight',
            facecolor='#F5F5DC', edgecolor='none')
plt.close()

print("Schematic v5 generated: figures/system_schematic.png")

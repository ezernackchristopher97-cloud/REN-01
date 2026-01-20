#!/usr/bin/env python3
"""Generate system schematic - EVEN LARGER TEXT."""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(1, 1, figsize=(60, 44), dpi=300)
ax.set_xlim(0, 60)
ax.set_ylim(0, 44)
ax.axis('off')
ax.set_facecolor('#F5F5DC')

# Title box at top
title_box = FancyBboxPatch((1, 40), 58, 3.5, boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#E8F5E9', edgecolor='#2E7D32', linewidth=5)
ax.add_patch(title_box)
ax.text(30, 41.75, 'REN-01: Complete Blood Brain Barrier Drug Delivery System', 
        fontsize=48, fontweight='bold', ha='center', va='center')

# BBB vertical dashed line
bbb_x = 22
ax.plot([bbb_x, bbb_x], [5, 39], color='#D32F2F', linestyle='--', linewidth=8, alpha=0.8)

# BBB label
ax.text(22, 22, 'BLOOD-BRAIN\nBARRIER', fontsize=32, fontweight='bold', ha='center', va='center', 
        color='#D32F2F', bbox=dict(boxstyle='round', facecolor='#FFCDD2', edgecolor='#D32F2F', linewidth=5, pad=1.0))

# LEFT COLUMN
left_x = 10
left_width = 16
box_height = 6
left_right_edge = left_x + left_width/2

left_boxes = [
    ('A. MIF Stealth Complex', ['Receptor + Nanocarrier', 'Stealth + Facile Biosensors', 'Minimal + Immune Activation'], 35),
    ('B. PEGylated Lipid Bilayer', ['Lipid Bilayer Core (DSPE-PEG)', 'Stealth Coating (PEG Layer)', 'Active Targeting (Transferrin)'], 27),
    ('C. PEGylated Lipid Bilayer', ['Lipid Bilayer Core (DSPE-PEG)', 'Stealth Coating (PEG Layer)', 'Active Targeting (Transferrin)'], 19),
    ('D. Transferrin Linker System', ['Surface Transferrin Conjugation', 'BBB Receptor Targeting', 'Receptor-Ligand Uptake'], 11),
]

for title, items, y in left_boxes:
    box = FancyBboxPatch((left_x - left_width/2, y - box_height/2), left_width, box_height,
                          boxstyle="round,pad=0.02,rounding_size=0.08",
                          facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=4)
    ax.add_patch(box)
    ax.text(left_x, y + 1.8, title, fontsize=28, fontweight='bold', ha='center', va='center')
    for i, item in enumerate(items):
        ax.text(left_x, y + 0.4 - i*1.2, item, fontsize=22, ha='center', va='center')

# RIGHT COLUMN
right_x = 50
right_width = 16
right_left_edge = right_x - right_width/2

right_boxes = [
    ('1. Enhanced Drugs', ['Nrf2-mediated uptake', 'Glutathione + Lysosomal', 'Astrocyte Targeting'], 35, '#E8F5E9', '#388E3C'),
    ('2. Activation Trigger', ['Dual Ligand + MOR Activation', 'Entropy Modulation', 'Integrated Feedback Loop'], 27, '#FCE4EC', '#C2185B'),
    ('3. Dual Target Release', ['Dopaminergic Activation', 'Astrocyte Modulation', 'Neuronal-Glial Coupling'], 19, '#E8F5E9', '#388E3C'),
    ('5. Neuronal Circuitry', ['Dopaminergic Restoration', 'Neuronal Glial Coupling', 'Entropy Stabilization'], 5, '#E8F5E9', '#388E3C'),
]

for title, items, y, facecolor, edgecolor in right_boxes:
    box = FancyBboxPatch((right_left_edge, y - box_height/2), right_width, box_height,
                          boxstyle="round,pad=0.02,rounding_size=0.08",
                          facecolor=facecolor, edgecolor=edgecolor, linewidth=4)
    ax.add_patch(box)
    ax.text(right_x, y + 1.8, title, fontsize=28, fontweight='bold', ha='center', va='center')
    for i, item in enumerate(items):
        ax.text(right_x, y + 0.4 - i*1.2, item, fontsize=22, ha='center', va='center')

# 4A and 4B boxes
box_4a = FancyBboxPatch((30, 9), 11, 6, boxstyle="round,pad=0.02,rounding_size=0.08",
                         facecolor='#FCE4EC', edgecolor='#C2185B', linewidth=4)
ax.add_patch(box_4a)
ax.text(35.5, 13.5, '4A. MOR-biased Core', fontsize=24, fontweight='bold', ha='center', va='center')
ax.text(35.5, 12, 'Selective Receptor Activation', fontsize=20, ha='center', va='center')
ax.text(35.5, 10.8, 'Dopamine Pathway Engagement', fontsize=20, ha='center', va='center')
ax.text(35.5, 9.6, 'Reduced Beta-Arrestin', fontsize=20, ha='center', va='center')

box_4b = FancyBboxPatch((42, 9), 11, 6, boxstyle="round,pad=0.02,rounding_size=0.08",
                         facecolor='#E8F5E9', edgecolor='#388E3C', linewidth=4)
ax.add_patch(box_4b)
ax.text(47.5, 13.5, '4B. CB2 Ligand Pathways', fontsize=24, fontweight='bold', ha='center', va='center')
ax.text(47.5, 12, 'CB2 Receptor Targeting', fontsize=20, ha='center', va='center')
ax.text(47.5, 10.8, 'Anti-inflammatory Response', fontsize=20, ha='center', va='center')
ax.text(47.5, 9.6, 'Neuroprotective Signaling', fontsize=20, ha='center', va='center')

# HORIZONTAL ARROWS - in gaps between rows
arrow_gap_y = [31, 23, 15, 7]

for y in arrow_gap_y:
    ax.annotate('', xy=(right_left_edge - 0.5, y), xytext=(left_right_edge + 0.5, y),
                arrowprops=dict(arrowstyle='->', color='#1976D2', lw=5))

# VERTICAL ARROWS on right side - outside boxes
arrow_x_right = 59

vertical_arrows = [
    (35 - box_height/2 - 0.5, 27 + box_height/2 + 0.5),
    (27 - box_height/2 - 0.5, 19 + box_height/2 + 0.5),
    (19 - box_height/2 - 0.5, 11 + box_height/2 + 0.5),
    (11 - box_height/2 - 0.5, 5 + box_height/2 + 0.5),
]

for y_start, y_end in vertical_arrows:
    ax.annotate('', xy=(arrow_x_right, y_end), xytext=(arrow_x_right, y_start),
                arrowprops=dict(arrowstyle='->', color='#388E3C', lw=5))

# Bottom summary box
summary_box = FancyBboxPatch((1, 0.5), 58, 4, boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor='#FFF8E1', edgecolor='#FF8F00', linewidth=5)
ax.add_patch(summary_box)
ax.text(30, 3.5, 'Key Interventions: MIF-Targeted Nanocarrier Framework - BBB-Based Drug Delivery', 
        fontsize=28, fontweight='bold', ha='center', va='center')
ax.text(30, 2.0, 'MIF-Stabilization - BBB-Receptor-Ligand Uptake - PEGylation-Linker - Transferrin-Mediated Transport', 
        fontsize=24, ha='center', va='center')
ax.text(30, 0.9, 'Entropy-Modulation - Astrocyte-Neuronal Coupling - Dopaminergic-Restoration - TRV130-Derivative', 
        fontsize=24, ha='center', va='center')

plt.tight_layout()
plt.savefig('/home/ubuntu/REN-01-repo/figures/system_schematic.png', dpi=300, bbox_inches='tight',
            facecolor='#F5F5DC', edgecolor='none')
plt.close()

print("Schematic v7 generated: figures/system_schematic.png")

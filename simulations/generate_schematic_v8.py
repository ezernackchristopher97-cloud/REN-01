#!/usr/bin/env python3
"""Generate system schematic - LARGER BOXES, NO OVERLAPPING."""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(1, 1, figsize=(50, 40), dpi=200)
ax.set_xlim(0, 100)
ax.set_ylim(0, 80)
ax.axis('off')
ax.set_facecolor('#F5F5DC')

# Title box at top
title_box = FancyBboxPatch((2, 74), 96, 5, boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#E8F5E9', edgecolor='#2E7D32', linewidth=6)
ax.add_patch(title_box)
ax.text(50, 76.5, 'REN-01: Complete Blood Brain Barrier Drug Delivery System', 
        fontsize=72, fontweight='bold', ha='center', va='center')

# BBB vertical dashed line
bbb_x = 40
ax.plot([bbb_x, bbb_x], [8, 72], color='#D32F2F', linestyle='--', linewidth=8, alpha=0.8)

# BBB label - positioned in gap between rows 2 and 3
ax.text(40, 45, 'BLOOD-BRAIN\nBARRIER', fontsize=48, fontweight='bold', ha='center', va='center', 
        color='#D32F2F', bbox=dict(boxstyle='round', facecolor='#FFCDD2', edgecolor='#D32F2F', linewidth=5, pad=1.0))

# LEFT COLUMN
left_x = 18
left_width = 28
box_height = 11

left_boxes = [
    ('A. MIF Stealth Complex', ['Receptor + Nanocarrier', 'Stealth + Facile Biosensors', 'Minimal + Immune Activation'], 66),
    ('B. PEGylated Lipid Bilayer', ['Lipid Bilayer Core (DSPE-PEG)', 'Stealth Coating (PEG Layer)', 'Active Targeting (Transferrin)'], 53),
    ('D. Transferrin Linker System', ['Surface Transferrin Conjugation', 'BBB Receptor Targeting', 'Receptor-Ligand Uptake'], 27),
    ('E. BBB Penetration Matrix', ['Permeability Coefficient', 'Receptor Saturation', 'Uptake Efficiency'], 14),
]

for title, items, y in left_boxes:
    box = FancyBboxPatch((left_x - left_width/2, y - box_height/2), left_width, box_height,
                          boxstyle="round,pad=0.02,rounding_size=0.08",
                          facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=4)
    ax.add_patch(box)
    ax.text(left_x, y + 3.5, title, fontsize=44, fontweight='bold', ha='center', va='center')
    for i, item in enumerate(items):
        ax.text(left_x, y + 1 - i*2.2, item, fontsize=36, ha='center', va='center')

# RIGHT COLUMN
right_x = 82
right_width = 28

right_boxes = [
    ('1. Enhanced Drugs', ['Nrf2-mediated uptake', 'Glutathione + Lysosomal', 'Astrocyte Targeting'], 66, '#E8F5E9', '#388E3C'),
    ('2. Activation Trigger', ['Dual Ligand + MOR Activation', 'Entropy Modulation', 'Integrated Feedback Loop'], 53, '#FCE4EC', '#C2185B'),
    ('4. Receptor Pathways', ['MOR-biased Signaling', 'CB2 Ligand Activation', 'Reduced Beta-Arrestin'], 27, '#FCE4EC', '#C2185B'),
    ('5. Neuronal Circuitry', ['Dopaminergic Restoration', 'Neuronal Glial Coupling', 'Entropy Stabilization'], 14, '#E8F5E9', '#388E3C'),
]

for title, items, y, facecolor, edgecolor in right_boxes:
    box = FancyBboxPatch((right_x - right_width/2, y - box_height/2), right_width, box_height,
                          boxstyle="round,pad=0.02,rounding_size=0.08",
                          facecolor=facecolor, edgecolor=edgecolor, linewidth=4)
    ax.add_patch(box)
    ax.text(right_x, y + 3.5, title, fontsize=44, fontweight='bold', ha='center', va='center')
    for i, item in enumerate(items):
        ax.text(right_x, y + 1 - i*2.2, item, fontsize=36, ha='center', va='center')

# HORIZONTAL ARROWS - in gaps between rows
left_edge = left_x + left_width/2
right_edge = right_x - right_width/2

arrow_y = [59.5, 40, 20.5]
for y in arrow_y:
    ax.annotate('', xy=(right_edge, y), xytext=(left_edge, y),
                arrowprops=dict(arrowstyle='->', color='#1976D2', lw=5))

# Bottom summary
summary_box = FancyBboxPatch((2, 1), 96, 5, boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor='#FFF8E1', edgecolor='#FF8F00', linewidth=5)
ax.add_patch(summary_box)
ax.text(50, 3.5, 'Key Interventions: MIF-Targeted Nanocarrier - BBB Drug Delivery - TRV130 Derivative - Entropy Modulation', 
        fontsize=40, fontweight='bold', ha='center', va='center')

plt.tight_layout()
plt.savefig('/home/ubuntu/REN-01-repo/figures/system_schematic.png', dpi=200, bbox_inches='tight',
            facecolor='#F5F5DC', edgecolor='none')
plt.close()

print("Schematic v8 generated")

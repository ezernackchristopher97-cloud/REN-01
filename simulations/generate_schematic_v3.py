#!/usr/bin/env python3
"""Generate system schematic - arrows end at box edges, no overlapping, larger text."""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(1, 1, figsize=(28, 20), dpi=300)
ax.set_xlim(0, 28)
ax.set_ylim(0, 20)
ax.axis('off')
ax.set_facecolor('#F5F5DC')

# Title box at top
title_box = FancyBboxPatch((1, 18), 26, 1.5, boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#E8F5E9', edgecolor='#2E7D32', linewidth=2)
ax.add_patch(title_box)
ax.text(14, 18.75, 'REN-01: Complete Blood Brain Barrier Drug Delivery System', 
        fontsize=18, fontweight='bold', ha='center', va='center')

# BBB vertical dashed line - in center
bbb_x = 14
ax.plot([bbb_x, bbb_x], [3, 17], color='#D32F2F', linestyle='--', linewidth=4, alpha=0.8)

# BBB label - just text, no box overlapping the line
ax.text(14, 10.5, 'BLOOD-BRAIN', fontsize=14, fontweight='bold', ha='center', va='center', 
        color='#D32F2F', bbox=dict(boxstyle='round', facecolor='#FFCDD2', edgecolor='#D32F2F', linewidth=2))
ax.text(14, 9.5, 'BARRIER', fontsize=14, fontweight='bold', ha='center', va='center', 
        color='#D32F2F', bbox=dict(boxstyle='round', facecolor='#FFCDD2', edgecolor='#D32F2F', linewidth=2))

# LEFT COLUMN positions
left_x = 4.5
left_width = 6
box_height = 2.2

left_boxes = [
    ('A. MIF Stealth Complex', ['Receptor + Nanocarrier', 'Stealth + Facile Biosensors', 'Minimal + Immune Activation'], 16),
    ('B. PEGylated Lipid Bilayer', ['Lipid Bilayer Core (DSPE-PEG)', 'Stealth Coating (PEG Layer)', 'Active Targeting (Transferrin)'], 13),
    ('C. PEGylated Lipid Bilayer', ['Lipid Bilayer Core (DSPE-PEG)', 'Stealth Coating (PEG Layer)', 'Active Targeting (Transferrin)'], 10),
    ('D. Transferrin Linker System', ['Surface Transferrin Conjugation', 'BBB Receptor Targeting', 'Receptor-Ligand Uptake'], 7),
    ('E. BBB Penetration Matrix', ['Permeability Coefficient', 'Receptor Saturation', 'Uptake Efficiency'], 4),
]

for title, items, y in left_boxes:
    box = FancyBboxPatch((left_x - left_width/2, y - box_height/2), left_width, box_height,
                          boxstyle="round,pad=0.02,rounding_size=0.08",
                          facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=2)
    ax.add_patch(box)
    ax.text(left_x, y + 0.6, title, fontsize=11, fontweight='bold', ha='center', va='center')
    for i, item in enumerate(items):
        ax.text(left_x, y + 0.1 - i*0.4, item, fontsize=9, ha='center', va='center')

# RIGHT COLUMN positions
right_x = 23.5
right_width = 6

right_boxes = [
    ('1. Enhanced Drugs', ['Nrf2-mediated uptake', 'Glutathione + Lysosomal', 'Astrocyte Targeting'], 16, '#E8F5E9', '#388E3C'),
    ('2. Activation Trigger', ['Dual Ligand + MOR Activation', 'Entropy Modulation', 'Integrated Feedback Loop'], 13, '#FCE4EC', '#C2185B'),
    ('3. Dual Target Release', ['Dopaminergic Activation', 'Astrocyte Modulation', 'Neuronal-Glial Coupling'], 10, '#E8F5E9', '#388E3C'),
    ('5. Neuronal Circuitry', ['Dopaminergic Restoration', 'Neuronal Glial Coupling', 'Entropy Stabilization'], 4, '#E8F5E9', '#388E3C'),
]

for title, items, y, facecolor, edgecolor in right_boxes:
    box = FancyBboxPatch((right_x - right_width/2, y - box_height/2), right_width, box_height,
                          boxstyle="round,pad=0.02,rounding_size=0.08",
                          facecolor=facecolor, edgecolor=edgecolor, linewidth=2)
    ax.add_patch(box)
    ax.text(right_x, y + 0.6, title, fontsize=11, fontweight='bold', ha='center', va='center')
    for i, item in enumerate(items):
        ax.text(right_x, y + 0.1 - i*0.4, item, fontsize=9, ha='center', va='center')

# 4A and 4B boxes at y=7
box_4a = FancyBboxPatch((17, 5.9), 4, 2.2, boxstyle="round,pad=0.02,rounding_size=0.08",
                         facecolor='#FCE4EC', edgecolor='#C2185B', linewidth=2)
ax.add_patch(box_4a)
ax.text(19, 7.5, '4A. MOR-biased Core', fontsize=10, fontweight='bold', ha='center', va='center')
ax.text(19, 7.0, 'Selective Receptor Activation', fontsize=8, ha='center', va='center')
ax.text(19, 6.6, 'Dopamine Pathway Engagement', fontsize=8, ha='center', va='center')
ax.text(19, 6.2, 'Reduced Beta-Arrestin', fontsize=8, ha='center', va='center')

box_4b = FancyBboxPatch((21.5, 5.9), 4, 2.2, boxstyle="round,pad=0.02,rounding_size=0.08",
                         facecolor='#E8F5E9', edgecolor='#388E3C', linewidth=2)
ax.add_patch(box_4b)
ax.text(23.5, 7.5, '4B. CB2 Ligand Pathways', fontsize=10, fontweight='bold', ha='center', va='center')
ax.text(23.5, 7.0, 'CB2 Receptor Targeting', fontsize=8, ha='center', va='center')
ax.text(23.5, 6.6, 'Anti-inflammatory Response', fontsize=8, ha='center', va='center')
ax.text(23.5, 6.2, 'Neuroprotective Signaling', fontsize=8, ha='center', va='center')

# HORIZONTAL ARROWS - from right edge of left boxes to left edge of right boxes
# Arrow y positions match box y positions
left_box_right_edge = left_x + left_width/2  # 7.5
right_box_left_edge = right_x - right_width/2  # 20.5

arrow_connections = [
    (16, 16),  # A -> 1
    (13, 13),  # B -> 2
    (10, 10),  # C -> 3
    (7, 7),    # D -> 4A/4B
    (4, 4),    # E -> 5
]

for left_y, right_y in arrow_connections:
    ax.annotate('', xy=(right_box_left_edge, right_y), xytext=(left_box_right_edge, left_y),
                arrowprops=dict(arrowstyle='->', color='#1976D2', lw=2))

# VERTICAL ARROWS on right side - outside the boxes
# From bottom of upper box to top of lower box
vertical_arrows = [
    (16 - box_height/2, 13 + box_height/2),  # 1 -> 2
    (13 - box_height/2, 10 + box_height/2),  # 2 -> 3
    (7 - box_height/2, 4 + box_height/2),    # 4 -> 5
]

arrow_x = right_x + right_width/2 + 0.5  # Outside right edge

for y_start, y_end in vertical_arrows:
    ax.annotate('', xy=(arrow_x, y_end), xytext=(arrow_x, y_start),
                arrowprops=dict(arrowstyle='->', color='#388E3C', lw=2))

# Bottom summary box
summary_box = FancyBboxPatch((1, 0.5), 26, 2, boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor='#FFF8E1', edgecolor='#FF8F00', linewidth=2)
ax.add_patch(summary_box)
ax.text(14, 2.0, 'Key Interventions: MIF-Targeted Nanocarrier Framework - BBB-Based Drug Delivery - Proof-of-Concept', 
        fontsize=12, fontweight='bold', ha='center', va='center')
ax.text(14, 1.4, 'MIF-Stabilization - BBB-Receptor-Ligand Uptake - PEGylation-Linker - Transferrin-Mediated Transport', 
        fontsize=10, ha='center', va='center')
ax.text(14, 0.9, 'Entropy-Modulation - Astrocyte-Neuronal Coupling - Dopaminergic-Restoration - TRV130-Derivative', 
        fontsize=10, ha='center', va='center')

plt.tight_layout()
plt.savefig('/home/ubuntu/REN-01-repo/figures/system_schematic.png', dpi=300, bbox_inches='tight',
            facecolor='#F5F5DC', edgecolor='none')
plt.close()

print("Schematic v3 generated: figures/system_schematic.png")

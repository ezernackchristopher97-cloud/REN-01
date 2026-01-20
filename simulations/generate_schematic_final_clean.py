#!/usr/bin/env python3
"""Generate system schematic - CLEAN, NO OVERLAPPING, LARGE TEXT."""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Much larger canvas with proper spacing
fig, ax = plt.subplots(1, 1, figsize=(40, 30), dpi=200)
ax.set_xlim(0, 80)
ax.set_ylim(0, 60)
ax.axis('off')
ax.set_facecolor('#F5F5DC')

# Title box at top - plenty of space
title_box = FancyBboxPatch((2, 55), 76, 4, boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#E8F5E9', edgecolor='#2E7D32', linewidth=6)
ax.add_patch(title_box)
ax.text(40, 57, 'REN-01: Complete Blood Brain Barrier Drug Delivery System', 
        fontsize=84, fontweight='bold', ha='center', va='center')

# BBB vertical dashed line - in the middle
bbb_x = 30
ax.plot([bbb_x, bbb_x], [6, 52], color='#D32F2F', linestyle='--', linewidth=10, alpha=0.8)

# BBB label - positioned to not overlap anything
ax.text(30, 30, 'BLOOD-BRAIN\nBARRIER', fontsize=60, fontweight='bold', ha='center', va='center', 
        color='#D32F2F', bbox=dict(boxstyle='round', facecolor='#FFCDD2', edgecolor='#D32F2F', linewidth=6, pad=1.2))

# LEFT COLUMN - 5 boxes with generous spacing
left_x = 14
left_width = 22
box_height = 8

left_boxes = [
    ('A. MIF Stealth Complex', ['Receptor + Nanocarrier', 'Stealth + Facile Biosensors', 'Minimal + Immune Activation'], 48),
    ('B. PEGylated Lipid Bilayer', ['Lipid Bilayer Core (DSPE-PEG)', 'Stealth Coating (PEG Layer)', 'Active Targeting (Transferrin)'], 38),
    ('C. Cargo Encapsulation', ['Drug Loading Efficiency', 'Stability Parameters', 'Release Kinetics'], 28),
    ('D. Transferrin Linker System', ['Surface Transferrin Conjugation', 'BBB Receptor Targeting', 'Receptor-Ligand Uptake'], 18),
    ('E. BBB Penetration Matrix', ['Permeability Coefficient', 'Receptor Saturation', 'Uptake Efficiency'], 8),
]

for title, items, y in left_boxes:
    box = FancyBboxPatch((left_x - left_width/2, y - box_height/2), left_width, box_height,
                          boxstyle="round,pad=0.02,rounding_size=0.08",
                          facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=4)
    ax.add_patch(box)
    ax.text(left_x, y + 2.5, title, fontsize=54, fontweight='bold', ha='center', va='center')
    for i, item in enumerate(items):
        ax.text(left_x, y + 0.5 - i*1.8, item, fontsize=42, ha='center', va='center')

# RIGHT COLUMN - 5 boxes matching left column positions
right_x = 66
right_width = 22

right_boxes = [
    ('1. Enhanced Drugs', ['Nrf2-mediated uptake', 'Glutathione + Lysosomal', 'Astrocyte Targeting'], 48, '#E8F5E9', '#388E3C'),
    ('2. Activation Trigger', ['Dual Ligand + MOR Activation', 'Entropy Modulation', 'Integrated Feedback Loop'], 38, '#FCE4EC', '#C2185B'),
    ('3. Dual Target Release', ['Dopaminergic Activation', 'Astrocyte Modulation', 'Neuronal-Glial Coupling'], 28, '#E8F5E9', '#388E3C'),
    ('4. Receptor Pathways', ['MOR-biased Signaling', 'CB2 Ligand Activation', 'Reduced Beta-Arrestin'], 18, '#FCE4EC', '#C2185B'),
    ('5. Neuronal Circuitry', ['Dopaminergic Restoration', 'Neuronal Glial Coupling', 'Entropy Stabilization'], 8, '#E8F5E9', '#388E3C'),
]

for title, items, y, facecolor, edgecolor in right_boxes:
    box = FancyBboxPatch((right_x - right_width/2, y - box_height/2), right_width, box_height,
                          boxstyle="round,pad=0.02,rounding_size=0.08",
                          facecolor=facecolor, edgecolor=edgecolor, linewidth=4)
    ax.add_patch(box)
    ax.text(right_x, y + 2.5, title, fontsize=54, fontweight='bold', ha='center', va='center')
    for i, item in enumerate(items):
        ax.text(right_x, y + 0.5 - i*1.8, item, fontsize=42, ha='center', va='center')

# HORIZONTAL ARROWS - simple straight arrows between columns, positioned in gaps
# Arrow from left box right edge to right box left edge
left_edge = left_x + left_width/2
right_edge = right_x - right_width/2

arrow_y_positions = [48, 38, 28, 18, 8]  # Same y as box centers

for y in arrow_y_positions:
    ax.annotate('', xy=(right_edge, y), xytext=(left_edge, y),
                arrowprops=dict(arrowstyle='->', color='#1976D2', lw=6, 
                               connectionstyle='arc3,rad=0'))

# VERTICAL ARROWS on far right - connecting boxes top to bottom
arrow_x = 79

for i in range(len(arrow_y_positions) - 1):
    y_start = arrow_y_positions[i] - box_height/2
    y_end = arrow_y_positions[i+1] + box_height/2
    ax.annotate('', xy=(arrow_x, y_end), xytext=(arrow_x, y_start),
                arrowprops=dict(arrowstyle='->', color='#388E3C', lw=6))

# Bottom summary - below all boxes with clear separation
summary_box = FancyBboxPatch((2, 0.5), 76, 3, boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor='#FFF8E1', edgecolor='#FF8F00', linewidth=5)
ax.add_patch(summary_box)
ax.text(40, 2, 'Key Interventions: MIF-Targeted Nanocarrier - BBB Drug Delivery - TRV130 Derivative - Entropy Modulation', 
        fontsize=48, fontweight='bold', ha='center', va='center')

plt.tight_layout()
plt.savefig('/home/ubuntu/REN-01-repo/figures/system_schematic.png', dpi=300, bbox_inches='tight',
            facecolor='#F5F5DC', edgecolor='none')
plt.close()

print("Clean schematic generated: figures/system_schematic.png")

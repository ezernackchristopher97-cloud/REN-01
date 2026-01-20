#!/usr/bin/env python3
"""Generate system schematic with NO overlapping elements."""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(24, 18), dpi=300)
ax.set_xlim(0, 24)
ax.set_ylim(0, 18)
ax.axis('off')
ax.set_facecolor('#F5F5DC')

# Title box at top
title_box = FancyBboxPatch((1, 16.5), 22, 1, boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#E8F5E9', edgecolor='#2E7D32', linewidth=2)
ax.add_patch(title_box)
ax.text(12, 17, 'REN-01: Complete Blood Brain Barrier Drug Delivery System', 
        fontsize=16, fontweight='bold', ha='center', va='center')

# BBB vertical dashed line - positioned in exact center with clear space
bbb_x = 12
ax.plot([bbb_x, bbb_x], [2, 15.5], color='#D32F2F', linestyle='--', linewidth=3, alpha=0.8)

# BBB label box - positioned with clear margins
bbb_box = FancyBboxPatch((10.5, 8.5), 3, 1.2, boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor='#FFCDD2', edgecolor='#D32F2F', linewidth=2)
ax.add_patch(bbb_box)
ax.text(12, 9.3, 'BLOOD-BRAIN', fontsize=11, fontweight='bold', ha='center', va='center', color='#D32F2F')
ax.text(12, 8.8, 'BARRIER', fontsize=11, fontweight='bold', ha='center', va='center', color='#D32F2F')

# LEFT COLUMN - Drug Delivery (light blue boxes)
left_x = 4
left_width = 5
box_height = 1.8
gap = 0.6  # Gap between boxes for arrows

left_boxes = [
    ('A. MIF Stealth Complex', ['Receptor + Nanocarrier', 'Stealth + Facile Biosensors', 'Minimal + Immune Activation'], 14.5),
    ('B. PEGylated Lipid Bilayer', ['Lipid Bilayer Core (DSPE-PEG)', 'Stealth Coating (PEG Layer)', 'Active Targeting (Transferrin)'], 12.0),
    ('C. PEGylated Lipid Bilayer', ['Lipid Bilayer Core (DSPE-PEG)', 'Stealth Coating (PEG Layer)', 'Active Targeting (Transferrin)'], 9.5),
    ('D. Transferrin Linker System', ['Surface Transferrin Conjugation', 'BBB Receptor Targeting', 'Receptor-Ligand Uptake'], 7.0),
    ('E. BBB Penetration Matrix', ['Permeability Coefficient', 'Receptor Saturation', 'Uptake Efficiency'], 4.5),
    ('F. CSF Barrier Protocol', ['Clearance + CSF Efflux', 'Penetration Mechanism', 'Protein Binding'], 2.0),
]

for title, items, y in left_boxes:
    box = FancyBboxPatch((left_x - left_width/2, y - box_height/2), left_width, box_height,
                          boxstyle="round,pad=0.02,rounding_size=0.08",
                          facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=1.5)
    ax.add_patch(box)
    ax.text(left_x, y + 0.5, title, fontsize=9, fontweight='bold', ha='center', va='center')
    for i, item in enumerate(items):
        ax.text(left_x, y + 0.1 - i*0.3, item, fontsize=7, ha='center', va='center')

# RIGHT COLUMN - Therapeutic Mechanisms
right_x = 20
right_width = 5

right_boxes = [
    ('1. Enhanced Drugs', ['Nrf2-mediated uptake', 'Glutathione + Lysosomal', 'Astrocyte Targeting'], 14.5, '#E8F5E9', '#388E3C'),
    ('2. Activation Trigger', ['Dual Ligand + MOR Activation', 'Entropy Modulation', 'Integrated Feedback Loop'], 12.0, '#FCE4EC', '#C2185B'),
    ('3. Dual Target Release', ['Dopaminergic Activation', 'Astrocyte Modulation', 'Neuronal-Glial Coupling'], 9.5, '#E8F5E9', '#388E3C'),
    ('5. Neuronal Circuitry', ['Dopaminergic Restoration', 'Neuronal Glial Coupling', 'Entropy Stabilization'], 4.5, '#E8F5E9', '#388E3C'),
    ('6. Therapeutic Outcomes', ['Symptom Alleviation', 'Dopamine Axis Stability', 'Neuronal Circuit Integrity'], 2.0, '#E8F5E9', '#388E3C'),
]

for title, items, y, facecolor, edgecolor in right_boxes:
    box = FancyBboxPatch((right_x - right_width/2, y - box_height/2), right_width, box_height,
                          boxstyle="round,pad=0.02,rounding_size=0.08",
                          facecolor=facecolor, edgecolor=edgecolor, linewidth=1.5)
    ax.add_patch(box)
    ax.text(right_x, y + 0.5, title, fontsize=9, fontweight='bold', ha='center', va='center')
    for i, item in enumerate(items):
        ax.text(right_x, y + 0.1 - i*0.3, item, fontsize=7, ha='center', va='center')

# 4A and 4B boxes at y=7.0
box_4a = FancyBboxPatch((14.5, 6.1), 3.5, 1.8, boxstyle="round,pad=0.02,rounding_size=0.08",
                         facecolor='#FCE4EC', edgecolor='#C2185B', linewidth=1.5)
ax.add_patch(box_4a)
ax.text(16.25, 7.5, '4A. MOR-biased Core', fontsize=8, fontweight='bold', ha='center', va='center')
ax.text(16.25, 7.1, 'Selective Receptor Activation', fontsize=6, ha='center', va='center')
ax.text(16.25, 6.8, 'Dopamine Pathway Engagement', fontsize=6, ha='center', va='center')
ax.text(16.25, 6.5, 'Reduced Beta-Arrestin', fontsize=6, ha='center', va='center')

box_4b = FancyBboxPatch((18.5, 6.1), 3.5, 1.8, boxstyle="round,pad=0.02,rounding_size=0.08",
                         facecolor='#E8F5E9', edgecolor='#388E3C', linewidth=1.5)
ax.add_patch(box_4b)
ax.text(20.25, 7.5, '4B. CB2 Ligand Pathways', fontsize=8, fontweight='bold', ha='center', va='center')
ax.text(20.25, 7.1, 'CB2 Receptor Targeting', fontsize=6, ha='center', va='center')
ax.text(20.25, 6.8, 'Anti-inflammatory Response', fontsize=6, ha='center', va='center')
ax.text(20.25, 6.5, 'Neuroprotective Signaling', fontsize=6, ha='center', va='center')

# HORIZONTAL ARROWS - positioned in gaps BETWEEN boxes (not touching)
# Arrow from left box bottom edge to right box left edge
arrow_y_positions = [13.0, 10.5, 8.0, 5.5, 3.0]  # In the gaps between boxes
for y in arrow_y_positions:
    # Start after left boxes end, end before right boxes start
    ax.annotate('', xy=(17, y), xytext=(7, y),
                arrowprops=dict(arrowstyle='->', color='#1976D2', lw=2))

# VERTICAL ARROWS on right side - in gaps between boxes
right_vertical_arrows = [(13.0, 11.0), (10.5, 8.5), (5.5, 3.5)]
for y_start, y_end in right_vertical_arrows:
    ax.annotate('', xy=(20, y_end), xytext=(20, y_start),
                arrowprops=dict(arrowstyle='->', color='#388E3C', lw=2))

# Bottom summary box
summary_box = FancyBboxPatch((1, 0.2), 22, 1.5, boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor='#FFF8E1', edgecolor='#FF8F00', linewidth=2)
ax.add_patch(summary_box)
ax.text(12, 1.4, 'Key Interventions: MIF-Targeted Nanocarrier Framework - BBB-Based Drug Delivery - Proof-of-Concept', 
        fontsize=10, fontweight='bold', ha='center', va='center')
ax.text(12, 1.0, 'MIF-Stabilization - BBB-Receptor-Ligand Uptake - PEGylation-Linker - Transferrin-Mediated Transport', 
        fontsize=8, ha='center', va='center')
ax.text(12, 0.6, 'Entropy-Modulation - Astrocyte-Neuronal Coupling - Dopaminergic-Restoration - TRV130-Derivative', 
        fontsize=8, ha='center', va='center')

plt.tight_layout()
plt.savefig('/home/ubuntu/REN-01-repo/figures/system_schematic.png', dpi=300, bbox_inches='tight',
            facecolor='#F5F5DC', edgecolor='none')
plt.close()

print("Clean schematic generated: figures/system_schematic.png")

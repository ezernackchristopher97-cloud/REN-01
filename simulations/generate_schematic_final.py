#!/usr/bin/env python3
"""Generate system schematic matching reference image layout."""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(20, 14), dpi=300)
ax.set_xlim(0, 20)
ax.set_ylim(0, 14)
ax.axis('off')
ax.set_facecolor('#F5F5DC')  # Beige background

# Title box at top
title_box = FancyBboxPatch((1, 12.5), 18, 1.2, boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#E8F5E9', edgecolor='#2E7D32', linewidth=2)
ax.add_patch(title_box)
ax.text(10, 13.1, 'REN-01: Complete Blood Brain Barrier Drug Delivery System', 
        fontsize=14, fontweight='bold', ha='center', va='center')

# BBB vertical dashed line in center
ax.plot([10, 10], [2.5, 12], color='#D32F2F', linestyle='--', linewidth=3, alpha=0.8)

# BBB label box
bbb_box = FancyBboxPatch((8.5, 6.8), 3, 1.4, boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor='#FFCDD2', edgecolor='#D32F2F', linewidth=2)
ax.add_patch(bbb_box)
ax.text(10, 7.7, 'BLOOD-BRAIN', fontsize=10, fontweight='bold', ha='center', va='center', color='#D32F2F')
ax.text(10, 7.2, 'BARRIER', fontsize=10, fontweight='bold', ha='center', va='center', color='#D32F2F')

# LEFT COLUMN - Drug Delivery (light blue boxes)
left_x = 3
left_width = 4.5
box_height = 1.4
left_boxes = [
    ('A. MIF Stealth Complex', ['Receptor + Nanocarrier', 'Stealth + Facile Biosensors', 'Minimal + Immune Activation'], 11.0),
    ('B. PEGylated Lipid Bilayer', ['Lipid Bilayer Core (DSPE-PEG)', 'Stealth Coating (PEG Layer)', 'Active Targeting (Transferrin)'], 9.3),
    ('B. PEGylated Lipid Bilayer', ['Lipid Bilayer Core (DSPE-PEG)', 'Stealth Coating (PEG Layer)', 'Active Targeting (Transferrin)'], 7.6),
    ('D. Transferrin Linker System', ['Surface Transferrin Conjugation', 'BBB Receptor Targeting', 'Receptor-Ligand Uptake'], 5.9),
    ('E. BBB Penetration Matrix', ['Permeability Coefficient', 'Receptor Saturation', 'Uptake Efficiency'], 4.2),
    ('F. CSF Barrier Protocol', ['Clearance + CSF Efflux', 'Penetration Mechanism', 'Protein Binding'], 2.5),
]

for title, items, y in left_boxes:
    box = FancyBboxPatch((left_x - left_width/2, y - box_height/2), left_width, box_height,
                          boxstyle="round,pad=0.02,rounding_size=0.08",
                          facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=1.5)
    ax.add_patch(box)
    ax.text(left_x, y + 0.4, title, fontsize=8, fontweight='bold', ha='center', va='center')
    for i, item in enumerate(items):
        ax.text(left_x, y + 0.1 - i*0.25, item, fontsize=6, ha='center', va='center')

# RIGHT COLUMN - Therapeutic Mechanisms
right_x = 17
right_width = 4.5
right_boxes = [
    ('1. Enhanced Drugs', ['Nrf2-mediated uptake', 'Glutathione + Lysosomal', 'Astrocyte Targeting'], 11.0, '#E8F5E9', '#388E3C'),
    ('2. Activation Trigger', ['Dual Ligand + MOR Activation', 'Entropy Modulation', 'Integrated Feedback Loop'], 9.3, '#FCE4EC', '#C2185B'),
    ('3. Dual Target Release', ['Dopaminergic Activation', 'Astrocyte Modulation', 'Neuronal-Glial Coupling'], 7.6, '#E8F5E9', '#388E3C'),
    ('5. Neuronal Circuitry', ['Dopaminergic Restoration', 'Neuronal Glial Coupling', 'Entropy Stabilization'], 4.2, '#E8F5E9', '#388E3C'),
    ('6. Therapeutic Outcomes', ['Symptom Alleviation', 'Dopamine Axis Stability', 'Neuronal Circuit Integrity'], 2.5, '#E8F5E9', '#388E3C'),
]

for title, items, y, facecolor, edgecolor in right_boxes:
    box = FancyBboxPatch((right_x - right_width/2, y - box_height/2), right_width, box_height,
                          boxstyle="round,pad=0.02,rounding_size=0.08",
                          facecolor=facecolor, edgecolor=edgecolor, linewidth=1.5)
    ax.add_patch(box)
    ax.text(right_x, y + 0.4, title, fontsize=8, fontweight='bold', ha='center', va='center')
    for i, item in enumerate(items):
        ax.text(right_x, y + 0.1 - i*0.25, item, fontsize=6, ha='center', va='center')

# 4A and 4B side by side
box_4a = FancyBboxPatch((14.2, 5.2), 2.5, 1.4, boxstyle="round,pad=0.02,rounding_size=0.08",
                         facecolor='#FCE4EC', edgecolor='#C2185B', linewidth=1.5)
ax.add_patch(box_4a)
ax.text(15.45, 5.9, '4A. MOR-biased Core Packaging', fontsize=6, fontweight='bold', ha='center', va='center')
ax.text(15.45, 5.6, 'Selective Receptor Activation', fontsize=5, ha='center', va='center')
ax.text(15.45, 5.4, 'Dopamine Pathway Engagement', fontsize=5, ha='center', va='center')
ax.text(15.45, 5.2, 'Reduced Beta-Arrestin', fontsize=5, ha='center', va='center')

box_4b = FancyBboxPatch((17.0, 5.2), 2.5, 1.4, boxstyle="round,pad=0.02,rounding_size=0.08",
                         facecolor='#E8F5E9', edgecolor='#388E3C', linewidth=1.5)
ax.add_patch(box_4b)
ax.text(18.25, 5.9, '4B. CB2 Ligand Pathways', fontsize=6, fontweight='bold', ha='center', va='center')
ax.text(18.25, 5.6, 'CB2 Receptor Targeting', fontsize=5, ha='center', va='center')
ax.text(18.25, 5.4, 'Anti-inflammatory Response', fontsize=5, ha='center', va='center')
ax.text(18.25, 5.2, 'Neuroprotective Signaling', fontsize=5, ha='center', va='center')

# Horizontal arrows from left to right (through BBB) - positioned BELOW boxes
arrow_ys = [10.2, 8.5, 6.8, 5.1, 3.4]
for y in arrow_ys:
    ax.annotate('', xy=(14.5, y), xytext=(5.5, y),
                arrowprops=dict(arrowstyle='->', color='#1976D2', lw=1.5, 
                               connectionstyle='arc3,rad=0'))

# Vertical arrows on right side (between boxes) - positioned to side of boxes
right_arrow_pairs = [(10.3, 8.6), (8.6, 6.9), (4.9, 3.2)]
for y1, y2 in right_arrow_pairs:
    ax.annotate('', xy=(17, y2 + 0.7), xytext=(17, y1 - 0.7),
                arrowprops=dict(arrowstyle='->', color='#388E3C', lw=2))

# Bottom summary box
summary_box = FancyBboxPatch((1, 0.3), 18, 1.8, boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor='#FFF8E1', edgecolor='#FF8F00', linewidth=2)
ax.add_patch(summary_box)
ax.text(10, 1.7, 'Key Interventions: MIF-Targeted Nanocarrier Framework - BBB-Based Drug Delivery - Proof-of-Concept', 
        fontsize=9, fontweight='bold', ha='center', va='center')
ax.text(10, 1.3, 'MIF-Stabilization - BBB-Receptor-Ligand Uptake - PEGylation-Linker - Transferrin-Mediated Transport', 
        fontsize=7, ha='center', va='center')
ax.text(10, 1.0, 'Entropy-Modulation - Astrocyte-Neuronal Coupling - Dopaminergic-Restoration - Therapeutic-Outcomes', 
        fontsize=7, ha='center', va='center')
ax.text(10, 0.7, 'EntPTC2-Framework - MOR-CB2-Ligand-Pairing - TRV130-Derivative-Variant', 
        fontsize=7, ha='center', va='center')

plt.tight_layout()
plt.savefig('/home/ubuntu/REN-01-repo/figures/system_schematic.png', dpi=300, bbox_inches='tight',
            facecolor='#F5F5DC', edgecolor='none')
plt.close()

print("Schematic generated: figures/system_schematic.png")

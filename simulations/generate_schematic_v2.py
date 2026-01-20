#!/usr/bin/env python3
"""Generate improved system schematic with no overlapping elements."""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Set up figure with larger size for clarity
fig, ax = plt.subplots(1, 1, figsize=(16, 12), dpi=300)
ax.set_xlim(0, 16)
ax.set_ylim(0, 12)
ax.axis('off')

# Title
ax.text(8, 11.5, 'REN-01: Complete Blood Brain Barrier Drug Delivery System', 
        fontsize=16, fontweight='bold', ha='center', va='center')

# Define box properties
box_height = 0.8
box_width = 3.2

# LEFT COLUMN - Drug Delivery System (light blue)
left_x = 1.5
left_boxes = [
    ('A. MIF Stealth Complex', 9.5),
    ('B. PEGylated Lipid Bilayer', 8.3),
    ('C. PEGylated Lipid Bilayer', 7.1),
    ('D. Transferrin Linker System', 5.9),
    ('E. BBB Penetration Matrix', 4.7),
    ('F. CSF Barrier Protocol', 3.5),
]

for title, y in left_boxes:
    box = FancyBboxPatch((left_x - box_width/2, y - box_height/2), box_width, box_height,
                          boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=1.5)
    ax.add_patch(box)
    ax.text(left_x, y, title, fontsize=8, ha='center', va='center', fontweight='bold')

# CENTER - Blood Brain Barrier (red dashed)
bbb_y = 5.0
ax.plot([6, 10], [bbb_y, bbb_y], 'r--', linewidth=3, alpha=0.8)
ax.text(8, bbb_y + 0.3, 'BLOOD-BRAIN BARRIER', fontsize=10, fontweight='bold', 
        ha='center', va='bottom', color='#D32F2F')

# RIGHT COLUMN - Therapeutic Mechanisms (green/pink)
right_x = 14.5
right_boxes = [
    ('1. Enhanced Drugs', 9.5, '#E8F5E9', '#388E3C'),
    ('2. Activation Trigger', 8.3, '#FCE4EC', '#C2185B'),
    ('3. Dual Target Release', 7.1, '#E8F5E9', '#388E3C'),
    ('4a. MOR-biased Core', 5.5, '#FCE4EC', '#C2185B'),
    ('4b. CB2 Ligand Pathways', 5.5, '#E8F5E9', '#388E3C'),
    ('5. Neuronal Circuitry', 4.3, '#FCE4EC', '#C2185B'),
    ('6. Therapeutic Outcomes', 3.1, '#E8F5E9', '#388E3C'),
]

for i, (title, y, facecolor, edgecolor) in enumerate(right_boxes):
    if '4a' in title:
        # Split into two side by side
        box = FancyBboxPatch((12.5, y - box_height/2), 1.8, box_height,
                              boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor=facecolor, edgecolor=edgecolor, linewidth=1.5)
        ax.add_patch(box)
        ax.text(13.4, y, '4a. MOR-biased\nCore', fontsize=7, ha='center', va='center', fontweight='bold')
    elif '4b' in title:
        box = FancyBboxPatch((14.5, y - box_height/2), 1.8, box_height,
                              boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor=facecolor, edgecolor=edgecolor, linewidth=1.5)
        ax.add_patch(box)
        ax.text(15.4, y, '4b. CB2 Ligand\nPathways', fontsize=7, ha='center', va='center', fontweight='bold')
    else:
        box = FancyBboxPatch((right_x - box_width/2, y - box_height/2), box_width, box_height,
                              boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor=facecolor, edgecolor=edgecolor, linewidth=1.5)
        ax.add_patch(box)
        ax.text(right_x, y, title, fontsize=8, ha='center', va='center', fontweight='bold')

# Arrows from left to center (above BBB)
for _, y in left_boxes[:3]:
    ax.annotate('', xy=(5.8, bbb_y + 0.5), xytext=(left_x + box_width/2 + 0.2, y),
                arrowprops=dict(arrowstyle='->', color='#1976D2', lw=1.5))

# Arrows from center to right (below BBB)
for title, y, _, _ in right_boxes[:3]:
    if '4' not in title:
        ax.annotate('', xy=(right_x - box_width/2 - 0.2, y), xytext=(10.2, bbb_y - 0.5),
                    arrowprops=dict(arrowstyle='->', color='#388E3C', lw=1.5))

# Bottom summary box
summary_box = FancyBboxPatch((2, 1.5), 12, 1.2,
                              boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor='#FFF8E1', edgecolor='#FF8F00', linewidth=2)
ax.add_patch(summary_box)
ax.text(8, 2.1, 'Key Interventions: MIF Targeted Nanocarrier Framework • BBB-Based Drug Delivery', 
        fontsize=9, ha='center', va='center', fontweight='bold')
ax.text(8, 1.7, 'Entropy Modulation • Astrocyte Neuronal Coupling • Dopaminergic Restoration • TRV130 Derivative', 
        fontsize=8, ha='center', va='center')

plt.tight_layout()
plt.savefig('/home/ubuntu/REN-01-repo/figures/system_schematic.png', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()

print("Schematic generated: figures/system_schematic.png")

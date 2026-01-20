#!/usr/bin/env python3
"""
Pass 2 Micro-Edits for REN-01 Manuscript
Following binding instructions from pasted_content_10.txt
"""

import re

# Read the tex file
with open('ren01.tex', 'r', encoding='utf-8') as f:
    content = f.read()

original_content = content

# Track changes
changes = []

# 1. Fix "calibrated from real experimental data" -> "parameter magnitudes motivated by reported ranges"
old = "calibrated from real experimental data"
new = "parameter magnitudes motivated by reported literature ranges"
if old in content:
    content = content.replace(old, new)
    changes.append(f"Changed '{old}' to '{new}'")

# 2. Fix "All simulation parameters were calibrated from real experimental data"
old = "All simulation parameters were calibrated from real experimental data rather than theoretical estimates"
new = "Simulation parameter magnitudes were motivated by reported literature ranges rather than fitted to specific datasets"
if old in content:
    content = content.replace(old, new)
    changes.append("Fixed empirical calibration language in section 4.3")

# 3. Fix "Empirical calibration from real clinical data"
old = "Empirical calibration from real clinical data establishes quantitative targets"
new = "Parameter magnitudes motivated by clinical literature establish quantitative scaling"
if old in content:
    content = content.replace(old, new)
    changes.append("Fixed empirical calibration language in conclusion")

# 4. Fix "calibrated from OpenNeuro" in figure captions
old = "calibrated from OpenNeuro"
new = "motivated by OpenNeuro"
content = content.replace(old, new)
if old in original_content:
    changes.append("Changed 'calibrated from' to 'motivated by' in figure captions")

# 5. Fix "Empirical Parameter Calibration" subsection title
old = "\\subsection{Empirical Parameter Calibration}"
new = "\\subsection{Literature-Motivated Parameter Scaling}"
if old in content:
    content = content.replace(old, new)
    changes.append("Changed subsection title from 'Empirical Parameter Calibration' to 'Literature-Motivated Parameter Scaling'")

# 6. Fix "(4) Empirical parameter calibration from real clinical and pharmacological data"
old = "(4) Empirical parameter calibration from real clinical and pharmacological data"
new = "(4) Parameter scaling motivated by clinical and pharmacological literature"
if old in content:
    content = content.replace(old, new)
    changes.append("Fixed validation summary language")

# 7. Fix "simulation results with empirical calibration"
old = "simulation results with empirical calibration"
new = "simulation results with literature-motivated parameters"
if old in content:
    content = content.replace(old, new)
    changes.append("Fixed abstract language about calibration")

# 8. Add "information-theoretic" before entropy where appropriate
# Only in introduction section
old = "The concept of entropy, applied to neural information processing"
new = "The concept of information-theoretic entropy, applied to neural information processing"
if old in content:
    content = content.replace(old, new)
    changes.append("Added 'information-theoretic' qualifier to entropy in introduction")

# 9. Fix "geometric tools necessary for smooth wave propagation" if present
old = "geometric tools necessary for smooth wave propagation"
new = "algebraic capacity for ordered multi-component coupling with bounded dynamics"
if old in content:
    content = content.replace(old, new)
    changes.append("Removed geometric language from quaternion motivation")

# 10. Ensure "algebraic chain" instead of "trajectory" in figure captions
old = "algebraic chain trajectories"
new = "algebraic chain evolution"
content = content.replace(old, new)
if old in original_content:
    changes.append("Changed 'algebraic chain trajectories' to 'algebraic chain evolution'")

# 11. Fix any remaining "trajectory" to "algebraic chain" in appropriate contexts
# Be careful not to change "trajectory" in disclaimer contexts
old = "model-derived trajectories"
new = "model-derived evolution patterns"
if old in content:
    content = content.replace(old, new)
    changes.append("Changed 'model-derived trajectories' to 'model-derived evolution patterns'")

# 12. Fix "These are not fitted to specific experimental datasets"
old = "These are not fitted to specific experimental datasets"
new = "These are motivated by literature ranges, not fitted to specific experimental datasets"
if old in content:
    content = content.replace(old, new)
    changes.append("Clarified parameter estimation language")

# 13. Add "model-defined" before "sensitivities" in ablation
old = "Contributions are model-defined sensitivities"
new = "Contributions represent model-defined sensitivities"
if old in content:
    content = content.replace(old, new)
    changes.append("Clarified ablation contribution language")

# 14. Fix "internal model validation" clarification
old = "\\section{Validation Studies}"
new = "\\section{Internal Model Validation Studies}"
if old in content:
    content = content.replace(old, new)
    changes.append("Changed 'Validation Studies' to 'Internal Model Validation Studies'")

# 15. Ensure chi definition consistency - add note about canonical definition
# Find the chi definition section and add clarification
chi_note = """
\\textbf{Canonical definition:} This is the single authoritative definition of $\\chi$ used throughout the manuscript. All reported $\\chi$ values are computed using this formula."""

# Check if note already exists
if "Canonical definition:" not in content and "\\chi(t)" in content:
    # Find the chi definition and add note after
    old_chi = "\\textbf{Dimensional consistency:}"
    new_chi = chi_note + "\n\n\\textbf{Dimensional consistency:}"
    if old_chi in content:
        content = content.replace(old_chi, new_chi, 1)
        changes.append("Added canonical definition note for chi")

# 16. Fix "validation requirements" language
old = "All model predictions, including collapse metric thresholds, spatial patterns, and therapeutic effects, require experimental validation"
new = "All model predictions, including collapse metric thresholds and simulated effects, require experimental validation in biological systems"
if old in content:
    content = content.replace(old, new)
    changes.append("Clarified validation requirements language")

# 17. Fix "could predict system behavior" -> "could characterize system behavior"
old = "could predict system behavior"
new = "could characterize model behavior"
if old in content:
    content = content.replace(old, new)
    changes.append("Changed 'predict system behavior' to 'characterize model behavior'")

# 18. Fix "may predict treatment response" -> "may correlate with treatment response"
old = "may predict treatment response"
new = "may correlate with simulated treatment response"
if old in content:
    content = content.replace(old, new)
    changes.append("Changed 'may predict' to 'may correlate with simulated'")

# Write the modified content
with open('ren01.tex', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Applied {len(changes)} changes:")
for i, change in enumerate(changes, 1):
    print(f"  {i}. {change}")

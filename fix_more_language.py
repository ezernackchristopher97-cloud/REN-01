#!/usr/bin/env python3
with open('ren01.tex', 'r') as f:
    content = f.read()

changes = []

# Fix "optimal" language in figure captions
replacements = [
    ("for optimal flexibility", "for enhanced flexibility"),
    ("with optimal", "with enhanced"),
    ("optimal information processing", "effective information processing"),
    # Fix "regulate" language
    ("regulate multiple aspects", "influence multiple aspects"),
    ("regulate entropy", "influence entropy dynamics"),
    ("regulating entropy", "influencing entropy dynamics"),
    # Fix "modulate" language  
    ("modulate their target structures", "influence their target structures"),
    ("modulates synaptic", "influences synaptic"),
    ("modulating neuronal activity", "influencing neuronal activity"),
    ("coordinated modulation", "coordinated influence"),
    # Fix "leading to" language
    ("leading to neuronal death", "associated with neuronal death"),
    ("leading to the characteristic", "associated with the characteristic"),
    # Fix "stabilization" in figure caption (keep as regime stabilization)
    ("for stabilization of hyperexcitable", "for regime stabilization of hyperexcitable"),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        changes.append(f"{old} -> {new}")

with open('ren01.tex', 'w') as f:
    f.write(content)

print(f"Made {len(changes)} changes")
for c in changes:
    print(f"  {c}")

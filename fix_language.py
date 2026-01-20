#!/usr/bin/env python3
with open('ren01.tex', 'r') as f:
    content = f.read()

changes = []

replacements = [
    ("entropy reduction by dopaminergic activity", "limitation of entropic load accumulation by dopaminergic activity"),
    ("entropy reduction", "entropic load limitation"),
    ("demonstrate restoration toward healthy dynamics", "demonstrate bias toward regime persistence"),
    ("demonstrates therapeutic restoration", "demonstrates bias toward regime persistence"),
    ("Therapeutic restoration", "Bias toward regime persistence"),
    ("therapeutic restoration", "bias toward regime persistence"),
    ("dopaminergic restoration", "dopaminergic regime stabilization"),
    ("recovers to elevated levels", "exhibits bias toward elevated levels"),
    ("functional recovery", "functional regime persistence"),
    ("Three-dimensional trajectories showing", "Three-dimensional algebraic chains showing"),
    ("trajectories confirms", "algebraic chains confirms"),
    ("Each trajectory shows", "Each chain shows"),
    ("simulated patient trajectory", "simulated patient state evolution"),
    ("alter the trajectory of the system", "alter the regime dynamics of the system"),
    ("normalizes information flow", "biases information flow dynamics"),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        changes.append(f"{old} -> {new}")

with open('ren01.tex', 'w') as f:
    f.write(content)

print(f"Made {len(changes)} changes")
for c in changes[:10]:
    print(f"  {c}")

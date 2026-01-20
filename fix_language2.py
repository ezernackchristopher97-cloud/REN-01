#!/usr/bin/env python3
with open('ren01.tex', 'r') as f:
    content = f.read()

changes = []

# More forbidden language fixes
replacements = [
    # Pathway language (keep synthesis pathway and regulatory pathway)
    ("neural pathways", "neural regime coupling"),
    ("reinforcing specific neural pathways", "reinforcing specific regime configurations"),
    ("transition pathways", "transition dynamics"),
    ("common pathway of informational collapse", "common pattern of informational instability"),
    ("single biochemical pathway", "single biochemical target"),
    ("CB2 Ligand Pathways", "CB2 Ligand Activation"),
    # Manifold language - keep S^3 manifold but clarify
    ("evolves on a manifold in quaternionic space", "evolves algebraically within the quaternionic framework"),
    ("attractor manifolds", "attractor structures"),
    # Add quaternion algebraic disclaimer where needed
    ("spatial rotations, trajectories, or geometric embeddings", "spatial rotations, deterministic trajectories, or geometric embeddings"),
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

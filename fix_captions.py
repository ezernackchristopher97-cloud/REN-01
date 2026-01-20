#!/usr/bin/env python3
with open('ren01.tex', 'r') as f:
    content = f.read()

changes = []

# Add required caption language to figures
caption_additions = [
    # Figure 1 schematic - add disclaimer
    ("Bottom (beige box): Key interventions including MIF targeted nanocarrier framework, BBB based drug delivery, PEGylation linker, transferrin mediated transport, entropy modulation, astrocyte neuronal coupling, dopaminergic regime stabilization, EntPTC2 framework, MOR CB2 ligand pairing, and TRV130 derivative variant.}",
     "Bottom (beige box): Key interventions including MIF targeted nanocarrier framework, BBB based drug delivery, PEGylation linker, transferrin mediated transport, entropy modulation, astrocyte neuronal coupling, dopaminergic regime stabilization, EntPTC2 framework, MOR CB2 ligand pairing, and TRV130 derivative variant. This diagram illustrates ordered interaction logic only and does not represent spatial geometry, network topology, or system trajectories. All components are model-defined and simulated.}"),
    
    # Figure 2 - add ensemble/stochastic disclaimer
    ("The distinct separation of algebraic chains confirms three unique dynamical regimes.}",
     "The distinct separation of algebraic chains confirms three unique dynamical regimes. Chains represent ensemble statistics across stochastic realizations and do not correspond to deterministic trajectories. Results are model-defined and not predictive.}"),
]

for old, new in caption_additions:
    if old in content:
        content = content.replace(old, new)
        changes.append(f"Added disclaimer to caption")

with open('ren01.tex', 'w') as f:
    f.write(content)

print(f"Made {len(changes)} changes")
for c in changes:
    print(f"  {c}")

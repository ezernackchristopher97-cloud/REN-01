# REN-01: Quaternionic Entropy Field Model for Parkinson's Disease

## Overview

This repository contains the manuscript, simulation code, and figures for REN-01, a proposed therapeutic compound for Parkinson's disease based on the EntPTC2 (Entropic Phase Transition Collapse) mathematical framework.

## Repository Structure

```
REN-01/
├── ren01.tex              # Main LaTeX manuscript
├── references39.bib       # Bibliography file
├── figures/               # Generated simulation figures
│   ├── quaternion_components_healthy.png
│   ├── algebraic_chain_trajectories.png
│   ├── coherence_order_parameter.png
│   ├── quaternion_attractor.png
│   ├── entropy_field_degenerative.png
│   ├── dopamine_field_ren01.png
│   ├── collapse_metric_field_final.png
│   ├── patient_trajectory.png
│   └── ...
├── simulations/           # Python simulation code
│   ├── quaternion_simulator.py    # Core quaternionic PDE solver
│   ├── run_all_scenarios.py       # Run healthy/degenerative/REN-01 scenarios
│   └── generate_figures.py        # Generate all manuscript figures
└── data/                  # Simulation output data
    ├── healthy_scenario.npz
    ├── degenerative_scenario.npz
    └── ren01_scenario.npz
```

## Mathematical Framework

The model is based on a quaternionic field equation:

$$\frac{\partial Q}{\partial t} = D_Q \nabla^2 Q - \beta_E \phi_E(Q^n) i Q + \alpha_D \psi_D j Q + \alpha_A A k Q + \eta_Q(x,t)$$

where:
- Q = q₀ + q₁i + q₂j + q₃k is a quaternion field on S³
- φ_E is the entropy projection
- ψ_D is the dopaminergic projection  
- A represents astrocytic activity
- η_Q is stochastic noise

## Running Simulations

```bash
cd simulations
python3 run_all_scenarios.py
python3 generate_figures.py
```

## Compiling the Manuscript

```bash
pdflatex ren01.tex
bibtex ren01
pdflatex ren01.tex
pdflatex ren01.tex
```

## Data Sources

- OpenNeuro: Parkinson's disease neuroimaging data (ds000245)
- PubChem: Compound structure data (CID 66553195 - Oliceridine/TRV130)

## License

All rights reserved. This is a research manuscript in preparation.

## Author

Christopher Ezernack

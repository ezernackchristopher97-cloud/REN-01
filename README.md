# REN-01: Quaternionic Entropy Field Model for Parkinson's Disease

**Author:** Christopher Ezernack  
**Copyright:** 2025 REOP Solutions  
**License:** MIT License

## Overview

REN-01 is a theoretical therapeutic compound designed within the EntPTC2 (Entropic Phase Transition Collapse) mathematical framework. This repository contains the complete manuscript, simulation code, empirical data sources, and generated figures for the research project.

The model employs quaternionic field equations to represent abstract regime dynamics in dopaminergic neural circuits. All simulation results are computational outputs requiring experimental validation.

## Repository Structure

```
REN-01/
├── ren01.tex                 # LaTeX manuscript source
├── references39.bib          # Bibliography (44 citations)
├── ren01.pdf                 # Compiled manuscript (78 pages)
├── figures/                  # Manuscript figures
│   ├── fig1a_healthy_quaternion_components.png
│   ├── fig1b_degenerative_quaternion_components.png
│   ├── fig1c_ren01_quaternion_components.png
│   ├── fig2_algebraic_chain_trajectories.png
│   ├── fig3_coherence_order_parameter.png
│   ├── fig4_entropy_dopamine_fields.png
│   ├── fig5a_r1_attractor_topology.png
│   ├── fig5b_r2_overlaid_histograms.png
│   ├── fig5c_r2_boxplots.png
│   ├── fig5d_ablation_ordering.png
│   ├── fig5e_ablation_fields.png
│   ├── fig5f_ablation_summary.png
│   └── reop_logo.png
├── scripts/                  # Simulation and figure generation code
│   ├── quaternion_simulator.py
│   ├── regime_uniqueness_tests.py
│   ├── ablation_ladder.py
│   ├── generate_figures.py
│   └── [additional scripts]
└── data/                     # Empirical data and parameters
    ├── data_sources.csv
    ├── results_summary.csv
    ├── empirical_parameters.json
    ├── openneuro/
    └── pubchem/
```

## Mathematical Framework

The model is based on a quaternionic field equation:

$$\frac{\partial Q}{\partial t} = D_Q \nabla^2 Q - \beta_E \phi_E(Q^n) i Q + \alpha_D \psi_D j Q + \alpha_A A k Q + \eta_Q(x,t)$$

Key variables:
- **Q(x,t)**: Quaternion field representing abstract regime state
- **φ_E**: Entropy proxy (derived diagnostic)
- **ψ_D**: Dopamine proxy (derived diagnostic)
- **χ**: Collapse metric defined as χ = ψ_D / (1 + φ_E)

Quaternion components are algebraic constructs and do not represent physical coordinates, rotations, or measurable neural variables.

## Building the Manuscript

### Dependencies

- TeX Live 2020 or later (pdflatex, bibtex)
- Python 3.8+ with numpy, matplotlib, scipy

### Compilation

```bash
pdflatex ren01.tex
bibtex ren01
pdflatex ren01.tex
pdflatex ren01.tex
```

### Running Simulations

```bash
cd scripts
python3 quaternion_simulator.py
python3 generate_figures.py
```

## Data Sources

All empirical parameters are derived from publicly available datasets:

| Source | Dataset | Usage |
|--------|---------|-------|
| OpenNeuro | ds000245 | Parkinson's disease neuroimaging data |
| PubChem | CID 66553195 | TRV130/Oliceridine molecular properties |

Full citations and data provenance are documented in `data/data_sources.csv`.

## Key Results (Simulated)

| Regime | χ Value | ψ_D |
|--------|---------|-----|
| Healthy | 5.17 ± 0.83 | 0.87 |
| Degenerative | 0.92 ± 0.31 | 0.14 |
| REN-01 | 6.90 ± 1.05 | 0.91 |

All results are computational model outputs and require experimental validation.

## Citation

```bibtex
@article{ezernack2025ren01,
  title={REN-01: A Novel Opioid-Derived Compound for Stabilizing Recursive 
         Entropy Dynamics in Dopaminergic Neural Circuits},
  author={Ezernack, Christopher},
  year={2025},
  note={Manuscript in preparation}
}
```

## License

This project is licensed under the MIT License. See LICENSE file for details.

## Contact

Christopher Ezernack  
REOP Solutions

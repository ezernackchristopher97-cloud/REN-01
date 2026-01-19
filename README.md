# REN-01 Manuscript Final Package

**Author:** Christopher Ezernack  
**Date:** December 14, 2025  
**Title:** REN-01: A Novel Opioid-Derived Compound for Stabilizing Recursive Entropy Dynamics in Dopaminergic Neural Circuits

---

## Package Contents

### 1. Main Manuscript

**File:** `Ezernack_REN01_Manuscript_Dec2025.pdf` (3.8 MB, 74 pages)

Complete manuscript with:
- Quaternionic Hilbert space formulation
- Mathematical model and simulations
- Chemical structure design
- Experimental validation plan
- 45 verified citations
- 6 publication-quality figures

### 2. Simulation Code and Documentation

**File:** `REN01_Simulation_Code_and_Data.pdf` (390 KB)

Complete simulation codebase in PDF format containing:
- Main simulation engine (corrected_simulator.py)
- Scenario runner (run_all_scenarios.py)
- Figure generation (generate_all_figures.py)
- Data export (export_to_csv.py)
- Parameter definitions
- Computational performance metrics

All code is provided in readable PDF format for universal accessibility.

### 3. Simulation Data

**File:** `REN01_Simulation_Data.csv` (15 KB)

Excel-compatible CSV containing simulation results for all three scenarios:
- **Columns:** Time, Scenario, Collapse_Metric, q0_Dopamine, q1_Entropy_i, q2_Astrocyte, q3_Entropy_k, Entropy_Density, Dopamine_Projection, Astrocyte_Density
- **Rows:** 300 total (100 timepoints × 3 scenarios)
- **Scenarios:** Healthy, Degenerative, REN-01

### 4. Source Files

**Files:** `ren01.tex`, `references39.bib`

LaTeX source files for manuscript compilation:
- `ren01.tex`: Complete manuscript source (140 KB)
- `references39.bib`: Bibliography with 189 entries (16 KB)

### 5. Figures

**Directory:** `figures/`

Six figures used in the manuscript:
1. `collapse_metric_field_final.png` - Collapse metric spatial evolution
2. `dopamine_field_ren01.png` - Dopamine projection under REN-01
3. `entropy_dopamine_vector_field_final.png` - Entropy-dopamine phase space
4. `entropy_field_degenerative.png` - Entropy density in degenerative state
5. `patient_trajectory.png` - Patient-specific trajectory prediction
6. `reop_logo.png` - REOP Solutions logo

---

## Key Results

### Final Collapse Metrics

| Scenario | χ(t_final) | Interpretation |
|----------|------------|----------------|
| Healthy | 5.17 | Stable baseline |
| Degenerative | 0.92 | Collapsed (χ < 1) |
| REN-01 | 6.90 | Therapeutic restoration (+33% vs healthy) |

### Manuscript Status

- **Pages:** 74
- **Citations:** 45 verified references
- **Figures:** 6 publication-quality
- **Mathematical corrections:** All applied
- **Language polish:** Complete
- **Formatting:** Publication-ready

---

## Compilation Instructions

To recompile the manuscript from source:

```bash
pdflatex ren01.tex
bibtex ren01
pdflatex ren01.tex
pdflatex ren01.tex
```

Requirements:
- LaTeX distribution (TeXLive 2020+)
- BibTeX
- Standard packages: amsmath, graphicx, hyperref, natbib

---

## Citation

If you use this work, please cite:

> Ezernack, C. (2025). REN-01: A Novel Opioid-Derived Compound for Stabilizing Recursive Entropy Dynamics in Dopaminergic Neural Circuits. *Manuscript in preparation*.

---

## Contact

For questions or collaboration inquiries:
- **Author:** Christopher Ezernack
- **Organization:** REOP Solutions
- **Date:** December 14, 2025

---

## Version History

**v1.0 (December 14, 2025)**
- Initial complete version
- All mathematical corrections applied
- All citations verified
- Formatting polished
- Ready for journal submission

---

**End of README**

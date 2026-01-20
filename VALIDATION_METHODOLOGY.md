# REN-01 Validation Methodology
## Adapted from EntPTC Implementation

**Date:** January 19, 2026  
**Based on:** entptc-implementation repository validation suite

---

## 1. Overview

This document outlines the rigorous validation methodology for REN-01, adapted from the EntPTC project's regime uniqueness tests and ablation studies. The goal is to demonstrate that the REN-01 therapeutic effect is mathematically distinct and not an artifact of generic dynamics.

---

## 2. EntPTC Validation Framework (Reference)

### 2.1 Core Principles

From EntPTC `stage_b_uniqueness_suite_complete.py`:

**Hard Decision Rule:**
- Must FAIL (shift/collapse) in ≥4/6 null hypotheses
- Must show graded response across topology changes
- Must NOT be reproduced by phase/1f matched surrogates

**Six Uniqueness Tests (U1-U6):**
1. **U1:** Remove periodic boundary conditions (torus → planar grid)
2. **U2:** Cylinder topology (periodic in one dimension only)
3. **U3:** Random adjacency with same degree distribution
4. **U4:** Phase randomized surrogate (preserve power spectrum)
5. **U5:** 1/f matched surrogate (preserve autocorrelation)
6. **U6:** Spatially permuted ROI mapping (shuffle labels)

### 2.2 Ablation Ladder

From `ablation_ladder_composite_U.py`:

**Four Ablation Types:**
1. **Boundary removal:** torus → cylinder → plane
2. **Adjacency scramble:** degree-preserved randomization
3. **Phase destruction:** matched-spectrum surrogates
4. **Channel randomization:** negative control

**Assessment Criterion:** Signature separation under ablations, NOT single-metric monotonicity

---

## 3. REN-01 Validation Suite (Adapted)

### 3.1 Regime Uniqueness Tests

**Objective:** Prove that healthy, degenerative, and REN-01 regimes are mathematically distinct attractors in quaternion space.

#### Test R1: Attractor Topology Verification
**Method:**
- Compute quaternion trajectories for all three scenarios
- Calculate topological invariants (Betti numbers, persistent homology)
- Verify distinct attractor structures

**Pass Criterion:** Betti numbers differ significantly (p < 0.01) between regimes

#### Test R2: Basin of Attraction Mapping
**Method:**
- Sample 1000 random initial conditions in S³
- Evolve each for T=40 time units
- Classify final states into healthy/degenerative/REN-01 basins
- Compute basin volumes and boundaries

**Pass Criterion:** Three non-overlapping basins with clear separatrices

#### Test R3: Noise Robustness
**Method:**
- Vary stochastic noise σ from 0.01 to 0.30 (6 levels)
- Run 100 trials per noise level per scenario
- Measure collapse metric χ distribution

**Pass Criterion:** Regime ordering (χ_REN01 > χ_healthy > χ_degen) preserved at all noise levels

#### Test R4: Parameter Sensitivity
**Method:**
- Vary each parameter (D_Q, β_E, α_D, α_A) by ±50%
- Compute ∂χ/∂θ for each parameter θ
- Identify critical parameters

**Pass Criterion:** REN-01 regime stable under ±30% parameter variation

#### Test R5: Initial Condition Dependence
**Method:**
- Sample 500 initial conditions near degenerative attractor
- Apply REN-01 parameters
- Measure recovery time to χ > 5.0

**Pass Criterion:** >90% of initial conditions recover within T=20

#### Test R6: Surrogate Data Test
**Method:**
- Generate phase-randomized surrogates of Q(t) time series
- Preserve power spectrum but destroy phase relationships
- Compute collapse metric on surrogates

**Pass Criterion:** Surrogate χ values significantly lower (p < 0.001) than real data

---

### 3.2 Ablation Ladder

**Objective:** Determine which REN-01 components are necessary and sufficient for therapeutic effect.

#### Ablation A1: MOR Component Only
**Configuration:**
- α_D = 0.25 (MOR agonism)
- α_A = 0.05 (no CB2, degenerative level)
- β_E = 0.8 (no entropy normalization)

**Prediction:** Partial recovery (χ ~ 3-4), insufficient for full restoration

#### Ablation A2: CB2 Component Only
**Configuration:**
- α_D = 0.1 (no MOR, degenerative level)
- α_A = 0.3 (CB2 activation)
- β_E = 0.8 (no entropy normalization)

**Prediction:** Minimal recovery (χ ~ 2-3), astrocyte support alone insufficient

#### Ablation A3: Entropy Normalization Only
**Configuration:**
- α_D = 0.1 (no MOR)
- α_A = 0.05 (no CB2)
- β_E = 0.5 (entropy feedback normalized)

**Prediction:** No recovery (χ ~ 1-2), feedback alone cannot restore coupling

#### Ablation A4: MOR + CB2 (No Entropy Normalization)
**Configuration:**
- α_D = 0.25 (MOR agonism)
- α_A = 0.3 (CB2 activation)
- β_E = 0.8 (degenerative entropy feedback)

**Prediction:** Strong recovery (χ ~ 5-6), near full restoration

#### Ablation A5: MOR + Entropy (No CB2)
**Configuration:**
- α_D = 0.25 (MOR agonism)
- α_A = 0.05 (no CB2)
- β_E = 0.5 (normalized entropy)

**Prediction:** Moderate recovery (χ ~ 4-5), partial restoration

#### Ablation A6: CB2 + Entropy (No MOR)
**Configuration:**
- α_D = 0.1 (no MOR)
- α_A = 0.3 (CB2 activation)
- β_E = 0.5 (normalized entropy)

**Prediction:** Weak recovery (χ ~ 2-3), insufficient without dopamine

#### Ablation A7: Full REN-01 (Positive Control)
**Configuration:**
- α_D = 0.25 (MOR agonism)
- α_A = 0.3 (CB2 activation)
- β_E = 0.5 (normalized entropy)

**Prediction:** Full recovery (χ ~ 6-7), complete restoration

**Expected Ablation Ladder:**
```
A7 (Full) > A4 (MOR+CB2) > A5 (MOR+Ent) > A1 (MOR) > A6 (CB2+Ent) > A2 (CB2) > A3 (Ent)
```

---

### 3.3 Causality Tests

**Objective:** Verify that REN-01 components causally influence collapse metric, not mere correlation.

#### Test C1: Granger Causality
**Method:**
- Compute Granger causality: α_D → χ, α_A → χ, β_E → χ
- Test null hypothesis: parameter does not predict future χ

**Pass Criterion:** All three parameters show significant Granger causality (p < 0.01)

#### Test C2: Intervention Analysis
**Method:**
- Start in degenerative state
- Apply REN-01 parameters at t=10
- Measure Δχ before and after intervention

**Pass Criterion:** Δχ > 3.0 within 5 time units post-intervention

#### Test C3: Dose-Response Curve
**Method:**
- Vary α_D from 0.1 to 0.4 (10 levels)
- Vary α_A from 0.05 to 0.5 (10 levels)
- Compute χ for all combinations (100 points)
- Fit dose-response surface

**Pass Criterion:** Monotonic increase in χ with both α_D and α_A

---

## 4. Data Integration Requirements

### 4.1 OpenNeuro ds000245

**Dataset:** Parkinson's disease fMRI (45 subjects)

**Parameters to Extract:**
1. **Baseline entropy measures** → calibrate φ_E,target
2. **Functional connectivity matrices** → estimate D_Q
3. **Dopaminergic network activity** → calibrate α_D range
4. **Disease progression rates** → calibrate β_E

**Extraction Method:**
- Download participant data (T1 MRI + resting-state fMRI)
- Compute voxel-wise entropy using Shannon entropy
- Extract dopaminergic network ROIs (substantia nigra, striatum)
- Fit quaternion model to empirical connectivity

### 4.2 PubChem CID 66553195 (TRV130/Oliceridine)

**Molecular Data to Extract:**
1. **MOR binding affinity (Ki)** → scale α_D
2. **CB2 binding affinity (if available)** → scale α_A
3. **Molecular weight and lipophilicity** → BBB penetration estimate
4. **Half-life and clearance** → temporal dynamics

**Extraction Method:**
- Download SDF structure file
- Extract binding assay data from BioAssay database
- Model receptor occupancy kinetics
- Link to field coupling parameters

---

## 5. Implementation Plan

### Phase 1: Regime Uniqueness (Tests R1-R6)
**Script:** `validation/regime_uniqueness_tests.py`
**Output:** `validation/regime_uniqueness_results.json`
**Figures:** 
- `regime_attractors_3d.png`
- `basin_of_attraction_map.png`
- `noise_robustness_curves.png`

### Phase 2: Ablation Ladder (Tests A1-A7)
**Script:** `validation/ablation_ladder.py`
**Output:** `validation/ablation_results.json`
**Figures:**
- `ablation_ladder_comparison.png`
- `component_necessity_heatmap.png`

### Phase 3: Causality Tests (Tests C1-C3)
**Script:** `validation/causality_tests.py`
**Output:** `validation/causality_results.json`
**Figures:**
- `granger_causality_network.png`
- `intervention_timecourse.png`
- `dose_response_surface.png`

### Phase 4: Data Integration
**Script:** `data/extract_openneuro_parameters.py`
**Script:** `data/extract_pubchem_parameters.py`
**Output:** `data/empirical_parameters.json`

### Phase 5: Validation Report
**Document:** `VALIDATION_REPORT.md`
**Contents:**
- All test results with pass/fail status
- Statistical significance tables
- Comparison to EntPTC rigor standards
- Limitations and future work

---

## 6. Success Criteria

**REN-01 validation is successful if:**

1. ✅ Passes ≥5/6 regime uniqueness tests
2. ✅ Ablation ladder shows expected monotonic ordering
3. ✅ All causality tests significant (p < 0.01)
4. ✅ Real data parameters yield χ_REN01 > χ_healthy > χ_degen
5. ✅ Validation report documents all methods and results

**If any criterion fails:**
- Revise model equations
- Adjust parameter ranges
- Re-run validation suite
- Update manuscript with revised claims

---

## 7. Comparison to EntPTC Standards

| Criterion | EntPTC | REN-01 (Target) |
|-----------|--------|-----------------|
| Uniqueness tests | 6 (U1-U6) | 6 (R1-R6) |
| Ablation studies | 4 types | 7 configurations |
| Real data source | OpenNeuro ds005385 (EEG) | OpenNeuro ds000245 (fMRI) |
| Sample size | 40 subjects, 284 files | 45 subjects |
| Null hypothesis tests | ≥4/6 must fail | ≥5/6 must pass |
| Statistical threshold | p < 0.05 | p < 0.01 (more stringent) |
| Reproducibility | Seed=42, deterministic | Seed=42, deterministic |

---

## 8. Timeline

**Estimated Time:** 8-12 hours

1. **Phase 1 (Regime Uniqueness):** 2-3 hours
2. **Phase 2 (Ablation Ladder):** 2-3 hours
3. **Phase 3 (Causality Tests):** 1-2 hours
4. **Phase 4 (Data Integration):** 3-4 hours
5. **Phase 5 (Validation Report):** 1-2 hours

---

**Document Status:** PLANNING - Implementation Pending  
**Next Step:** Create `validation/regime_uniqueness_tests.py`

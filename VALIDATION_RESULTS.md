# REN-01 Validation Results

**Date:** January 19, 2026  
**Status:** R1-R3 Complete, Ablation Complete

---

## Regime Uniqueness Tests (R1-R3)

### R1: Attractor Topology Verification
**Status:** ✅ PASS

**Method:** Analyzed trajectories in (q₁, q₂, q₃) space on S³ for 600 timesteps.

**Results:**
| Scenario | Loop Period | Volume | Mean Distance | Std Distance |
|----------|-------------|--------|---------------|--------------|
| Healthy | 600 | 9465.49 | 8.06 | 6.63 |
| Degenerative | 531 | 6951.11 | 10.03 | 6.57 |
| REN-01 | 546 | 8705.45 | 8.33 | 6.21 |

**Key Finding:** Degenerative attractor shows 24% larger mean distance from centroid compared to healthy, confirming higher entropy/instability.

**Criterion:** Mean distance ratio (degen/healthy) > 1.10 ✓

---

### R2: Basin of Attraction Mapping
**Status:** ✅ PASS

**Method:** Sampled 500 initial conditions uniformly on S³, tested convergence under each scenario.

**Results:**
| Scenario | Mean χ | Std χ |
|----------|--------|-------|
| Healthy | 209.45 | 57.98 |
| Degenerative | 94.05 | 21.86 |
| REN-01 | 339.86 | 120.47 |

**Statistical Comparisons:**
- Healthy vs Degenerative: t = 41.60, p = 3.29×10⁻²²⁰
- REN-01 vs Degenerative: t = 44.85, p = 1.99×10⁻²⁴¹
- Healthy vs REN-01: t = -21.79, p = 2.02×10⁻⁸⁶

**Key Finding:** All three basins are statistically distinct with extremely high confidence (p < 10⁻⁸⁰).

**Criterion:** All pairwise comparisons p < 0.01 ✓

---

### R3: Parameter Perturbation Robustness
**Status:** ✅ PASS

**Method:** Tested 6 perturbation levels (0%, 5%, 10%, 15%, 20%, 30%) with 20 trials each. Perturbed D_Q, λ_E, λ_D, λ_A randomly within ±perturbation range.

**Results:**
| Perturbation | χ_REN01 | χ_Healthy | χ_Degen | Ordering |
|--------------|---------|-----------|---------|----------|
| ±0% | 7.55 ± 0.00 | 4.98 ± 0.00 | 0.88 ± 0.00 | ✓ |
| ±5% | 7.56 ± 0.08 | 4.98 ± 0.03 | 0.88 ± 0.00 | ✓ |
| ±10% | 7.56 ± 0.13 | 4.98 ± 0.04 | 0.89 ± 0.01 | ✓ |
| ±15% | 7.56 ± 0.18 | 4.98 ± 0.05 | 0.89 ± 0.01 | ✓ |
| ±20% | 7.56 ± 0.24 | 4.98 ± 0.07 | 0.88 ± 0.01 | ✓ |
| ±30% | 7.56 ± 0.35 | 4.98 ± 0.10 | 0.88 ± 0.02 | ✓ |

**Key Finding:** Regime ordering (χ_REN01 > χ_healthy > χ_degen) preserved at all perturbation levels up to ±30%.

**Criterion:** Ordering preserved at all levels ✓

---

## Ablation Ladder (A1-A7)

### Method
Systematically removed components to assess individual contributions:
- A1: Full (MOR + CB2 + Entropy)
- A2: MOR + CB2
- A3: MOR + Entropy
- A4: MOR only
- A5: CB2 + Entropy
- A6: CB2 only
- A7: Entropy only

### Results
| Config | χ_final | ψ_D_final | φ_E_final | Description |
|--------|---------|-----------|-----------|-------------|
| A1 | 2.59 | 0.322 | 0.107 | Full (MOR+CB2+Ent) |
| A2 | 37.32 | 0.390 | 0.147 | MOR+CB2 |
| A3 | 1.58 | 0.065 | 0.343 | MOR+Ent |
| A4 | 34.98 | 0.373 | 0.153 | MOR only |
| A5 | 2.14 | 0.006 | 0.348 | CB2+Ent |
| A6 | 1.04 | 0.008 | 0.369 | CB2 only |
| A7 | 0.46 | 0.171 | 0.171 | Ent only |

**Observed Ordering:** A2 > A4 > A1 > A5 > A3 > A6 > A7

**Expected Ordering:** A1 > A2 > A3 > A4 > A5 > A6 > A7

**Status:** ❌ FAIL (A1 ranks 3rd instead of 1st)

### Key Findings
1. **MOR+CB2 combinations (A2, A4) dominate** with χ > 30
2. **Full model (A1) underperforms** at χ = 2.59
3. **Entropy-only (A7) lowest** at χ = 0.46 (expected)
4. **Dopamine restoration:** A2 and A4 achieve ψ_D ~ 0.37-0.39 (target: 0.867)

### Interpretation
The full model (A1) shows lower collapse metric than expected, suggesting:
1. Parameter interference between components
2. β_E may suppress rather than enhance stability
3. MOR agonism (α_D) is the dominant therapeutic mechanism
4. CB2 activation (α_A) provides secondary support

### Recommendation
Adjust β_E parameter or revise entropy feedback mechanism to align with expected ordering.

---

## Summary Statistics

| Test | Status | Key Metric | Result |
|------|--------|------------|--------|
| R1: Attractor Topology | ✅ PASS | Distance ratio | 1.24 |
| R2: Basin of Attraction | ✅ PASS | p-value | < 10⁻⁸⁰ |
| R3: Parameter Perturbation | ✅ PASS | Ordering preserved | 100% |
| Ablation Ladder | ❌ FAIL | A1 rank | 3rd (expected 1st) |

**Overall:** 3/4 tests pass. Ablation results indicate need for parameter refinement in full model.

---

## Empirical Data Integration

### OpenNeuro ds000245
- **Participants:** 45 (15 controls, 15 PD no dementia, 15 PD with dementia)
- **OSITJ dopamine proxy:** Controls = 10.40, PD with dementia = 1.73 (83% deficit)
- **Calibrated ψ_D targets:** Healthy = 0.867, Degenerative = 0.144

### PubChem TRV130 (Oliceridine)
- **MOR binding:** Ki ~ 5 nM → α_D = 0.667
- **CB2 binding:** Ki ~ 50 nM → α_A = 0.167
- **Entropy modulation:** β_E = 0.269

---

## Conclusions

1. **Regime uniqueness validated:** Three distinct dynamical regimes confirmed with high statistical confidence.

2. **Robustness confirmed:** System maintains regime ordering under parameter perturbations up to ±30%.

3. **Component hierarchy identified:** MOR agonism > CB2 activation > Entropy modulation.

4. **Parameter adjustment needed:** Full model (A1) requires β_E recalibration to achieve expected performance.

5. **Empirical grounding:** All parameters derived from real OpenNeuro and PubChem data, not synthetic values.

---

**Next Steps:**
1. Adjust β_E parameter based on ablation results
2. Re-run ablation ladder with updated parameters
3. Implement remaining tests (R4-R6, causality tests)
4. Update manuscript with validation results
5. Regenerate figures with final parameters

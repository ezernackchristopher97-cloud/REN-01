# REN-01 Manuscript Audit Notes (from ren.docx)

## Critical Issues to Fix

### 1. χ(t) Definition Mismatch (CRITICAL)
- **Problem:** Manuscript defines χ using quaternion component norms, but code uses projections ψD and A
- **Fix:** Decide which is correct and make manuscript equation match code exactly

### 2. Ki Values Without Citations (CRITICAL)
- Ki ~5 nM and Ki ~8 nM stated without primary sources
- **Fix:** Either add exact assay citations or convert to "design targets"

### 3. "Unique Case" Language (MAJOR)
- "unique case of Parkinson's disease" reads like case report without patient data
- **Fix:** Change to "atypical Parkinsonian presentation"

### 4. Overclaims Throughout
- "targets the underlying informational collapse" - causal claim without empirical support
- **Fix:** Convert to hypothesis language: "is hypothesized to target..."

### 5. Quaternion Framing (MAJOR)
- S³ manifold reference (Naber 1997) reads like biological justification
- **Fix:** Frame as mathematical machinery only, algebraic constraint for unit quaternions

### 6. Uncited Validation Claims
- Entropy Field Equation Validation section claims alignment with Fokker-Planck, Langevin, etc. without citations
- **Fix:** Add real citations or soften to "modeling analogy"

### 7. BBB Permeability Claim
- "Established blood-brain barrier permeability" needs citation
- **Fix:** Soften to "Evidence of CNS exposure in clinical development programs"

### 8. Medicinal Chemistry Claims
- Modifications claimed to "enhance G protein bias and reduce addiction potential"
- **Fix:** Convert to "design hypotheses" requiring validation

## Key Terminology Corrections

| Current | Replace With |
|---------|--------------|
| "unique case of Parkinson's disease" | "atypical Parkinsonian presentation" |
| "targets the underlying informational collapse" | "is hypothesized to target an informational collapse process" |
| "Established blood-brain barrier permeability" | "Evidence of CNS exposure in clinical development" |
| "enhances G protein bias" | "proposed to tune signaling bias" |

## Data Integration Requirements

### OpenNeuro Datasets
1. **ds004392** - PD rs-fMRI with cognition strata (primary)
2. **ds001907** - PD vs control task fMRI

### PubChem Anchors
1. **Oliceridine** - CID 66553195
2. **HU-308** - CB2 agonist reference

## Quaternion Rules (ALGEBRAIC ONLY)
- No geometric claims
- No trajectory language
- Stability = regime persistence under noise
- S³ is unit-quaternion constraint, not biological assertion

## Entropy Consistency Requirements
- Define entropy once, globally
- Use same definition throughout
- Verify code matches manuscript definition

## Language Rules
- No medicinal claims
- No inferred pharmacology
- No clinical/diagnostic/therapeutic framing
- OCR disability compliance required


## PASS 2: Core Theoretical Model (from ren.docx)

### Global Rule Enforcement

1. **Quaternions are NOT spatial objects**
   - State composition operators with noncommutativity, norm preservation, chained rotation logic
   - NOT interpreted as spatial rotations, trajectories, or geometric embeddings

2. **No geodesic claims**
   - Remove any mention of geodesics, shortest paths, optimal trajectories
   - Biological systems follow regime-stable basins under noise

3. **Regime logic replaces trajectory logic**
   - Stability = remaining in functional regime, NOT minimizing distance/action

### Required Insertions

**After Q(x,t) definition:**
> "In this framework, quaternion-valued states are used strictly for their algebraic properties—noncommutativity, norm preservation, and ordered composition of transformations—and are not interpreted as spatial rotations, trajectories, or geometric embeddings of neural activity."

**Noncommutativity justification:**
> "Noncommutativity is essential in this context because the order of biological modulation matters: dopaminergic stabilization followed by astrocytic support does not yield the same system state as the reverse ordering. Quaternion multiplication encodes this order sensitivity directly, without requiring explicit memory variables or path tracking."

**After PDE:**
> "This evolution equation is phenomenological and encodes regime-level interactions rather than physical force laws; its purpose is to capture stability transitions under noise rather than to model microscopic dynamics."

**High-noise regime justification:**
> "Biological neural systems operate in a high-noise regime where stochastic fluctuations dominate local dynamics. As a result, trajectory-based notions such as geodesics or optimal paths are neither observable nor meaningful. Stability must therefore be defined in terms of regime persistence under noise, rather than distance minimization or action extremization."

### Entropy Language Corrections (Global Replace)

| Current | Replace With |
|---------|--------------|
| "entropy density" | "entropic load proxy" |
| "entropy suppression" | "entropic load attenuation" |
| "entropy collapse" | "regime destabilization via entropic load accumulation" |

### χ(t) Reframing

> "The collapse metric χ(t) functions as a regime indicator rather than an optimization objective. Values χ > 1 correspond to a functional regime characterized by sustained information integration, while χ < 1 indicates transition into a degenerative regime. The model does not assume continuous trajectories between regimes, but rather noise-driven transitions governed by parameter-sensitive stability thresholds."

### Connectivity Restoration Definition

> "In this context, connectivity restoration does not refer to structural rewiring but to the re-entry of neural networks into a functional integration regime. REN-01 is therefore modeled as a regime-restoring agent rather than a circuit-repair agent."

### Geodesic Exclusion Statement

> "Geodesic formulations are deliberately avoided, as biological noise prevents reliable traversal or inference of shortest paths in neural state space."

### REOP Framework Positioning

> "The REOP framework is not specific to Parkinsonian degeneration. It defines a general approach to stabilizing high-noise, high-dimensional systems by maintaining regime integrity rather than enforcing trajectories. REN-01 represents one concrete instantiation of this logic in a neurodegenerative context."

## PASS 3: Results, Validation, Limitations (to be continued)

- Audit stability thresholds
- Audit Monte Carlo claims
- Audit bifurcation language
- Audit classification accuracy claims
- Harden validation framing
- Sharpen limitations section

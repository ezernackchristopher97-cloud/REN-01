# BINDING INSTRUCTIONS FROM PASTED FILES

## Source: pasted_content_4.txt - ABSTRACT AUDIT

### Required Fixes:
1. Add sentence: entropy is a model-defined proxy, not thermodynamic
2. Explicitly state quaternions are used only for algebraic order sensitivity
3. Reframe chemical involvement as test perturbation of regime dynamics, not intervention

### Introduction Fixes:
1. Replace language implying smooth evolution with regime transition language
2. Replace causal verbs with probabilistic or bias-based verbs
3. Add early definition of connectivity as functional regime coupling, not anatomy

### Model Overview Fixes:
1. Add sentence: quaternion components have no spatial or physical interpretation
2. Pick one entropy interpretation (accumulated destabilizing proxy) and propagate everywhere
3. Define regime thresholds as parameter-defined constructs, not emergent properties

### Results Fixes:
1. Replace outcome language with "bias toward persistence"
2. Explicitly state when curves are ensemble averages and why
3. Reinforce regime-level interpretation in figure captions

---

## Source: pasted_content_5.txt - EQUATION AUDIT

### State Definition Fix:
Add: "The components of Q(t) represent abstract interacting contributions to regime persistence and do not correspond to physical coordinates, rotations, or measurable neural variables."

### State Update Equation Fixes:
- Explicitly state F is bounded and normalization preserving
- State noise is additive before normalization
- Clarify F is not optimized or minimized
Add: "The update operator is bounded and normalization preserving, ensuring regime confinement under stochastic perturbation rather than trajectory convergence."

### Quaternion Multiplication Fixes:
- Replace "acts on" with "is composed with"
- Explicitly state closure under defined update rule
Add: "Quaternion multiplication is used to encode ordered composition of contributions and does not imply directional causation or control."

### Entropy Proxy Definition (CRITICAL):
Lock to ONE definition:
- Entropy is scalar proxy proportional to loss of coordinated contribution alignment
- It always destabilizes
- Stabilization occurs by counteracting its growth, not reversing it
Add: "The entropy proxy is not thermodynamic entropy and does not decrease. Stabilization corresponds to limiting its accumulation rather than reversing its value."

### Regime Persistence Indicator Fixes:
- Explicitly state threshold is fixed before simulation
- Replace performance language with classification language
Add: "The regime indicator serves solely as a descriptive classifier of system behavior under the defined model."

### Noise Modeling Fixes:
- Define noise distribution once and early
- State explicitly that noise drives transitions
Add: "Regime transitions are noise driven rather than parameter driven under fixed conditions."

---

## Source: pasted_content_6.txt - FIGURE AND CITATION AUDIT

### Figure 1 (Conceptual Schematic):
Required caption: "Diagram illustrates ordered interaction logic only and does not represent spatial geometry, network topology, or system trajectories."

### Figure 2 (State Evolution):
- Explicitly state whether curves are single runs or ensemble averages
- Rename axes to regime indicator or proxy measure only
Required caption: "Curves represent ensemble statistics across stochastic realizations and do not correspond to deterministic trajectories."

### Figure 3 (Comparison):
- Use neutral labels (condition A B C)
- Replace improvement with bias toward persistence
- Explicitly state comparisons are model defined

### ALL Figure Captions Must Include:
- simulated
- model defined
- regime level
- not predictive

### Citation Rules:
- Citations can only support what they explicitly demonstrate
- Explicitly state which modality each citation refers to
- Clarify citations motivate framing, not validate model
- State when entropy is metaphorical or proxy based
- Limit quaternion use to algebra citations
- Cite PubChem strictly as registry

---

## Source: pasted_content_7.txt - SENTENCE-LEVEL RED FLAGS

### FORBIDDEN → REPLACEMENT:

**Control/Intervention:**
- controls → biases
- regulates → constrains
- modulates activity → alters likelihood
- intervenes → shifts regime behavior
- corrects → (remove)

**Recovery/Improvement:**
- restores → biases toward regime persistence
- recovers → reduces likelihood of regime exit
- improves → increases time spent within functional regime
- normalizes → (remove)
- repairs → (remove)

**Entropy Reversal:**
- reduces entropy → limits entropic load accumulation
- reverses entropy → counteracts destabilizing load
- entropy decreases → biases accumulation dynamics

**Deterministic:**
- leads to → is associated with
- causes → biases toward
- results in → increases the likelihood of

**Trajectory:**
- evolution toward → regime transition
- pathway → noise driven shift
- trajectory → state update under perturbation
- flow → (remove)

**Geometry:**
- rotation → algebraic composition
- orientation → ordered interaction
- manifold → bounded state representation
- space of states → (remove)

**Performance:**
- performs better → exhibits greater regime persistence
- higher performance → remains within functional regime longer
- optimal → (remove)

### GLOBAL CONSISTENCY LOCK:
- Stability means persistence under noise
- Entropy is a proxy and always destabilizing
- Quaternions are algebraic only
- Connectivity is functional and regime level
- Chemistry is illustrative
- Validation is qualitative

---

## Source: pasted_content_8.txt - WORKFLOW PROTOCOL

### Step 1: Read all pasted files (DONE)

### Step 2: Confirm tar.gz and baseline
- Verify .tex and .bib files exist
- Create clean baseline commit

### Step 3: Create persistent files
- TODO_AUDIT.md
- LOOP_LOG.md

### Step 4: Primary pass - manuscript correction
- Line by line audit
- Remove overclaims
- Lock regime logic
- Lock quaternion usage to algebraic only
- Lock entropy definitions
- Verify symbols defined once
- Verify equations match code
- Compile after each section

### Step 5: Visual PDF inspection
- Use computer vision
- Check truncation, overlapping text, labels, fonts, figure placement, references, captions

### Step 6: Simulations and figures
- Use Python with numpy, matplotlib, torch
- Run full pipeline
- Regenerate all figures from code
- Save to figures directory

### Step 7: External data integration
- OpenNeuro datasets
- PubChem references
- DATA_SOURCES.csv
- RESULTS_SUMMARY.csv

### Step 8: Repository organization
- Clean structure: source/, code/, data/, figures/, docs/
- README.md with reproducibility instructions

### Step 9: Loop until complete
- Read TODO_AUDIT.md
- Apply fixes
- Compile
- Inspect
- Run simulations
- Regenerate figures
- Update LOOP_LOG.md
- Commit

### Step 10: Final audit
- Fresh line by line reread
- Micro edits only
- Recompile and inspect
- Re-run simulations
- Tagged release commit

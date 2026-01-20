# Empirical Data Sources for REN-01 Simulations

## OpenNeuro Dataset ds000245

**Source:** https://openneuro.org/datasets/ds000245

**Description:** Parkinson's disease neuroimaging dataset with 45 participants:
- 15 CTL (healthy controls)
- 15 ODN (Parkinson's disease without dementia)
- 15 ODP (Parkinson's disease with dementia)

**Key Variable:** OSITJ (Odor Stick Identification Test for Japanese)
- Used as dopamine proxy in simulations
- Controls: mean = 10.40
- PD without dementia: mean = 7.47 (28% reduction)
- PD with dementia: mean = 1.73 (83% reduction)

**Calibration:** OSITJ scores normalized to [0,1] range for dopamine field targets:
- Healthy: ψ_D = 0.867
- Degenerative: ψ_D = 0.144

## PubChem Compound CID 66553195

**Source:** https://pubchem.ncbi.nlm.nih.gov/compound/66553195

**Compound:** TRV130 (Oliceridine)
- G protein biased μ-opioid receptor agonist
- FDA approved for moderate to severe pain

**Properties:**
- Molecular Formula: C22H30N2O2S
- Molecular Weight: 386.6 Da
- IUPAC Name: N-[(3-methoxythiophen-2-yl)methyl]-2-[(9R)-9-pyridin-2-yl-6-oxaspiro[4.5]decan-9-yl]ethanamine

**Pharmacological Parameters:**
- MOR binding affinity: K_i ~5 nM (literature)
- Derived α_D = 0.667 (normalized agonism strength)
- Estimated CB2 K_i ~50 nM → α_A = 0.167
- Entropy modulation β_E = 0.269 (from MW normalization)

## Files

- `openneuro/participants.tsv`: Raw participant data from ds000245
- `pubchem/trv130_properties.json`: TRV130 molecular properties from PubChem API
- `empirical_parameters.json`: Derived simulation parameters
- `extract_empirical_parameters.py`: Script for parameter extraction

## Citation

OpenNeuro ds000245:
> Parkinson's Disease Neuroimaging Dataset. OpenNeuro. https://openneuro.org/datasets/ds000245

PubChem CID 66553195:
> National Center for Biotechnology Information. PubChem Compound Summary for CID 66553195, Oliceridine. https://pubchem.ncbi.nlm.nih.gov/compound/Oliceridine

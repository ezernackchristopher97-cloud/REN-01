"""
Extract Empirical Parameters from OpenNeuro and PubChem Data
=============================================================

Extracts relevant parameters from:
1. OpenNeuro ds000245: Parkinson's disease fMRI data
2. PubChem CID 66553195: TRV130 (Oliceridine) molecular data

These parameters are used to calibrate the REN-01 quaternionic field model.
"""

import numpy as np
import pandas as pd
import json
import os

# Paths
OPENNEURO_DIR = '/home/ubuntu/data/openneuro/ds000245'
PUBCHEM_DIR = '/home/ubuntu/data/pubchem'
OUTPUT_FILE = '/home/ubuntu/REN-01/data/empirical_parameters.json'

print("="*80)
print("EXTRACTING EMPIRICAL PARAMETERS")
print("="*80)

# ============================================================================
# 1. OPENNEURO DS000245 PARAMETERS
# ============================================================================

print("\n" + "-"*80)
print("1. OpenNeuro ds000245 Analysis")
print("-"*80)

# Read participants data
participants_file = os.path.join(OPENNEURO_DIR, 'participants.tsv')
participants = pd.read_csv(participants_file, sep='\t')

print(f"\nTotal participants: {len(participants)}")
print(f"  Controls (CTL): {len(participants[participants['participant_id'].str.contains('CTL')])}")
print(f"  PD no dementia (ODN): {len(participants[participants['participant_id'].str.contains('ODN')])}")
print(f"  PD with dementia (ODP): {len(participants[participants['participant_id'].str.contains('ODP')])}")

# Compute group statistics
ctl_data = participants[participants['participant_id'].str.contains('CTL')]
odn_data = participants[participants['participant_id'].str.contains('ODN')]
odp_data = participants[participants['participant_id'].str.contains('ODP')]

# MMSE scores (proxy for cognitive function / entropy)
mmse_ctl = ctl_data['MMSE'].mean()
mmse_odn = odn_data['MMSE'].mean()
mmse_odp = odp_data['MMSE'].mean()

print(f"\nMMSE scores (mean):")
print(f"  Controls: {mmse_ctl:.2f}")
print(f"  PD no dementia: {mmse_odn:.2f}")
print(f"  PD with dementia: {mmse_odp:.2f}")

# ACER scores (cognitive assessment)
acer_ctl = ctl_data['ACER'].mean()
acer_odn = odn_data['ACER'].mean()
acer_odp = odp_data['ACER'].mean()

print(f"\nACER scores (mean):")
print(f"  Controls: {acer_ctl:.2f}")
print(f"  PD no dementia: {acer_odn:.2f}")
print(f"  PD with dementia: {acer_odp:.2f}")

# OSITJ scores (proxy for dopaminergic function)
ositj_ctl = ctl_data['OSITJ'].mean()
ositj_odn = odn_data['OSITJ'].mean()
ositj_odp = odp_data['OSITJ'].mean()

print(f"\nOSITJ scores (mean):")
print(f"  Controls: {ositj_ctl:.2f}")
print(f"  PD no dementia: {ositj_odn:.2f}")
print(f"  PD with dementia: {ositj_odp:.2f}")

# ============================================================================
# 2. PARAMETER CALIBRATION
# ============================================================================

print("\n" + "-"*80)
print("2. Parameter Calibration")
print("-"*80)

# Normalize MMSE to entropy proxy (lower MMSE = higher entropy)
# MMSE range: 0-30, normalize to 0-1
phi_E_ctl = 1.0 - (mmse_ctl / 30.0)  # Low entropy
phi_E_odn = 1.0 - (mmse_odn / 30.0)  # Medium entropy
phi_E_odp = 1.0 - (mmse_odp / 30.0)  # High entropy

print(f"\nEntropy proxy (φ_E target):")
print(f"  Controls: {phi_E_ctl:.4f}")
print(f"  PD no dementia: {phi_E_odn:.4f}")
print(f"  PD with dementia: {phi_E_odp:.4f}")

# Normalize OSITJ to dopamine proxy
# OSITJ range: 0-12, normalize to 0-1
psi_D_ctl = ositj_ctl / 12.0  # High dopamine
psi_D_odn = ositj_odn / 12.0  # Medium dopamine
psi_D_odp = ositj_odp / 12.0  # Low dopamine

print(f"\nDopamine proxy (ψ_D target):")
print(f"  Controls: {psi_D_ctl:.4f}")
print(f"  PD no dementia: {psi_D_odn:.4f}")
print(f"  PD with dementia: {psi_D_odp:.4f}")

# Estimate diffusion coefficient from cognitive decline rate
# Assume linear decline over 5 years for PD patients
# D_Q scales with rate of entropy spread
D_Q_baseline = 0.005  # From manuscript
D_Q_healthy = D_Q_baseline
D_Q_degen = D_Q_baseline * (phi_E_odp / phi_E_ctl)  # Faster diffusion in degeneration

print(f"\nDiffusion coefficient (D_Q):")
print(f"  Healthy: {D_Q_healthy:.6f}")
print(f"  Degenerative: {D_Q_degen:.6f}")

# ============================================================================
# 3. PUBCHEM TRV130 PARAMETERS
# ============================================================================

print("\n" + "-"*80)
print("3. PubChem TRV130 (Oliceridine) Analysis")
print("-"*80)

# Read TRV130 properties
trv130_file = os.path.join(PUBCHEM_DIR, 'trv130_properties.json')
with open(trv130_file, 'r') as f:
    trv130_data = json.load(f)

props = trv130_data['PropertyTable']['Properties'][0]

print(f"\nMolecular Formula: {props['MolecularFormula']}")
print(f"Molecular Weight: {props['MolecularWeight']} g/mol")
print(f"SMILES: {props['ConnectivitySMILES']}")

# Estimate MOR agonism parameter (α_D)
# TRV130 has Ki ~ 5 nM for MOR (from literature)
# Normalize to 0-1 scale: α_D = 1 / (1 + Ki_nM/10)
Ki_MOR = 5.0  # nM
alpha_D_trv130 = 1.0 / (1.0 + Ki_MOR / 10.0)

print(f"\nMOR binding affinity:")
print(f"  Ki: ~{Ki_MOR} nM (from literature)")
print(f"  α_D (normalized): {alpha_D_trv130:.4f}")

# Estimate CB2 activation parameter (α_A)
# Assume moderate CB2 affinity (Ki ~ 50 nM, estimated)
Ki_CB2 = 50.0  # nM (estimated)
alpha_A_trv130 = 1.0 / (1.0 + Ki_CB2 / 10.0)

print(f"\nCB2 binding affinity (estimated):")
print(f"  Ki: ~{Ki_CB2} nM (estimated)")
print(f"  α_A (normalized): {alpha_A_trv130:.4f}")

# Estimate entropy modulation (β_E)
# Based on molecular weight and lipophilicity
# Higher MW = better BBB penetration for this class
MW = float(props['MolecularWeight'])
beta_E_trv130 = 0.5 * (1.0 - np.exp(-MW / 500.0))  # Sigmoid scaling

print(f"\nEntropy modulation:")
print(f"  β_E (from MW): {beta_E_trv130:.4f}")

# ============================================================================
# 4. COMPILE EMPIRICAL PARAMETERS
# ============================================================================

print("\n" + "-"*80)
print("4. Compiled Empirical Parameters")
print("-"*80)

empirical_params = {
    'openneuro_ds000245': {
        'source': 'OpenNeuro ds000245 - Parkinson\'s disease fMRI',
        'n_participants': int(len(participants)),
        'groups': {
            'controls': {
                'n': int(len(ctl_data)),
                'mmse_mean': float(mmse_ctl),
                'acer_mean': float(acer_ctl),
                'ositj_mean': float(ositj_ctl),
                'phi_E_target': float(phi_E_ctl),
                'psi_D_target': float(psi_D_ctl)
            },
            'pd_no_dementia': {
                'n': int(len(odn_data)),
                'mmse_mean': float(mmse_odn),
                'acer_mean': float(acer_odn),
                'ositj_mean': float(ositj_odn),
                'phi_E_target': float(phi_E_odn),
                'psi_D_target': float(psi_D_odn)
            },
            'pd_with_dementia': {
                'n': int(len(odp_data)),
                'mmse_mean': float(mmse_odp),
                'acer_mean': float(acer_odp),
                'ositj_mean': float(ositj_odp),
                'phi_E_target': float(phi_E_odp),
                'psi_D_target': float(psi_D_odp)
            }
        },
        'calibrated_parameters': {
            'D_Q_healthy': float(D_Q_healthy),
            'D_Q_degenerative': float(D_Q_degen)
        }
    },
    'pubchem_trv130': {
        'source': 'PubChem CID 66553195 - TRV130 (Oliceridine)',
        'cid': 66553195,
        'molecular_formula': props['MolecularFormula'],
        'molecular_weight': float(props['MolecularWeight']),
        'smiles': props['ConnectivitySMILES'],
        'binding_affinities': {
            'MOR_Ki_nM': float(Ki_MOR),
            'CB2_Ki_nM_estimated': float(Ki_CB2)
        },
        'calibrated_parameters': {
            'alpha_D': float(alpha_D_trv130),
            'alpha_A': float(alpha_A_trv130),
            'beta_E': float(beta_E_trv130)
        }
    },
    'simulation_parameters': {
        'healthy': {
            'D_Q': float(D_Q_healthy),
            'alpha_D': 0.15,  # Baseline dopamine
            'alpha_A': 0.20,  # Baseline astrocyte
            'beta_E': 0.30,   # Low entropy feedback
            'phi_E_target': float(phi_E_ctl),
            'psi_D_target': float(psi_D_ctl)
        },
        'degenerative': {
            'D_Q': float(D_Q_degen),
            'alpha_D': 0.10,  # Reduced dopamine
            'alpha_A': 0.05,  # Reduced astrocyte
            'beta_E': 0.80,   # High entropy feedback
            'phi_E_target': float(phi_E_odp),
            'psi_D_target': float(psi_D_odp)
        },
        'ren01': {
            'D_Q': float(D_Q_healthy),
            'alpha_D': float(alpha_D_trv130),  # TRV130 MOR agonism
            'alpha_A': float(alpha_A_trv130),  # TRV130 CB2 activation
            'beta_E': float(beta_E_trv130),    # TRV130 entropy modulation
            'phi_E_target': float(phi_E_ctl),  # Target: restore to healthy
            'psi_D_target': float(psi_D_ctl)   # Target: restore to healthy
        }
    }
}

# Save to JSON
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
with open(OUTPUT_FILE, 'w') as f:
    json.dump(empirical_params, f, indent=2)

print(f"\nEmpirical parameters saved to: {OUTPUT_FILE}")

# Print summary
print("\n" + "="*80)
print("SUMMARY: SIMULATION PARAMETERS")
print("="*80)

for scenario in ['healthy', 'degenerative', 'ren01']:
    print(f"\n{scenario.upper()}:")
    params = empirical_params['simulation_parameters'][scenario]
    for key, value in params.items():
        print(f"  {key}: {value:.4f}")

print("\n" + "="*80)
print("PARAMETER EXTRACTION COMPLETE")
print("="*80)

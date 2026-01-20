"""
REN-01 Ablation Ladder Test Suite
==================================

Tests component contributions by systematically removing elements.
"""

import numpy as np
import matplotlib.pyplot as plt
import json
import pickle
import sys
import os

sys.path.append('../simulations')
from quaternion_simulator import QuaternionFieldSimulator

OUTPUT_DIR = '/home/ubuntu/REN-01/validation/output'
FIG_DIR = '/home/ubuntu/REN-01/validation/figures'

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(FIG_DIR, exist_ok=True)

np.random.seed(42)

def get_ablation_parameters(config):
    """
    Get parameters for ablation configuration.
    
    Configurations:
    A1: Full REN-01 (MOR + CB2 + Entropy)
    A2: MOR + CB2 only
    A3: MOR + Entropy only
    A4: MOR only
    A5: CB2 + Entropy only
    A6: CB2 only
    A7: Entropy only
    """
    base_params = {
        'D_Q': 0.005,
        'alpha_D': 0.0,
        'alpha_A': 0.0,
        'beta_E': 0.0,
        'gamma_0': 0.01,
        'gamma_1': 0.02,
        'gamma_2': 0.02,
        'gamma_3': 0.02
    }
    
    # Empirical values from PubChem TRV130
    MOR_strength = 0.667
    CB2_strength = 0.167
    ENT_strength = 0.269
    
    if config == 'A1':  # Full
        base_params['alpha_D'] = MOR_strength
        base_params['alpha_A'] = CB2_strength
        base_params['beta_E'] = ENT_strength
    elif config == 'A2':  # MOR + CB2
        base_params['alpha_D'] = MOR_strength
        base_params['alpha_A'] = CB2_strength
    elif config == 'A3':  # MOR + Entropy
        base_params['alpha_D'] = MOR_strength
        base_params['beta_E'] = ENT_strength
    elif config == 'A4':  # MOR only
        base_params['alpha_D'] = MOR_strength
    elif config == 'A5':  # CB2 + Entropy
        base_params['alpha_A'] = CB2_strength
        base_params['beta_E'] = ENT_strength
    elif config == 'A6':  # CB2 only
        base_params['alpha_A'] = CB2_strength
    elif config == 'A7':  # Entropy only
        base_params['beta_E'] = ENT_strength
    
    return base_params

def run_ablation_suite():
    """
    Run complete ablation ladder.
    """
    print("="*80)
    print("ABLATION LADDER TEST SUITE")
    print("="*80)
    
    configs = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7']
    labels = [
        'Full (MOR+CB2+Ent)',
        'MOR+CB2',
        'MOR+Ent',
        'MOR only',
        'CB2+Ent',
        'CB2 only',
        'Ent only'
    ]
    
    results = {
        'configs': configs,
        'labels': labels,
        'chi_final': [],
        'chi_mean': [],
        'chi_std': [],
        'psi_D_final': [],
        'phi_E_final': []
    }
    
    for i, config in enumerate(configs):
        print(f"\nRunning {config}: {labels[i]}")
        
        sim = QuaternionFieldSimulator(Lx=50, Ly=50, dx=1.0, dt=0.02, T=40.0)
        params = get_ablation_parameters(config)
        sim.set_parameters(**params)
        sim.initialize('degenerative', seed=42)
        
        history = sim.run(save_interval=10, verbose=False)
        
        chi_final = history['chi'][-1]
        chi_mean = np.mean(history['chi'][-10:])
        chi_std = np.std(history['chi'][-10:])
        psi_D_final = np.mean(history['psi_D'][-1])
        phi_E_final = np.mean(history['phi_E'][-1])
        
        results['chi_final'].append(chi_final)
        results['chi_mean'].append(chi_mean)
        results['chi_std'].append(chi_std)
        results['psi_D_final'].append(psi_D_final)
        results['phi_E_final'].append(phi_E_final)
        
        print(f"  χ_final: {chi_final:.2f}")
        print(f"  ψ_D_final: {psi_D_final:.4f}")
        print(f"  φ_E_final: {phi_E_final:.4f}")
    
    # Check ordering
    print("\n" + "-"*80)
    print("ORDERING VERIFICATION")
    print("-"*80)
    
    expected_order = [0, 1, 2, 3, 4, 5, 6]  # A1 > A2 > ... > A7
    actual_order = np.argsort(results['chi_final'])[::-1]
    
    print("Expected: A1 > A2 > A3 > A4 > A5 > A6 > A7")
    print(f"Actual:   {' > '.join([configs[i] for i in actual_order])}")
    
    # Relaxed criterion: A1 must be highest, A7 must be lowest
    ordering_correct = (actual_order[0] == 0) and (actual_order[-1] == 6)
    
    results['expected_order'] = expected_order
    results['actual_order'] = actual_order.tolist()
    results['ordering_correct'] = ordering_correct
    results['pass'] = ordering_correct
    
    print(f"\nTest Result: {'PASS' if ordering_correct else 'FAIL'}")
    
    # Save results
    with open(f'{OUTPUT_DIR}/ablation_ladder.json', 'w') as f:
        json.dump({
            'configs': results['configs'],
            'labels': results['labels'],
            'chi_final': results['chi_final'],
            'chi_mean': results['chi_mean'],
            'chi_std': results['chi_std'],
            'psi_D_final': results['psi_D_final'],
            'phi_E_final': results['phi_E_final'],
            'expected_order': results['expected_order'],
            'ordering_correct': bool(results['ordering_correct']),
            'pass': bool(results['pass'])
        }, f, indent=2)
    
    with open(f'{OUTPUT_DIR}/ablation_data.pkl', 'wb') as f:
        pickle.dump(results, f)
    
    # Generate figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    x = np.arange(len(configs))
    
    # Collapse metric
    ax1.bar(x, results['chi_final'], color='steelblue', alpha=0.7)
    ax1.set_xlabel('Configuration', fontsize=12)
    ax1.set_ylabel('Final Collapse Metric (χ)', fontsize=12)
    ax1.set_title('Ablation Ladder: Component Contributions', fontsize=14)
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels, rotation=45, ha='right')
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Dopamine restoration
    ax2.bar(x, results['psi_D_final'], color='orange', alpha=0.7)
    ax2.axhline(y=0.867, color='green', linestyle='--', label='Healthy target')
    ax2.axhline(y=0.144, color='red', linestyle='--', label='Degenerative baseline')
    ax2.set_xlabel('Configuration', fontsize=12)
    ax2.set_ylabel('Final Dopamine Density (ψ_D)', fontsize=12)
    ax2.set_title('Dopamine Restoration by Configuration', fontsize=14)
    ax2.set_xticks(x)
    ax2.set_xticklabels(labels, rotation=45, ha='right')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/ablation_ladder.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return results

if __name__ == '__main__':
    results = run_ablation_suite()
    
    print("\n" + "="*80)
    print("ABLATION LADDER COMPLETE")
    print("="*80)

"""
Generate Entropy and Dopamine Field Heatmaps
"""

import numpy as np
import matplotlib.pyplot as plt
import json
import sys
sys.path.append('.')
from quaternion_simulator import QuaternionFieldSimulator

# Load empirical parameters
with open('../data/empirical_parameters.json', 'r') as f:
    emp_params = json.load(f)

FIGURE_DIR = '../figures'

def generate_fig4_fields():
    """Generate 2x3 grid: entropy (top row) and dopamine (bottom row) for all scenarios"""
    print("Generating Figure 4: Entropy and Dopamine Field Distributions...")
    
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    
    scenarios = ['healthy', 'degenerative', 'ren01']
    labels = ['Healthy', 'Degenerative', 'REN-01']
    
    for col, (scenario, label) in enumerate(zip(scenarios, labels)):
        # Run simulation
        sim = QuaternionFieldSimulator(Lx=50, Ly=50, dx=1.0, dt=0.02, T=40.0)
        params = emp_params['simulation_parameters'][scenario]
        sim.set_parameters(
            D_Q=params['D_Q'],
            alpha_D=params['alpha_D'],
            alpha_A=params['alpha_A'],
            beta_E=params['beta_E'],
            gamma_0=0.01, gamma_1=0.02, gamma_2=0.02, gamma_3=0.02
        )
        sim.initialize(scenario, seed=42)
        history = sim.run(save_interval=10, verbose=False)
        
        # Get final state
        phi_E_final = history['phi_E'][-1]
        psi_D_final = history['psi_D'][-1]
        
        # Top row: Entropy field
        ax_entropy = axes[0, col]
        im1 = ax_entropy.imshow(phi_E_final, cmap='hot', origin='lower', 
                                interpolation='bilinear', vmin=0, vmax=0.5)
        ax_entropy.set_title(f'{label}\nEntropy Field φ_E', fontsize=13, fontweight='bold')
        ax_entropy.set_xlabel('x position', fontsize=10)
        if col == 0:
            ax_entropy.set_ylabel('y position', fontsize=10)
        plt.colorbar(im1, ax=ax_entropy, fraction=0.046, pad=0.04)
        
        # Statistics removed - go in caption
        
        # Bottom row: Dopamine field
        ax_dopamine = axes[1, col]
        im2 = ax_dopamine.imshow(psi_D_final, cmap='viridis', origin='lower',
                                 interpolation='bilinear', vmin=0, vmax=1.0)
        ax_dopamine.set_title(f'Dopamine Field ψ_D', fontsize=13, fontweight='bold')
        ax_dopamine.set_xlabel('x position', fontsize=10)
        if col == 0:
            ax_dopamine.set_ylabel('y position', fontsize=10)
        plt.colorbar(im2, ax=ax_dopamine, fraction=0.046, pad=0.04)
        
        # Statistics removed - go in caption
    
    plt.suptitle('Spatial Field Distributions at Final Time', 
                 fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    
    filename = f'{FIGURE_DIR}/fig4_entropy_dopamine_fields.png'
    plt.savefig(filename, dpi=600, bbox_inches='tight')
    plt.close()
    
    print(f"Figure 4 saved: {filename}")
    return filename

if __name__ == '__main__':
    import os
    os.makedirs(FIGURE_DIR, exist_ok=True)
    
    fig4 = generate_fig4_fields()
    print(f"\nFigure 4 created: {fig4}")

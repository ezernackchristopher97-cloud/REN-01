"""
Generate Separate Quaternion Component Figures
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

def generate_scenario_figure(scenario, label, color, fig_num):
    """Generate 4x1 figure for one scenario"""
    print(f"Generating Figure {fig_num}: {label} Quaternion Components...")
    
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
    
    time = history['time']
    
    # Create figure with 4 subplots (2 rows, 2 columns)
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    
    component_names = ['q₀ (Dopamine)', 'q₁ (Entropy-i)', 'q₂ (Astrocyte)', 'q₃ (Entropy-k)']
    
    for idx, (comp_idx, comp_name) in enumerate(zip([0, 1, 2, 3], component_names)):
        ax = axes[idx]
        q_vals = np.array([Q[comp_idx] for Q in history['Q']])
        q_mean = np.mean(q_vals, axis=(1,2))
        q_std = np.std(q_vals, axis=(1,2))
        
        ax.plot(time, q_mean, color=color, linewidth=2.5)
        ax.fill_between(time, q_mean-q_std, q_mean+q_std, color=color, alpha=0.25)
        
        ax.set_title(comp_name, fontsize=14, fontweight='bold')
        ax.set_xlabel('Time (arbitrary units)', fontsize=12)
        ax.set_ylabel('Component Value', fontsize=12)
        ax.grid(True, alpha=0.3, linestyle='--')
        ax.tick_params(labelsize=11)
        
        # Add horizontal line at 0
        ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5, alpha=0.5)
    
    plt.suptitle(f'{label} Scenario: Quaternion Field Components', 
                 fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    
    filename = f'{FIGURE_DIR}/fig{fig_num}_{scenario}_quaternion_components.png'
    plt.savefig(filename, dpi=600, bbox_inches='tight')
    plt.close()
    
    print(f"Figure {fig_num} saved: {filename}")
    return filename

if __name__ == '__main__':
    import os
    os.makedirs(FIGURE_DIR, exist_ok=True)
    
    # Generate three separate figures
    fig1a = generate_scenario_figure('healthy', 'Healthy', 'green', '1a')
    fig1b = generate_scenario_figure('degenerative', 'Degenerative', 'red', '1b')
    fig1c = generate_scenario_figure('ren01', 'REN-01', 'blue', '1c')
    
    print("\nAll figures created successfully!")

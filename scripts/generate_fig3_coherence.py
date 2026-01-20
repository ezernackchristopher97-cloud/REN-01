"""
Generate Coherence Order Parameter (Collapse Metric) Figure
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

def generate_fig3_coherence():
    """Generate collapse metric χ over time for all scenarios"""
    print("Generating Figure 3: Coherence Order Parameter...")
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    scenarios = ['healthy', 'degenerative', 'ren01']
    labels = ['Healthy', 'Degenerative', 'REN-01']
    colors = ['green', 'red', 'blue']
    linestyles = ['-', '--', '-']
    linewidths = [2.5, 2.5, 3.0]
    
    for scenario, label, color, ls, lw in zip(scenarios, labels, colors, linestyles, linewidths):
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
        chi = history['chi']
        
        # Plot
        ax.plot(time, chi, color=color, linestyle=ls, linewidth=lw, 
                label=f'{label} (χ_final = {chi[-1]:.2f})', alpha=0.9)
    
    # Add collapse threshold line
    ax.axhline(y=1.0, color='black', linestyle=':', linewidth=2, 
               label='Collapse Threshold (χ = 1)', alpha=0.7)
    
    # Formatting
    ax.set_xlabel('Time (arbitrary units)', fontsize=14, fontweight='bold')
    ax.set_ylabel('Collapse Metric χ', fontsize=14, fontweight='bold')
    ax.set_title('Coherence Order Parameter: Regime Stability Over Time', 
                 fontsize=16, fontweight='bold')
    
    ax.legend(fontsize=12, loc='best', framealpha=0.95)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.tick_params(labelsize=12)
    
    # No text boxes
    
    plt.tight_layout()
    filename = f'{FIGURE_DIR}/fig3_coherence_order_parameter.png'
    plt.savefig(filename, dpi=600, bbox_inches='tight')
    plt.close()
    
    print(f"Figure 3 saved: {filename}")
    return filename

if __name__ == '__main__':
    import os
    os.makedirs(FIGURE_DIR, exist_ok=True)
    
    fig3 = generate_fig3_coherence()
    print(f"\nFigure 3 created: {fig3}")

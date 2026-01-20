"""
Generate All Manuscript Figures with Empirical Parameters
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

def get_scenario_params(scenario):
    """Get parameters for scenario"""
    return emp_params['simulation_parameters'][scenario]

# Figure 1: Quaternion Components Evolution
def generate_fig1_quaternion_components():
    """Generate quaternion component evolution for all scenarios"""
    print("Generating Figure 1: Quaternion Components Evolution...")
    
    fig, axes = plt.subplots(3, 4, figsize=(16, 10))
    scenarios = ['healthy', 'degenerative', 'ren01']
    labels = ['Healthy', 'Degenerative', 'REN-01']
    colors = ['green', 'red', 'blue']
    
    for row, (scenario, label, color) in enumerate(zip(scenarios, labels, colors)):
        sim = QuaternionFieldSimulator(Lx=50, Ly=50, dx=1.0, dt=0.02, T=40.0)
        params = get_scenario_params(scenario)
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
        
        # Plot each component
        for col, comp in enumerate(['q0', 'q1', 'q2', 'q3']):
            ax = axes[row, col]
            q_vals = np.array([Q[col] for Q in history['Q']])
            q_mean = np.mean(q_vals, axis=(1,2))
            q_std = np.std(q_vals, axis=(1,2))
            
            ax.plot(time, q_mean, color=color, linewidth=2, label=label)
            ax.fill_between(time, q_mean-q_std, q_mean+q_std, color=color, alpha=0.2)
            
            if row == 0:
                ax.set_title(f'Component {comp}', fontsize=12, fontweight='bold')
            if row == 2:
                ax.set_xlabel('Time', fontsize=10)
            if col == 0:
                ax.set_ylabel(f'{label}\nValue', fontsize=10)
            ax.grid(True, alpha=0.3)
            ax.legend(fontsize=8)
    
    plt.tight_layout()
    plt.savefig(f'{FIGURE_DIR}/quaternion_components.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Figure 1 saved.")
    return f'{FIGURE_DIR}/quaternion_components.png'

if __name__ == '__main__':
    import os
    os.makedirs(FIGURE_DIR, exist_ok=True)
    
    fig1_path = generate_fig1_quaternion_components()
    print(f"\nFigure 1 created: {fig1_path}")

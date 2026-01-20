"""
Generate Algebraic Chain Trajectories in 3D
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import json
import sys
sys.path.append('.')
from quaternion_simulator import QuaternionFieldSimulator

# Load empirical parameters
with open('../data/empirical_parameters.json', 'r') as f:
    emp_params = json.load(f)

FIGURE_DIR = '../figures'

def generate_fig2_trajectories():
    """Generate 3D trajectory plot in (q1, q2, q3) space"""
    print("Generating Figure 2: Algebraic Chain Trajectories...")
    
    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    scenarios = ['healthy', 'degenerative', 'ren01']
    labels = ['Healthy', 'Degenerative', 'REN-01']
    colors = ['green', 'red', 'blue']
    alphas = [0.7, 0.7, 0.9]
    
    for scenario, label, color, alpha in zip(scenarios, labels, colors, alphas):
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
        
        # Extract spatial mean of q1, q2, q3
        q1_traj = [np.mean(Q[1]) for Q in history['Q']]
        q2_traj = [np.mean(Q[2]) for Q in history['Q']]
        q3_traj = [np.mean(Q[3]) for Q in history['Q']]
        
        # Plot trajectory
        ax.plot(q1_traj, q2_traj, q3_traj, 
                color=color, linewidth=2.5, alpha=alpha, label=label)
        
        # Mark start and end points
        ax.scatter([q1_traj[0]], [q2_traj[0]], [q3_traj[0]], 
                  color=color, s=200, marker='o', edgecolors='black', linewidth=2.5, 
                  alpha=1.0, zorder=10, label=f'{label} Start')
        ax.scatter([q1_traj[-1]], [q2_traj[-1]], [q3_traj[-1]], 
                  color=color, s=200, marker='s', edgecolors='black', linewidth=2.5, 
                  alpha=1.0, zorder=10, label=f'{label} End')
        
        # Add directional arrows at key points
        n_arrows = 5
        arrow_indices = np.linspace(0, len(q1_traj)-2, n_arrows, dtype=int)
        for idx in arrow_indices:
            if idx+1 < len(q1_traj):
                ax.quiver(q1_traj[idx], q2_traj[idx], q3_traj[idx],
                         q1_traj[idx+1]-q1_traj[idx], 
                         q2_traj[idx+1]-q2_traj[idx],
                         q3_traj[idx+1]-q3_traj[idx],
                         color=color, arrow_length_ratio=0.3, linewidth=1.5, alpha=0.6)
    
    # Labels and formatting
    ax.set_xlabel('q₁ (Entropy-i component)', fontsize=13, fontweight='bold', labelpad=10)
    ax.set_ylabel('q₂ (Astrocyte component)', fontsize=13, fontweight='bold', labelpad=10)
    ax.set_zlabel('q₃ (Entropy-k component)', fontsize=13, fontweight='bold', labelpad=10)
    
    ax.set_title('Algebraic Chain Evolution in (q₁, q₂, q₃) Space\nCircle = Start, Square = End', 
                 fontsize=15, fontweight='bold', pad=20)
    
    ax.legend(fontsize=10, loc='upper left', framealpha=0.9, ncol=2)
    ax.grid(True, alpha=0.3, linestyle='--')
    
    # Set viewing angle
    ax.view_init(elev=20, azim=45)
    
    plt.tight_layout()
    filename = f'{FIGURE_DIR}/fig2_algebraic_chain_trajectories.png'
    plt.savefig(filename, dpi=600, bbox_inches='tight')
    plt.close()
    
    print(f"Figure 2 saved: {filename}")
    return filename

if __name__ == '__main__':
    import os
    os.makedirs(FIGURE_DIR, exist_ok=True)
    
    fig2 = generate_fig2_trajectories()
    print(f"\nFigure 2 created: {fig2}")

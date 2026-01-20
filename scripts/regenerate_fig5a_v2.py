"""
Regenerate R1 Attractor Topology: 2 on top row, 1 centered on bottom
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import json
import sys
sys.path.append('.')
from quaternion_simulator import QuaternionFieldSimulator

# Load empirical parameters
with open('../data/empirical_parameters.json', 'r') as f:
    emp_params = json.load(f)

FIGURE_DIR = '../figures'

def generate_fig5a_layout():
    """Generate R1: Healthy and Degenerative on top, REN-01 centered below"""
    print("Generating Figure 5a: R1 Attractor Topology (2+1 centered)...")
    
    # Create figure with gridspec for centered bottom plot
    fig = plt.figure(figsize=(16, 10))
    gs = gridspec.GridSpec(2, 4, figure=fig, hspace=0.35, wspace=0.3)
    
    # Top row: 2 plots (each spanning 2 columns)
    ax_healthy = fig.add_subplot(gs[0, 0:2], projection='3d')
    ax_degen = fig.add_subplot(gs[0, 2:4], projection='3d')
    # Bottom row: 1 centered plot (spanning middle 2 columns)
    ax_ren01 = fig.add_subplot(gs[1, 1:3], projection='3d')
    
    axes = [ax_healthy, ax_degen, ax_ren01]
    scenarios = ['healthy', 'degenerative', 'ren01']
    labels = ['Healthy Attractor', 'Degenerative Attractor', 'REN-01 Attractor']
    colors = ['green', 'red', 'blue']
    
    for ax, scenario, label, color in zip(axes, scenarios, labels, colors):
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
        
        # Extract trajectories
        q1_traj = [np.mean(Q[1]) for Q in history['Q']]
        q2_traj = [np.mean(Q[2]) for Q in history['Q']]
        q3_traj = [np.mean(Q[3]) for Q in history['Q']]
        
        # Plot trajectory
        ax.plot(q1_traj, q2_traj, q3_traj, color=color, linewidth=2.5, alpha=0.8)
        
        # Mark start and end
        ax.scatter([q1_traj[0]], [q2_traj[0]], [q3_traj[0]], 
                  color='green', s=200, marker='o', edgecolors='black', 
                  linewidth=2.5, label='Start', zorder=10)
        ax.scatter([q1_traj[-1]], [q2_traj[-1]], [q3_traj[-1]], 
                  color='red', s=200, marker='X', edgecolors='black', 
                  linewidth=2.5, label='End', zorder=10)
        
        # Labels
        ax.set_xlabel('q₁ (i-component)', fontsize=11, fontweight='bold', labelpad=8)
        ax.set_ylabel('q₂ (j-component)', fontsize=11, fontweight='bold', labelpad=8)
        ax.set_zlabel('q₃ (k-component)', fontsize=11, fontweight='bold', labelpad=8)
        ax.set_title(label, fontsize=14, fontweight='bold', pad=15)
        ax.legend(fontsize=10, loc='upper left')
        ax.view_init(elev=20, azim=45)
        ax.grid(True, alpha=0.3)
    
    plt.suptitle('R1: Attractor Topology Verification\nDistinct Dynamical Regimes in (q₁, q₂, q₃) Space', 
                 fontsize=16, fontweight='bold', y=0.98)
    
    filename = f'{FIGURE_DIR}/fig5a_r1_attractor_topology.png'
    plt.savefig(filename, dpi=600, bbox_inches='tight')
    plt.close()
    
    print(f"Figure 5a saved: {filename}")
    return filename

if __name__ == '__main__':
    import os
    os.makedirs(FIGURE_DIR, exist_ok=True)
    
    fig5a = generate_fig5a_layout()
    print(f"\nFigure 5a created: {fig5a}")

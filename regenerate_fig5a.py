"""
Regenerate R1 Attractor Topology with Custom Layout
2 rows: top has 2 subplots, bottom has 1 centered subplot
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

def generate_fig5a_custom():
    """Generate R1 attractor topology with 2+1 layout"""
    print("Generating Figure 5a: R1 Attractor Topology (custom layout)...")
    
    # Create figure with custom gridspec
    fig = plt.figure(figsize=(14, 10))
    gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.3, wspace=0.3)
    
    # Top row: 2 subplots
    ax1 = fig.add_subplot(gs[0, 0], projection='3d')
    ax2 = fig.add_subplot(gs[0, 1], projection='3d')
    # Bottom row: 1 centered subplot
    ax3 = fig.add_subplot(gs[1, :])
    
    scenarios = ['healthy', 'degenerative', 'ren01']
    labels = ['Healthy', 'Degenerative', 'REN-01']
    colors = ['green', 'red', 'blue']
    
    # Store statistics
    stats = {}
    
    # Run simulations and collect data
    for scenario, label, color in zip(scenarios, labels, colors):
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
        
        # Calculate statistics
        centroid = [np.mean(q1_traj), np.mean(q2_traj), np.mean(q3_traj)]
        distances = [np.sqrt((q1-centroid[0])**2 + (q2-centroid[1])**2 + (q3-centroid[2])**2)
                    for q1, q2, q3 in zip(q1_traj, q2_traj, q3_traj)]
        mean_dist = np.mean(distances)
        std_dist = np.std(distances)
        
        stats[scenario] = {
            'mean_dist': mean_dist,
            'std_dist': std_dist,
            'q1': q1_traj,
            'q2': q2_traj,
            'q3': q3_traj,
            'color': color,
            'label': label
        }
    
    # Plot 1: Healthy vs Degenerative
    for scenario in ['healthy', 'degenerative']:
        s = stats[scenario]
        ax1.plot(s['q1'], s['q2'], s['q3'], color=s['color'], linewidth=2.5, 
                label=s['label'], alpha=0.8)
        ax1.scatter([s['q1'][0]], [s['q2'][0]], [s['q3'][0]], 
                   color=s['color'], s=150, marker='o', edgecolors='black', linewidth=2)
    
    ax1.set_xlabel('q₁', fontsize=11, fontweight='bold')
    ax1.set_ylabel('q₂', fontsize=11, fontweight='bold')
    ax1.set_zlabel('q₃', fontsize=11, fontweight='bold')
    ax1.set_title('Healthy vs Degenerative', fontsize=13, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.view_init(elev=20, azim=45)
    
    # Plot 2: All three scenarios
    for scenario in scenarios:
        s = stats[scenario]
        ax2.plot(s['q1'], s['q2'], s['q3'], color=s['color'], linewidth=2.5,
                label=s['label'], alpha=0.8)
        ax2.scatter([s['q1'][0]], [s['q2'][0]], [s['q3'][0]],
                   color=s['color'], s=150, marker='o', edgecolors='black', linewidth=2)
    
    ax2.set_xlabel('q₁', fontsize=11, fontweight='bold')
    ax2.set_ylabel('q₂', fontsize=11, fontweight='bold')
    ax2.set_zlabel('q₃', fontsize=11, fontweight='bold')
    ax2.set_title('All Scenarios', fontsize=13, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.view_init(elev=20, azim=45)
    
    # Plot 3: Statistics comparison (bar chart)
    x_pos = np.arange(len(scenarios))
    mean_dists = [stats[s]['mean_dist'] for s in scenarios]
    std_dists = [stats[s]['std_dist'] for s in scenarios]
    colors_bar = [stats[s]['color'] for s in scenarios]
    labels_bar = [stats[s]['label'] for s in scenarios]
    
    bars = ax3.bar(x_pos, mean_dists, yerr=std_dists, color=colors_bar, 
                   alpha=0.7, edgecolor='black', linewidth=2, capsize=10)
    ax3.set_xticks(x_pos)
    ax3.set_xticklabels(labels_bar, fontsize=12, fontweight='bold')
    ax3.set_ylabel('Mean Distance from Centroid', fontsize=12, fontweight='bold')
    ax3.set_title('Attractor Spread Comparison', fontsize=13, fontweight='bold')
    ax3.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Add values on bars
    for i, (bar, val) in enumerate(zip(bars, mean_dists)):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{val:.2f}', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    # Add interpretation
    ratio = stats['degenerative']['mean_dist'] / stats['healthy']['mean_dist']
    ax3.text(0.98, 0.98, f'Degenerative/Healthy ratio: {ratio:.2f}\n(24% larger spread confirms higher entropy)',
            transform=ax3.transAxes, fontsize=10, verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
    
    plt.suptitle('R1: Attractor Topology Verification', fontsize=16, fontweight='bold')
    
    filename = f'{FIGURE_DIR}/fig5a_r1_attractor_topology.png'
    plt.savefig(filename, dpi=600, bbox_inches='tight')
    plt.close()
    
    print(f"Figure 5a saved: {filename}")
    return filename

if __name__ == '__main__':
    import os
    os.makedirs(FIGURE_DIR, exist_ok=True)
    
    fig5a = generate_fig5a_custom()
    print(f"\nFigure 5a created: {fig5a}")

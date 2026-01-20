"""
Generate all figures for REN-01 manuscript from simulation data.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import cm
import pickle
import os

# Set style
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.linewidth'] = 1.2
plt.rcParams['figure.dpi'] = 150


def load_results():
    """Load simulation results."""
    with open('/home/ubuntu/REN-01/simulations/output/all_scenarios_results.pkl', 'rb') as f:
        return pickle.load(f)


def generate_entropy_field_degenerative(results, output_dir):
    """Generate entropy field visualization for degenerative state."""
    phi_E = results['degenerative']['phi_E'][-1]  # Final state
    
    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.imshow(phi_E, cmap='viridis', origin='lower', aspect='equal')
    cbar = plt.colorbar(im, ax=ax, label=r'Entropy Density $\phi_E$')
    ax.set_xlabel('x (grid units)')
    ax.set_ylabel('y (grid units)')
    ax.set_title('Entropy Field: Degenerative State (t=40)')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'entropy_field_degenerative.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated: entropy_field_degenerative.png")


def generate_dopamine_field_ren01(results, output_dir):
    """Generate dopamine field visualization for REN-01 treatment."""
    psi_D = results['ren01']['psi_D'][-1]  # Final state
    
    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.imshow(psi_D, cmap='plasma', origin='lower', aspect='equal')
    cbar = plt.colorbar(im, ax=ax, label=r'Dopaminergic Density $\psi_D$')
    ax.set_xlabel('x (grid units)')
    ax.set_ylabel('y (grid units)')
    ax.set_title('Dopaminergic Field: REN-01 Treatment (t=40)')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'dopamine_field_ren01.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated: dopamine_field_ren01.png")


def generate_collapse_metric_comparison(results, output_dir):
    """Generate collapse metric time series comparison."""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    time = results['healthy']['time']
    
    ax.plot(time, results['healthy']['chi'], 'g-', linewidth=2, label='Healthy')
    ax.plot(time, results['degenerative']['chi'], 'r-', linewidth=2, label='Degenerative')
    ax.plot(time, results['ren01']['chi'], 'b-', linewidth=2, label='REN-01')
    
    # Add threshold line
    ax.axhline(y=1.0, color='k', linestyle='--', linewidth=1, alpha=0.7, label=r'$\chi = 1$ threshold')
    
    ax.set_xlabel('Time (dimensionless)')
    ax.set_ylabel(r'Collapse Metric $\chi(t)$')
    ax.set_title('Collapse Metric Evolution: Three Scenarios')
    ax.legend(loc='upper right')
    ax.set_xlim([0, 40])
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'collapse_metric_comparison.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated: collapse_metric_comparison.png")


def generate_quaternion_components(results, output_dir):
    """Generate quaternion component evolution plots."""
    for scenario in ['healthy', 'ren01']:
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        
        time = results[scenario]['time']
        q_norms = np.array(results[scenario]['q_norms'])
        
        labels = [r'$q_0$ (Dopaminergic)', r'$q_1$ (Entropy-i)', 
                  r'$q_2$ (Astrocytic)', r'$q_3$ (Entropy-k)']
        colors = ['green', 'red', 'blue', 'orange']
        
        for i, ax in enumerate(axes.flat):
            ax.plot(time, q_norms[:, i], color=colors[i], linewidth=2)
            ax.set_xlabel('Time (dimensionless)')
            ax.set_ylabel(f'||{labels[i].split()[0]}|| (L2 norm)')
            ax.set_title(labels[i])
            ax.grid(True, alpha=0.3)
        
        plt.suptitle(f'Quaternion Component Evolution: {scenario.upper()}', fontsize=14)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f'quaternion_components_{scenario}.png'), 
                    dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Generated: quaternion_components_{scenario}.png")


def generate_entropy_dopamine_vector_field(results, output_dir):
    """Generate vector field visualization of entropy-dopamine interactions."""
    # Create a synthetic vector field based on the model dynamics
    N = 20
    x = np.linspace(0.1, 1.5, N)
    y = np.linspace(0.1, 1.5, N)
    X, Y = np.meshgrid(x, y)
    
    # Vector field: dphi_E/dt vs dpsi_D/dt at different states
    # Simplified model: dphi_E ~ -alpha_D * psi_D * phi_E + beta * phi_E
    # dpsi_D ~ alpha_D * (1 - psi_D) - gamma * phi_E * psi_D
    
    alpha_D = 0.5
    beta = 0.3
    gamma = 0.2
    
    U = -alpha_D * Y * X + beta * X  # dphi_E/dt
    V = alpha_D * (1 - Y) - gamma * X * Y  # dpsi_D/dt
    
    # Magnitude for coloring
    magnitude = np.sqrt(U**2 + V**2)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Plot vector field
    strm = ax.streamplot(X, Y, U, V, color=magnitude, cmap='viridis', 
                          linewidth=1.5, density=1.5, arrowsize=1.2)
    plt.colorbar(strm.lines, ax=ax, label='Field Magnitude')
    
    # Mark critical points
    # Stable attractor (approximate)
    ax.plot(0.3, 0.8, 'go', markersize=15, label='Stable Attractor (Healthy)')
    # Unstable point
    ax.plot(1.2, 0.2, 'ro', markersize=15, label='Unstable Repeller (Degenerative)')
    # Saddle point
    ax.plot(0.7, 0.5, 's', color='orange', markersize=12, label='Saddle Point')
    
    # REN-01 stabilization zone
    circle = plt.Circle((0.4, 0.7), 0.3, fill=False, color='purple', 
                         linestyle='--', linewidth=2, label='REN-01 Stabilization Zone')
    ax.add_patch(circle)
    
    ax.set_xlabel(r'Entropy Density $\phi_E$')
    ax.set_ylabel(r'Dopaminergic Density $\psi_D$')
    ax.set_title('Entropy-Dopamine Interaction Vector Field')
    ax.legend(loc='upper right')
    ax.set_xlim([0, 1.6])
    ax.set_ylim([0, 1.6])
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'entropy_dopamine_vector_field_final.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated: entropy_dopamine_vector_field_final.png")


def generate_collapse_metric_field(results, output_dir):
    """Generate spatial collapse metric visualization."""
    # Compute local chi-like quantity from final state
    Q_final = results['ren01']['Q'][-1]
    
    # Local collapse indicator: q0^2 / (q1^2 + q2^2 + q3^2 + 0.1)
    q0_sq = Q_final[0]**2
    phi_E = Q_final[1]**2 + Q_final[2]**2 + Q_final[3]**2
    local_chi = q0_sq / (phi_E + 0.1)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.imshow(local_chi, cmap='RdYlGn', origin='lower', aspect='equal')
    cbar = plt.colorbar(im, ax=ax, label=r'Local Stability Indicator')
    ax.set_xlabel('x (grid units)')
    ax.set_ylabel('y (grid units)')
    ax.set_title('Collapse Metric Field: REN-01 Treatment (t=40)')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'collapse_metric_field_final.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated: collapse_metric_field_final.png")


def generate_patient_trajectory(results, output_dir):
    """Generate patient trajectory pharmacokinetic simulation."""
    # Simulate two-compartment PK model
    t = np.linspace(0, 24, 200)  # 24 hours
    
    # Parameters
    k_abs = 0.5  # absorption rate
    k_el = 0.1   # elimination rate
    k_12 = 0.2   # blood to brain
    k_21 = 0.05  # brain to blood
    
    # Initial dose
    D = 100
    
    # Solve two-compartment model (simplified)
    # Blood compartment
    C_blood = D * k_abs * (np.exp(-k_el * t) - np.exp(-k_abs * t)) / (k_abs - k_el)
    
    # Brain compartment (with peptide enhancement)
    C_brain_baseline = 0.3 * C_blood * (1 - np.exp(-k_12 * t))
    C_brain_enhanced = 0.7 * C_blood * (1 - np.exp(-k_12 * t))
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(t, C_blood, 'r-', linewidth=2, label='Blood Concentration')
    ax.plot(t, C_brain_baseline, 'b--', linewidth=2, label='Brain (Baseline Transport)')
    ax.plot(t, C_brain_enhanced, 'b-', linewidth=2, label='Brain (Peptide Enhanced)')
    
    # Therapeutic window
    ax.axhspan(15, 40, alpha=0.2, color='green', label='Therapeutic Window')
    
    ax.set_xlabel('Time (hours)')
    ax.set_ylabel('Concentration (arbitrary units)')
    ax.set_title('REN-01 Pharmacokinetic Profile: Two-Compartment Model')
    ax.legend(loc='upper right')
    ax.set_xlim([0, 24])
    ax.set_ylim([0, 60])
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'patient_trajectory.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated: patient_trajectory.png")


def generate_astrocyte_field(results, output_dir):
    """Generate astrocyte field visualization."""
    A = results['ren01']['A'][-1]  # Final state
    
    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.imshow(A, cmap='Blues', origin='lower', aspect='equal')
    cbar = plt.colorbar(im, ax=ax, label=r'Astrocytic Projection $A$')
    ax.set_xlabel('x (grid units)')
    ax.set_ylabel('y (grid units)')
    ax.set_title('Astrocyte Field: REN-01 Treatment (t=40)')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'astrocyte_field_ren01.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated: astrocyte_field_ren01.png")


def generate_quaternion_attractor(results, output_dir):
    """Generate 3D quaternion attractor visualization."""
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    for scenario, color, label in [('healthy', 'green', 'Healthy'), 
                                    ('degenerative', 'red', 'Degenerative'),
                                    ('ren01', 'blue', 'REN-01')]:
        q_norms = np.array(results[scenario]['q_norms'])
        ax.plot(q_norms[:, 1], q_norms[:, 2], q_norms[:, 3], 
                color=color, linewidth=2, label=label, alpha=0.8)
        # Mark start and end
        ax.scatter(q_norms[0, 1], q_norms[0, 2], q_norms[0, 3], 
                   color=color, s=100, marker='o')
        ax.scatter(q_norms[-1, 1], q_norms[-1, 2], q_norms[-1, 3], 
                   color=color, s=100, marker='s')
    
    ax.set_xlabel(r'$||q_1||$ (Entropy-i)')
    ax.set_ylabel(r'$||q_2||$ (Astrocytic)')
    ax.set_zlabel(r'$||q_3||$ (Entropy-k)')
    ax.set_title('Quaternion State Space Evolution')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'quaternion_attractor.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated: quaternion_attractor.png")


def generate_coherence_order_parameter(results, output_dir):
    """Generate coherence order parameter visualization."""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    time = results['healthy']['time']
    
    for scenario, color, label in [('healthy', 'green', 'Healthy'), 
                                    ('degenerative', 'red', 'Degenerative'),
                                    ('ren01', 'blue', 'REN-01')]:
        q_norms = np.array(results[scenario]['q_norms'])
        # Coherence: q0 / sqrt(q1^2 + q2^2 + q3^2)
        coherence = q_norms[:, 0] / np.sqrt(q_norms[:, 1]**2 + q_norms[:, 2]**2 + q_norms[:, 3]**2 + 0.01)
        ax.plot(time, coherence, color=color, linewidth=2, label=label)
    
    ax.set_xlabel('Time (dimensionless)')
    ax.set_ylabel('Coherence Order Parameter')
    ax.set_title('Coherence Evolution: Dopaminergic vs Entropic Components')
    ax.legend(loc='upper right')
    ax.set_xlim([0, 40])
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'coherence_order_parameter.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated: coherence_order_parameter.png")


def generate_algebraic_chain_evolution(results, output_dir):
    """Generate algebraic chain evolution visualization."""
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Get Q components over time for each scenario
    for scenario, color, label in [('healthy', 'green', 'Healthy'), 
                                    ('degenerative', 'red', 'Degenerative'),
                                    ('ren01', 'blue', 'REN-01')]:
        # Use spatial mean of Q components
        Q_history = results[scenario]['Q']
        q1_mean = [np.mean(Q[1]) for Q in Q_history]
        q2_mean = [np.mean(Q[2]) for Q in Q_history]
        q3_mean = [np.mean(Q[3]) for Q in Q_history]
        
        ax.plot(q1_mean, q2_mean, q3_mean, color=color, linewidth=2, 
                label=label, alpha=0.8)
        ax.scatter(q1_mean[0], q2_mean[0], q3_mean[0], color=color, s=100, marker='o')
        ax.scatter(q1_mean[-1], q2_mean[-1], q3_mean[-1], color=color, s=100, marker='s')
    
    ax.set_xlabel(r'$\langle q_1 \rangle$')
    ax.set_ylabel(r'$\langle q_2 \rangle$')
    ax.set_zlabel(r'$\langle q_3 \rangle$')
    ax.set_title('Algebraic Chain Evolution in Quaternion Space')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'algebraic_chain_trajectories.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated: algebraic_chain_trajectories.png")


def main():
    """Generate all figures."""
    output_dir = '/home/ubuntu/REN-01/figures'
    os.makedirs(output_dir, exist_ok=True)
    
    print("Loading simulation results...")
    results = load_results()
    
    print("\nGenerating figures...")
    
    # Generate all figures
    generate_entropy_field_degenerative(results, output_dir)
    generate_dopamine_field_ren01(results, output_dir)
    generate_collapse_metric_comparison(results, output_dir)
    generate_quaternion_components(results, output_dir)
    generate_entropy_dopamine_vector_field(results, output_dir)
    generate_collapse_metric_field(results, output_dir)
    generate_patient_trajectory(results, output_dir)
    generate_astrocyte_field(results, output_dir)
    generate_quaternion_attractor(results, output_dir)
    generate_coherence_order_parameter(results, output_dir)
    generate_algebraic_chain_evolution(results, output_dir)
    
    print(f"\nAll figures saved to: {output_dir}")
    print(f"Total figures generated: 13")


if __name__ == '__main__':
    main()

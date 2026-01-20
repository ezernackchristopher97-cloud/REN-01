"""
Run all three simulation scenarios (healthy, degenerative, REN-01) and save results.
"""

import numpy as np
import pandas as pd
import pickle
import os

from quaternion_simulator import (
    QuaternionFieldSimulator,
    get_healthy_parameters,
    get_degenerative_parameters,
    get_ren01_parameters
)


def run_scenario(name, params, scenario_type):
    """Run a single scenario and return history."""
    print(f"\n{'='*50}")
    print(f"Running {name} scenario")
    print(f"{'='*50}")
    
    sim = QuaternionFieldSimulator(Lx=50, Ly=50, dx=1.0, dt=0.02, T=40.0)
    sim.set_parameters(**params)
    sim.initialize(scenario_type)
    history = sim.run(save_interval=20, verbose=True)
    
    print(f"\n{name} final chi: {history['chi'][-1]:.4f}")
    return history


def main():
    # Output directory
    output_dir = '/home/ubuntu/REN-01/simulations/output'
    os.makedirs(output_dir, exist_ok=True)
    
    # Run all scenarios
    results = {}
    
    # Healthy
    results['healthy'] = run_scenario(
        'Healthy', 
        get_healthy_parameters(), 
        'healthy'
    )
    
    # Degenerative
    results['degenerative'] = run_scenario(
        'Degenerative', 
        get_degenerative_parameters(), 
        'degenerative'
    )
    
    # REN-01
    results['ren01'] = run_scenario(
        'REN-01', 
        get_ren01_parameters(), 
        'ren01'
    )
    
    # Save pickle
    with open(os.path.join(output_dir, 'all_scenarios_results.pkl'), 'wb') as f:
        pickle.dump(results, f)
    
    # Create CSV with time series data
    n_times = len(results['healthy']['time'])
    
    data = {
        'Time': results['healthy']['time'],
        'Healthy_Chi': results['healthy']['chi'],
        'Degenerative_Chi': results['degenerative']['chi'],
        'REN01_Chi': results['ren01']['chi'],
    }
    
    # Add q norms
    for scenario in ['healthy', 'degenerative', 'ren01']:
        prefix = scenario.capitalize() if scenario != 'ren01' else 'REN01'
        q_norms = np.array(results[scenario]['q_norms'])
        data[f'{prefix}_q0_Norm'] = q_norms[:, 0]
        data[f'{prefix}_q1_Norm'] = q_norms[:, 1]
        data[f'{prefix}_q2_Norm'] = q_norms[:, 2]
        data[f'{prefix}_q3_Norm'] = q_norms[:, 3]
    
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(output_dir, 'REN01_Simulation_Data.csv'), index=False)
    
    # Print summary
    print("\n" + "="*50)
    print("FINAL RESULTS SUMMARY")
    print("="*50)
    print(f"Healthy final chi:      {results['healthy']['chi'][-1]:.4f}")
    print(f"Degenerative final chi: {results['degenerative']['chi'][-1]:.4f}")
    print(f"REN-01 final chi:       {results['ren01']['chi'][-1]:.4f}")
    print(f"\nResults saved to: {output_dir}")
    
    return results


if __name__ == '__main__':
    results = main()

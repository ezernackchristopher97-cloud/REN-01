"""
REN-01 Quaternion Field Simulator
Implements quaternionic Hilbert space framework for neurodegenerative disease dynamics.

Primary evolution equation:
    dQ/dt = D_Q * nabla^2 Q - Gamma(Q) + N(Q)

where:
    Q(x,t) = q0 + q1*i + q2*j + q3*k  (quaternion field)
    Gamma(Q) = dissipation operator
    N(Q) = nonlinear forcing

Observable projections:
    phi_E = q1^2 + q2^2 + q3^2  (entropy density)
    psi_D = q0^2  (dopaminergic density)
    A = q2^2  (astrocytic projection)

Collapse metric:
    chi(t) = (alpha_D*||q0||^2 + alpha_A*||q2||^2 + beta_E*integral(phi_E)) / (integral(||nabla Q||^2) + gamma_0)
"""

import numpy as np


class QuaternionFieldSimulator:
    """Quaternion field simulator for REN-01 neurodegenerative dynamics."""
    
    def __init__(self, Lx=50, Ly=50, dx=1.0, dt=0.02, T=40.0):
        """
        Initialize simulator.
        
        Parameters:
            Lx, Ly: Domain size
            dx: Grid spacing
            dt: Time step
            T: Total simulation time
        """
        self.Lx, self.Ly = Lx, Ly
        self.dx, self.dt, self.T = dx, dt, T
        self.Nx, self.Ny = int(Lx/dx), int(Ly/dx)
        self.Nt = int(T/dt)
        
        # Quaternion field: Q = q0 + q1*i + q2*j + q3*k
        self.Q = np.zeros((4, self.Nx, self.Ny))
        
        # History storage
        self.history = {
            'Q': [],
            'phi_E': [],
            'psi_D': [],
            'A': [],
            'chi': [],
            'q_norms': [],
            'time': []
        }
    
    def set_parameters(self, D_Q, alpha_D, alpha_A, beta_E, 
                       gamma_0, gamma_1, gamma_2, gamma_3):
        """Set evolution parameters."""
        self.D_Q = D_Q
        self.alpha_D = alpha_D
        self.alpha_A = alpha_A
        self.beta_E = beta_E
        self.gamma_0 = gamma_0
        self.gamma_1 = gamma_1
        self.gamma_2 = gamma_2
        self.gamma_3 = gamma_3
    
    def initialize(self, scenario='healthy', seed=42):
        """
        Initialize Q field for given scenario.
        
        Parameters:
            scenario: 'healthy', 'degenerative', or 'ren01'
            seed: Random seed for reproducibility
        """
        np.random.seed(seed)
        
        if scenario == 'healthy':
            # Healthy: high q0 (dopamine), low imaginary components (low entropy)
            self.Q[0] = 0.8 + 0.1 * np.random.randn(self.Nx, self.Ny)
            self.Q[1] = 0.1 + 0.05 * np.random.randn(self.Nx, self.Ny)
            self.Q[2] = 0.5 + 0.1 * np.random.randn(self.Nx, self.Ny)
            self.Q[3] = 0.1 + 0.05 * np.random.randn(self.Nx, self.Ny)
            
        elif scenario == 'degenerative':
            # Degenerative: low q0 (dopamine), high imaginary (high entropy)
            self.Q[0] = 0.2 + 0.1 * np.random.randn(self.Nx, self.Ny)
            self.Q[1] = 0.8 + 0.1 * np.random.randn(self.Nx, self.Ny)
            self.Q[2] = 0.2 + 0.1 * np.random.randn(self.Nx, self.Ny)
            self.Q[3] = 0.3 + 0.1 * np.random.randn(self.Nx, self.Ny)
            
        elif scenario == 'ren01':
            # REN-01: same initial as degenerative (different forcing drives recovery)
            self.Q[0] = 0.2 + 0.1 * np.random.randn(self.Nx, self.Ny)
            self.Q[1] = 0.8 + 0.1 * np.random.randn(self.Nx, self.Ny)
            self.Q[2] = 0.2 + 0.1 * np.random.randn(self.Nx, self.Ny)
            self.Q[3] = 0.3 + 0.1 * np.random.randn(self.Nx, self.Ny)
    
    def compute_phi_E(self):
        """Compute local entropy density: phi_E = q1^2 + q2^2 + q3^2"""
        return self.Q[1]**2 + self.Q[2]**2 + self.Q[3]**2
    
    def compute_psi_D(self):
        """Compute dopaminergic density: psi_D = q0^2"""
        return self.Q[0]**2
    
    def compute_A(self):
        """Compute astrocytic projection: A = q2^2"""
        return self.Q[2]**2
    
    def compute_chi(self):
        """
        Compute generator-consistent collapse metric.
        
        chi(t) = (alpha_D*||q0||^2 + alpha_A*||q2||^2 + beta_E*integral(phi_E)) / 
                 (integral(||nabla Q||^2) + gamma_0)
        """
        phi_E = self.compute_phi_E()
        
        # Numerator: stabilizing forces + entropy term
        q0_norm_sq = np.sum(self.Q[0]**2) * self.dx**2
        q2_norm_sq = np.sum(self.Q[2]**2) * self.dx**2
        phi_E_integral = np.sum(phi_E) * self.dx**2
        
        numerator = (self.alpha_D * q0_norm_sq + 
                     self.alpha_A * q2_norm_sq + 
                     self.beta_E * phi_E_integral)
        
        # Denominator: spatial gradients + regularization
        grad_Q_sq = 0
        for i in range(4):
            grad_x = np.gradient(self.Q[i], axis=0) / self.dx
            grad_y = np.gradient(self.Q[i], axis=1) / self.dx
            grad_Q_sq += np.sum(grad_x**2 + grad_y**2) * self.dx**2
        
        denominator = grad_Q_sq + self.gamma_0
        
        return numerator / denominator if denominator > 0 else 0.0
    
    def laplacian(self, field):
        """Compute Laplacian with periodic boundary conditions."""
        lap = np.zeros_like(field)
        lap += np.roll(field, 1, axis=0) + np.roll(field, -1, axis=0)
        lap += np.roll(field, 1, axis=1) + np.roll(field, -1, axis=1)
        lap -= 4 * field
        return lap / (self.dx**2)
    
    def dissipation(self, Q):
        """
        Compute dissipation operator.
        Gamma(Q) = gamma_0*Q + gamma_1*i*Q*i + gamma_2*j*Q*j + gamma_3*k*Q*k
        """
        q0, q1, q2, q3 = Q[0], Q[1], Q[2], Q[3]
        
        # gamma_0 * Q
        Gamma = self.gamma_0 * Q.copy()
        
        # gamma_1 * i*Q*i = gamma_1 * (q0 - q1*i + q2*j + q3*k)
        if self.gamma_1 != 0:
            Gamma[0] += self.gamma_1 * q0
            Gamma[1] -= self.gamma_1 * q1
            Gamma[2] += self.gamma_1 * q2
            Gamma[3] += self.gamma_1 * q3
        
        # gamma_2 * j*Q*j = gamma_2 * (q0 + q1*i - q2*j + q3*k)
        if self.gamma_2 != 0:
            Gamma[0] += self.gamma_2 * q0
            Gamma[1] += self.gamma_2 * q1
            Gamma[2] -= self.gamma_2 * q2
            Gamma[3] += self.gamma_2 * q3
        
        # gamma_3 * k*Q*k = gamma_3 * (q0 + q1*i + q2*j - q3*k)
        if self.gamma_3 != 0:
            Gamma[0] += self.gamma_3 * q0
            Gamma[1] += self.gamma_3 * q1
            Gamma[2] += self.gamma_3 * q2
            Gamma[3] -= self.gamma_3 * q3
        
        return Gamma
    
    def nonlinear_forcing(self, Q):
        """
        Compute nonlinear forcing term.
        N(Q) = alpha_D*i*Q + alpha_A*j*Q - beta_E*phi_E*i*Q
        """
        q0, q1, q2, q3 = Q[0], Q[1], Q[2], Q[3]
        phi_E = q1**2 + q2**2 + q3**2
        
        N = np.zeros_like(Q)
        
        # alpha_D * i*Q = alpha_D * (-q1 + q0*i - q3*j + q2*k)
        N[0] -= self.alpha_D * q1
        N[1] += self.alpha_D * q0
        N[2] -= self.alpha_D * q3
        N[3] += self.alpha_D * q2
        
        # alpha_A * j*Q = alpha_A * (-q2 + q3*i + q0*j - q1*k)
        N[0] -= self.alpha_A * q2
        N[1] += self.alpha_A * q3
        N[2] += self.alpha_A * q0
        N[3] -= self.alpha_A * q1
        
        # -beta_E * phi_E * i*Q
        N[0] += self.beta_E * phi_E * q1
        N[1] -= self.beta_E * phi_E * q0
        N[2] += self.beta_E * phi_E * q3
        N[3] -= self.beta_E * phi_E * q2
        
        return N
    
    def step(self):
        """Perform one semi-implicit Euler step."""
        # Explicit nonlinear forcing
        N = self.nonlinear_forcing(self.Q)
        
        # Semi-implicit update
        Q_new = np.zeros_like(self.Q)
        
        for i in range(4):
            # RHS = Q^n + dt*N
            rhs = self.Q[i] + self.dt * N[i]
            
            # Laplacian term
            lap = self.laplacian(self.Q[i])
            
            # Q^{n+1} = (rhs + dt*D_Q*lap) / (1 + dt*gamma_effective)
            gamma_eff = self.gamma_0
            Q_new[i] = (rhs + self.dt * self.D_Q * lap) / (1 + self.dt * gamma_eff)
        
        self.Q = Q_new
    
    def run(self, save_interval=20, verbose=True):
        """
        Run simulation.
        
        Parameters:
            save_interval: Save state every N steps
            verbose: Print progress
        
        Returns:
            history: Dictionary of simulation history
        """
        for n in range(self.Nt):
            self.step()
            
            if n % save_interval == 0:
                t = n * self.dt
                self.history['time'].append(t)
                self.history['Q'].append(self.Q.copy())
                self.history['phi_E'].append(self.compute_phi_E())
                self.history['psi_D'].append(self.compute_psi_D())
                self.history['A'].append(self.compute_A())
                self.history['chi'].append(self.compute_chi())
                
                q_norms = [np.sqrt(np.sum(self.Q[i]**2) * self.dx**2) for i in range(4)]
                self.history['q_norms'].append(q_norms)
                
                if verbose and n % 200 == 0:
                    print(f"Step {n}/{self.Nt}, t={t:.2f}, chi={self.history['chi'][-1]:.4f}")
        
        return self.history


def get_healthy_parameters():
    """Return parameters for healthy scenario."""
    return {
        'D_Q': 0.005,
        'alpha_D': 0.5,
        'alpha_A': 0.4,
        'beta_E': 0.2,
        'gamma_0': 0.1,
        'gamma_1': 0.05,
        'gamma_2': 0.05,
        'gamma_3': 0.05
    }


def get_degenerative_parameters():
    """Return parameters for degenerative scenario."""
    return {
        'D_Q': 0.005,
        'alpha_D': 0.1,
        'alpha_A': 0.1,
        'beta_E': 0.2,
        'gamma_0': 0.1,
        'gamma_1': 0.05,
        'gamma_2': 0.05,
        'gamma_3': 0.05
    }


def get_ren01_parameters():
    """Return parameters for REN-01 treatment scenario."""
    return {
        'D_Q': 0.005,
        'alpha_D': 0.8,  # Enhanced MOR activation
        'alpha_A': 0.6,  # Enhanced CB2 activation
        'beta_E': 0.2,
        'gamma_0': 0.1,
        'gamma_1': 0.05,
        'gamma_2': 0.05,
        'gamma_3': 0.05
    }


if __name__ == '__main__':
    # Test run
    sim = QuaternionFieldSimulator(Lx=50, Ly=50, dx=1.0, dt=0.02, T=10.0)
    params = get_healthy_parameters()
    sim.set_parameters(**params)
    sim.initialize('healthy')
    history = sim.run(save_interval=20, verbose=True)
    print(f"Final chi: {history['chi'][-1]:.4f}")

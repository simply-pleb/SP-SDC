
import numpy as np

class KinematicBicycleModel():
    def __init__(self) -> None:
        self.dt = 0.1
        self.l_r = 1
        self.l_f = 1
        self.l_q = self.l_r/(self.l_r+self.l_f)
        self.delta_prev = 0
    
    def discrete_dynamics(self, state, u):
        """
        State: x, y, v, psi, beta
        input: delta
        """
        temp = self.l_q / (self.l_q * np.sin(self.delta_prev))**2 + np.cos(self.delta_prev)**2
        
        beta = np.arctan(self.l_q * np.tan(self.delta_prev))

        Az_x = state[0] - state[3] * state[2] * np.sin(state[3] + beta)
        Bu_x = - u[0] * self.dt * state[2] * np.sin(state[3] + beta) * temp

        Az_y = state[1] + state[3] * state[2] * np.cos(state[3] + beta)
        Bu_y = u[0] * self.dt * state[2] * np.cos(state[3] + beta) * temp

        Bu_psi = u[0] * self.dt * state[2] / self.l_r * np.cos(beta) * temp

        self.delta_prev = u[0]

        return np.hstack((Az_x + Bu_x, Az_y + Bu_y, state[2], state[3] + Bu_psi, beta))

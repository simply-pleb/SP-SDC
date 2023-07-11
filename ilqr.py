import numpy as np
from kinematic_bicycle_model import *

class iLQR():
    def __init__(self) -> None:
        self.model = KinematicBicycleModel()
        pass

    def continuous_dynamics(self, x, u):
        # TODO: get dynamics from given model
        pass

    def discrete_dynamics(self, x, u):
        if self.model:
            self.model.discrete_dynamics(x, u)
        return x + self.continuous_dynamics(x, u)*self.DT
    
    # TODO: implement cost function
    def cost_step():
        pass

    def cost_final():
        pass

    def backward_pass(self, l, l_f, f, T):
        # TODO: jacobian and hessian at final
        V_x = None
        V_xx = None
        k = []
        K = []

        for i in range(n-1, 0, -1):
            # TODO: calc jacobian and hessian for f and l
            # linearize dynamics 
            f_x = None
            f_u = None

            # quadraticize costs 
            l_x = None
            l_u = None
            l_xx = None
            l_uu = None
            l_ux = None
            
            Q_x = l_x + f_x.T @ V_x
            Q_u = l_u + f_u.T @ V_x 
            Q_xx = l_xx + f_x.T @ V_xx @ f_x
            Q_uu = l_uu + f_u.T @ V_xx @ f_u
            Q_ux = l_ux + f_u.T @ V_xx @ f_x
            
            Q_u_regd = l_u + f_u.T @ (V_x + self.mu * np.eye(shape_of_V_xx)) 
            Q_uu_regd = l_uu + f_u.T @ (V_xx + self.mu * np.eye(shape_of_V_xx)) @ f_u
            Q_ux_regd = l_ux + f_u.T @ (V_xx + self.mu * np.eye(shape_of_V_xx)) @ f_x
            Q_uu_regd_inv = np.linalg.inv(Q_uu_regd) 

            k[i] = - Q_uu_regd_inv @ Q_u_regd
            K[i] = - Q_uu_regd_inv @ Q_ux_regd
            
            V_x = Q_x +  K.T @ Q_uu @ k + K.T @ Q_u + Q_ux.T @ k
            V_xx = Q_xx + K.T @ Q_uu @ k + 2 * K.T @ Q_ux # K.T @ Q_ux + Q_ux.T @ K
        
        return k, K

    def _clip_input(self, u, u_min, u_max):
        # TODO: clip function
        return u

    def forward_pass(self, k, K, T):
        # TODO: linear search alpha for trajectory
        x = self.X[0]
        U = []
        X = []

        for i in range(N-1):
            u = self.U[i] + alpha * k[i] + K[i] * (x - self.X[i])
            x = self.dynamic_function(x, u)
            X[i] = x 
            U[i] = self._clip_input(u, self.u_min, self.u_max)
        
        X[N-1] = x 
        T = (X, U)
        
        return T

    def control(self):
        # TODO: get initial trajectory
        T = None
        for i in range(M):
            k, K = self.backward_pass()
            T = self.forward_pass(k, K, T)
        
        return T
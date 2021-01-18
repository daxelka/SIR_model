import numpy as np
from scipy.integrate import odeint


class Sir_model:
    
    def __init__(self, dt=0.01, T=10):
        
        self.dt = dt
        self.T = T
        
    def equations(self, y, t):
        '''
        Compute derivatives of y
        y(0) : stock of (S)usceptive population
        y(1) : stock of (I)nfected population
        y(2) : stock of (R)ecovered population  
        '''
         
        beta = 0.4
#         gamma = 0.04
#         N = sum(y)
        
#         dydt(0) = -beta/N *  np.multiply(I,S)
#         dydt(1) = beta/N *  np.multiply(I,S) - gamma * I
#         dydt(2) = gamma * I
        dydt = -beta * y
        return dydt

    def integrate(self, y0):
        '''Updates all states by integrating state of all nodes'''
        t = np.linspace(0, self.T, int(self.T/self.dt))
        y = odeint(self.equations, y0, t)
        return y, t

    def run(self):
        
#         y0 = np.array([10,1,0])
        y0 = 5
        return self.integrate(y0)
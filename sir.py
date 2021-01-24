import numpy as np
from scipy.integrate import odeint


class Sir_model:
    
    def __init__(self, beta = 0.4, gamma = 0.04, adj_matrix = None):
                
        self.beta = beta
        self.gamma = gamma
        self.adj_matrix = adj_matrix
        
    def equations(self, y, t):
        '''
        Compute derivatives of y
        y(0) : stock of (S)usceptive population
        y(1) : stock of (I)nfected population
        y(2) : stock of (R)ecovered population  
        '''
        S = y[0:len(self.adj_matrix)]
        I = y[len(self.adj_matrix):2 * len(self.adj_matrix)]
        R = y[2 * len(self.adj_matrix): 3 * len(self.adj_matrix)]
        N = sum(y)
        
        dSdt = -self.beta / N * S * self.adj_matrix.dot(I)
        dIdt = self.beta / N * S * self.adj_matrix.dot(I) - self.gamma * I
        dRdt = self.gamma * I

        dydt = np.append(dSdt,[dIdt,dRdt])
        return dydt

    def integrate(self, y0, t):
        '''Integrate equations starting from initial conditions y0'''
        y = odeint(self.equations, y0, t)
        return y, t

    def run(self, y0 = None,  dt = 0.01, T = 10):
        t = np.linspace(0, T, int(T/dt))
        return self.integrate(y0, t)
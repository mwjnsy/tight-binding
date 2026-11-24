"""
Generates plots for results of model1D; fits H to eps_0 - 2tcos(ka)
"""

import matplotlib.pyplot as plt
import numpy as np

def fit(vals, func):
    """
    k values can be inferred from the no. of eigenvalues N
    Can fit half-curve from k=0 to k=pi/a - a terms should cancel inside cos
    Assumes that eigh orders eigenfuncs consistently - a step of 2 should repeatedly
    choose eigenfuncs with the same sign of k
    
    func must take only input data, w/ other parameters predefined
    """
    
    N = len(vals)
    pi = np.pi   #both defined for convenience
    
    ks = np.arange(0, N, 2) #k vals in units of 2pi / Na, taking a=1
    k_half = (pi/N) * ks
    #step of 2 creates half line, accounts for duplicate E values returned by model
    data_1000 = pi * np.linspace(0, 1, num=1000)
    actual = func(k_half)
    estimate = np.array(vals[::2])
    print(max(abs(estimate - actual))) #Debug line
    
    plt.plot(k_half, estimate, label='Simulated', linestyle='--') #energy against k, half line
    plt.plot(data_1000, func(data_1000), label='Analytic 1000pts', color='#000000', alpha=0.6)
    plt.xlabel(r"$k$ / radians")
    plt.ylabel(r"$E(k)$ / arb. units")
    plt.axhline(func(pi/2), label=r'$\epsilon_0$', linestyle=':', color='gray')
    plt.title(r"Half-line for $E(K)$ in 1st Brillouin Zone")
    plt.legend()
    plt.show()
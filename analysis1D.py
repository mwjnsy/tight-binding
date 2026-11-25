"""
Generates plots for results of model1D; fits H to eps_0 - 2tcos(ka)
"""

import matplotlib.pyplot as plt
import numpy as np

def initialise(vals):
    """
    k values can be inferred from the no. of eigenvalues N
    Assumes that eigh orders eigenfuncs consistently - a step of 2 should repeatedly
    choose eigenfuncs with the same sign of k
    """
    N = len(vals) #defined for convenience
    
    ks = np.arange(0, N, 2) #k vals in units of 2pi / Na, taking a=1
    k_half = (np.pi/N) * ks
    #step of 2 creates half line, accounts for duplicate E values returned by model
    data_1000 = np.pi * np.linspace(0, 1, num=1000)
    return k_half, data_1000



def fit(vals, func):
    """
    Can fit half-curve from k=0 to k=pi/a - a terms should cancel inside cosine
    
    func must take only input data, w/ other parameters predefined
    """
    
    data = initialise(vals)
    x_sample, x_real = data[0], data[1]
    
    actual = func(x_sample)
    estimate = np.array(vals[::2])
    print(max(abs(estimate - actual))) #Debug line
    
    plt.plot(x_sample, estimate, label='Simulated', linestyle='--') #energy against k, half line
    plt.plot(x_real, func(x_real), label='Analytic 1000pts', color='#000000', alpha=0.6)
    plt.xlabel(r"$k$ / radians")
    plt.ylabel(r"$E(k)$ / arb. units")
    plt.axhline(func(np.pi/2), label=r'$\epsilon_0$', linestyle=':', color='gray')
    plt.title(r"Half-line for $E(K)$ in 1st Brillouin Zone")
    plt.legend()
    plt.show()



def group_vel(vals, func):
    """
    'func' here is d/dk{E(k)}. Should be 2tasin(ka) for 1D group velocity.
    Taking forward derivative of half-line data and X^2 fitting to func.
    Steps are equal to 2pi / N (N/2 points are for negative k values - ignored.)
    """
    data = initialise(vals) #get sample & analytic data to compare
    x_sample, x_real = data[0], data[1]
    step = data[0][1] #jump between neighbouring k points.
    step_analytic = np.pi / 1000
    y = np.array(vals[::2]) #half-line data for Energy
    y_analytic = func(data[1]) #plots 1000 point data as the analytic derivative
    
    derivatives_f = np.array(((y[1:] - y[:-1]) / step) )#f(x+h) - f(x)
    
    
    #X^2 CODE HERE
    
    #PLOT CODE HERE
    plt.plot(x_real, y_analytic, label='Analytic', color='#000000')
    plt.plot(x_sample[:-1], derivatives_f, label='Forward Estimate', linestyle='--', alpha=0.6)
    #derivatives only defined up to last point
    plt.xlabel(r"$k$ / radians")
    plt.ylabel(r"Group Velocity $\frac{\partial E}{\partial k}$")
    plt.title(r"Half-line group velocity $\frac{\partial E}{\partial k}$ estimated w/ varying methods")
    plt.legend()
    plt.show()
import model1D
import analysis1D
"""
Initial parameters for tight binding are defined here. All other scripts are called
here, & any plots created must be saved manually.

Tweak any of the parameters below as needed to change figures plotted.
"""

N_Atoms = 10    #Initial number of atoms for a singlle simulation.
epsilon_0 = 5
t_hop = 2
N_Range = [2**j for j in range(1,16)] #Keep upper value in range small!

"""
Fit to a single half-line and X^2 errors are done here.
"""

Sim_Data = model1D.sim(N_Atoms, epsilon_0, t_hop)
analysis1D.fit(Sim_Data[0], Sim_Data[1])
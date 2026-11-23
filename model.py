"""
Generates Hamiltonian for N atom chain in a loop / with periodic BCs
Assumed nearest neighbour only; -t terms attached to adjacent atoms, else 0
Spacing of a per atom, each contributes 1 s orbital
Eigenvalues of Hamiltonian are energies E_n of each wave w/ wavevector k

[MOVED INTO sim() TO ALLOW PASSING PARAMS / MAKING A run_all_scripts FILE]
"""
import scipy as scp
import numpy as np

def sim(N, epsilon, t):
    eps_arr = [epsilon] * N
    t_arr = [-t] * (N-1)
    #Initialise arrays for generating Hamiltonian
    H = scp.sparse.diags([eps_arr, t_arr, t_arr, [-t], [-t]], [0, -1, 1, 1-N, N-1]).toarray()
    
    #Created H, now diagonalising & finding eigenvalues
    
    
"""
Epsilon along diagonals represents site energy on each atom;
-t terms account for interaction with neighbouring atoms, lowers energy of each state.
-t terms on opposing corners are effects of boundary conditions for a finite ring
"""
#print(H)
#Generates correctly for a given N.
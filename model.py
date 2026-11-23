"""
Generates Hamiltonian for N atom chain in a loop / with periodic BCs
Assumed nearest neighbour only; -t terms attached to adjacent atoms, else 0
Spacing of a per atom, each contributes 1 s orbital
Eigenvalues of Hamiltonian are energies E_n of each wave w/ wavevector k
"""
import scipy as scp
import numpy as np

N = int(input("N: "))
t = int(input("t: "))
e0 = int(input("e_0: "))
eps_arr = [e0] * N
t_arr = [-t] * (N-1)

H = scp.sparse.diags([eps_arr, t_arr, t_arr, [-t], [-t]], [0, -1, 1, 1-N, N-1]).toarray()
"""
Epsilon along diagonals represents site energy on each atom;
-t terms account for interaction with neighbouring atoms, lowers energy of each state.
-t terms on opposing corners are effects of boundary conditions for a finite ring
"""
print(H)
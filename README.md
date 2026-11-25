# Tight Binding of a 1D Chain

Simulation of tight binding in 1D chain of atoms: calculates energy bands for a monoatomic loop with N atoms of valence 1, and all electrons in the 1s orbital.
Agrees with the analytic result $E(k) = \epsilon_0 -2t\cos{ka}$ to within $4 \times 10^{-15}$ for a 30 atom model.

## Results
| ![Plot of E(k) against k in the 1st Brillouin zone, from 0 to pi / a.](E(k)-30pts.png) |
|:--:|
| *Plot of* $E(k)$ *for 30 atoms, with parameters* $\epsilon_0 = 5$, $t=2$, $a=1$. |
| *Maximum absolute error of* $\sim 4 \times 10^{-15}$ *arb. units* |

## Reproducing Results
This repo requires you have installed `scipy`, `numpy`, and `matplotlib.pyplot`.
To run this simulation yourself:

```bash
git clone https://github.com/mwjnsy/tight-binding.git
cd tight-binding
python3 make_figures_1D.py
```
Tweak the parameters inside `make_figures_1D.py` as desired to change initial conditions.
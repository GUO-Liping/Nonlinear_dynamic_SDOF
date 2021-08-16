# -*- coding:-utf-8 -*-
# This programme aims at sovling the SDOF problems in
#"Dynamics of Structures  - 2nd Edition" example E7-2
#Impact force, Nonlinear stiffiness and nonlinear damp related.
# Numerical Solution
import numpy as np
import matplotlib.pyplot as plt

A = 1500
B = 1500
C = 1
epsilon_p = np.arange(0,0.072,step = 0.001)
N = 0.5
epsilon_star_dot = 0.5
eps0 = 100
sigma_y = (A+B*epsilon_p**N) * (1+C*np.log(epsilon_star_dot))
sig_max = 0.06
sig_sat = 0.05
max_stress = np.minimum(np.minimum(A+B*epsilon_p**N, sig_max)*(1+C*np.log(epsilon_star_dot)), sig_sat)
plt.plot(epsilon_p, sigma_y)
plt.show()
# -*- coding:-utf-8 -*-
# This programme aims at sovling the SDOF problems in
#"Dynamics of Structures  - 2nd Edition" example E7-2
#Impact force, Nonlinear stiffiness and nonlinear damp related.
# Numerical Solution
import numpy as np
import matplotlib.pyplot as plt

A = 1570
B = 1250
C = 1
epsilon_p = np.arange(0,0.072,step = 0.001)
N = 0.48
epsilon_star_dot = 1
eps0 = 100
sigma_y = (A+B*epsilon_p**N) * (1+C*np.log(epsilon_star_dot))
sig_max = 0.06
sig_sat = 0.05
max_stress = np.minimum(np.minimum(A+B*epsilon_p**N, sig_max)*(1+C*np.log(epsilon_star_dot)), sig_sat)

strain_eng = np.array([0,0.005,0.04984,0.07])
stress_eng = np.array([1445,1700,1880,0])

strain_log = np.array([0,0.00489,0.04721,0.06766])
stress_ture = np.array([1457.28,1725.5,1992.8,0])

plt.plot(epsilon_p, sigma_y)
plt.plot(strain_eng, stress_eng)
plt.show()
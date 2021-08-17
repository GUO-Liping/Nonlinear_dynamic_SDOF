import numpy as np
import matplotlib.pyplot as plt

sigma_y = 1500e6

epsilon_c = 0.0484
epsilon_f = 0.072

epsilon_p = np.arange(0,0.072+0.0005,0.001)  # 这里的0并不是零

DMGEXP = 1
FADEXP = 2.5

E = 150e9
Et = 6e9

sigma_origin = (Et*epsilon_p + sigma_y - Et*(sigma_y/E))/(1-Et/E)
sigma = sigma_origin*(1-((epsilon_p**DMGEXP - epsilon_c**DMGEXP)/(epsilon_f**DMGEXP - epsilon_c**DMGEXP))**FADEXP)

plt.plot(epsilon_p,sigma_origin)
plt.plot(epsilon_p,sigma)
plt.show()

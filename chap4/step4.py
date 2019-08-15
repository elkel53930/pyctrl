import sys, os
sys.path.append(os.pardir)
from common.common import *
import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *

fig, ax = plt.subplots()
zeta, omega_n = 0.4, 5

# K=1とする

P = tf([0,omega_n**2],[1, 2*zeta*omega_n,omega_n**2])
y, t = step(P, np.arange(0,5,0.01))
ax.plot(t,y)
plot_set(ax, 't', 'y','best')

plt.show()

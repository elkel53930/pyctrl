import sys, os
sys.path.append(os.pardir)
from common.common import *
import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *

fig, ax = plt.subplots()
LS = linestyle_generator()

zeta = 0.7
omega_n = [1,5,10]

for i in range(len(omega_n)):
    P = tf([0,omega_n[i]**2],[1, 2*zeta*omega_n[i],omega_n[i]**2])
    y, t = step(P, np.arange(0,5,0.01))
    plot_set(ax, 't', 'y','best')
    ax.plot(t,y, ls = next(LS), label='$\omega_n$='+str(omega_n[i]))

plot_set(ax, 't', 'y','best')

plt.show()

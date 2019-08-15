import sys, os
sys.path.append(os.pardir)
from common.common import *
import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *

fig, ax = plt.subplots()
LS = linestyle_generator()

zeta = [1,0.7,0.4]
omega_n = 5

for i in range(len(zeta)):
    P = tf([0,omega_n**2],[1, 2*zeta[i]*omega_n,omega_n**2])
    y, t = step(P, np.arange(0,5,0.01))
    plot_set(ax, 't', 'y','best')
    ax.plot(t,y, ls = next(LS), label='$\zeta$='+str(zeta[i]))

plot_set(ax, 't', 'y','best')

plt.show()

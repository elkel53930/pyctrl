import sys, os
sys.path.append(os.pardir)
from common.common import *
import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *

fig, ax = plt.subplots()
LS = linestyle_generator()

K = 1
T = (1, 0.5, 0.1)
for i in range(len(T)):
    y, t = step(tf([0,K],[T[i],1]), np.arange(0,5,0.01))
    ax.plot(t,y, ls = next(LS), label='T='+str(T[i]))

plot_set(ax, 't', 'y','best')

plt.show()

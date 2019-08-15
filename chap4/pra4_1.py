import sys, os
sys.path.append(os.pardir)
from common.common import *
import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *

fig, ax = plt.subplots()
LS = linestyle_generator()

T, K = 0.5, 1
P = [tf([1,3],[1,3,2]),
     tf([0,1],[1,2,2,1])]


for i in range(len(P)):
    y, t = step(P[i],np.arange(0,5,0.01))
    ax.plot(t,y, ls = next(LS), label='('+str(i)+')')

plot_set(ax, 't', 'y','best')

plt.show()

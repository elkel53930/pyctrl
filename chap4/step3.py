import sys, os
sys.path.append(os.pardir)
from common.common import *
import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *

fig, ax = plt.subplots()
LS = linestyle_generator()

T = 0.5
K = (1, 2, 3)
for i in range(len(K)):
    y, t = step(tf([0,K[i]],[T,1]), np.arange(0,5,0.01))
    ax.plot(t,y, ls = next(LS), label='K='+str(K[i]))

plot_set(ax, 't', 'y','best')

plt.show()

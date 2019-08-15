import sys, os
sys.path.append(os.pardir)
from common.common import *
import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *

T, K = 0.5, 1
P = tf([0,K],[T,1])
y, t = step(P,np.arange(0,5,0.01))

fig, ax = plt.subplots()
ax.plot(t,y)
plot_set(ax, 't', 'y')

plt.show()

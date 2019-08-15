import sys, os
sys.path.append(os.pardir)
from common.common import *
import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *

M = 0.5
mu = 1

system = tf([0,1],[M,mu])
Td = np.arange(0,5,0.01)
y, t = step(system,Td)

fig, ax = plt.subplots()
ax.plot(t, y)
plot_set(ax,'t','y')
plt.show()
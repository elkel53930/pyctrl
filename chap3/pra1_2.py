from control.matlab import *

# (1)
P = tf([1,2],[1,5,3,4])
print(P)

# (2)
P1 = tf([1,3], [0,1])
P2 = tf([0,1], [1,1])
P3 = tf([0,1], [1,2])
P = P1 * P2 * P3**2
print(P)
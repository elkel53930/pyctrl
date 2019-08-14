from control.matlab import *


S1 = tf([0,1],[1,1])
S2 = tf([1,1],[1,1,1])
S = S2 * S1
print('S2 * S1 = ', S)
S = series(S1, S2)
print('series(S1, S2) = ', S)

S = S1 + S2
print('S1 + S2 = ',S)
S = parallel(S1, S2)
print('paralles(S1,S2) = ',S)

S = S1 / (1 + S1*S2)
print('S1 / (1 + S1*S2) = ', S.minreal())
S = feedback(S1, S2)
print('feedback(S1, S2) = ', S.minreal())


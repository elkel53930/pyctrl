import sympy as sp
sp.init_printing()
s = sp.Symbol('s')
root = sp.solve(2 * s**2 + 5*s + 3, s)
print(root)

f = sp.expand( (s+1)*(s+2)**2, s)
print(f)

g = sp.factor(f, s)
print(g)
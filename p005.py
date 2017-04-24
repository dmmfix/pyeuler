#!/usr/bin/python
import euler

total_factors = [0] * 21
for n in range(20,2,-1):
    f = euler.factors(n)
    while f:
        x = f[0]
        c = f.count(x)
        total_factors[x] = max(total_factors[x], c)
        f = [e for e in f if e != x]

prod = 1
for x in range(2,21):
    prod *= (x ** total_factors[x])

print(prod)
    
    

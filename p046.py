#!/usr/bin/python
import euler

primes = euler.sieve(10000)
comp   = list(map(lambda x: 1 - x, primes))
comp[0] = 0
comp[1] = 0
#for c in range(len(comp)):
#    if c & 1 == 0:
#        comp[c] = 0

for p in range(len(primes)):
    if not primes[p]:
        continue
    c = 1
    v = p + 2 * c**2
    while v < len(comp):
        comp[v] = 0
        c += 1
        v = p + 2 * c**2

print(comp.index(1))

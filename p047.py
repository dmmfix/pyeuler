#!/usr/bin/python
import euler

primes  = euler.sieve(1000000)
factors = [0] * len(primes)

for x in range(0,len(primes)):
    if primes[x]:
        for s in range(x,len(primes),x):
            factors[s] += 1

for x in range(0, len(factors)-3):
    if (factors[x:x+4] == [4,4,4,4]):
        print(x)
        break


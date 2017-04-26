#!/usr/bin/python
import euler

isprime = euler.sieve(1000000)
primes  = [x for x in range(1000000) if isprime[x]]

for run in range(1000,20,-1):
    for start in range(len(primes) - run):
        v = sum(primes[start:start + run])
        if v >= 1000000:
            break
        if isprime[v]:
            print(run, v)
            exit(0)
        

#!/usr/bin/python
import euler

primes = euler.sieve(1000000)

max_run = 0
max_prod = 0
for b in range(2,1001):
    for a in range(-b,1001):
        run_len = 0
        for n in range(0,80):
            v = n*n + a*n + b
            if v < 2 or primes[v] == 0:
                break
            run_len += 1
        if run_len > max_run:
            max_run = run_len
            max_prod = a*b
            #print(a, b, a*b, max_run)

print(max_prod)

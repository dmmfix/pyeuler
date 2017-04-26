#!/usr/bin/python
import euler

primes = euler.sieve(10000)

def check_triple_gap(ps):
    for f in range(len(ps)-2):
        for s in range(f+1,len(ps)-1):
            d = ps[s] - ps[f]
            if ps[s] + d in ps:
                print(ps[f], ps[s], ps[s] + d)
                return

def prime_perms(n):
    digits = euler.digits(n)
    return sorted(set(filter(lambda x: primes[x], map(euler.num_from_digits, euler.perms(sorted(digits))))))
    

for n in range(1000, len(primes)):
    if not primes[n]:
        continue
    ps = prime_perms(n)
    if ps[0] != n:
        continue
    check_triple_gap(ps)


#!/usr/bin/python
import euler
import itertools
import math
import operator

RCache = {}
RCache[2] = 1

def resiliance(d, base_primes):
    global RCache
    bn = reduce(operator.mul, base_primes, 1)
    if (d == bn):
        if not d in RCache:
            pn = reduce(operator.mul, base_primes[:-1], 1)
            RCache[d] = (base_primes[-1] - 1) * resiliance(pn, base_primes[:-1])
        return RCache[d]
    else:
        copies = d // bn
        rnum   = resiliance(bn, base_primes)
        return (rnum*copies)

def n_with_fac_less(p):
    assert euler.is_prime(p)
    yield 1
    for n in range(2,p):
        if max(euler.factors(n)) < p:
            yield n


Target = 15499/94744.0

msf  = 1
base = []
for p in euler.primes():
    base.append(p)
    bn = reduce(operator.mul, base, 1)
    for n in n_with_fac_less(p):
        i = n * bn
        r = resiliance(i, base) / float(i-1)
        if r < Target:
            print(i, r, euler.factors(i))
            exit(0)

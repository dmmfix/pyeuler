#!/usr/bin/python
import euler

UpTo = 1000000

primes = euler.sieve(UpTo)
circular = [0] * len(primes)

def rotate(d):
    return d[-1:] + d[:-1]

def num_from_digits(d):
    f = 1
    s = 0
    for x in d:
        s += x*f
        f *= 10
    return s

for x in range(0, len(primes)):
    if not primes[x]:
        continue
    if circular[x]:
        continue
    d = rotate(euler.digits(x))
    rd = num_from_digits(d)
    while rd != x:
        if not primes[rd]:
            break
        d = rotate(d)
        rd = num_from_digits(d)

    if rd == x:
        d = rotate(d)
        rd = num_from_digits(d)
        circular[x] = 1
        while rd != x:
            circular[rd] = 1
            d = rotate(d)
            rd = num_from_digits(d)

print('Total count: ', sum(circular))

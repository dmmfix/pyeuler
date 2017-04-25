#!/usr/bin/python
import euler

UpTo = 1000000

primes = euler.sieve(UpTo)
circular = [0] * len(primes)

def rotate(d):
    return d[-1:] + d[:-1]

for x in range(0, len(primes)):
    if not primes[x]:
        continue
    if circular[x]:
        continue
    d = rotate(euler.digits(x))
    rd = euler.num_from_digits(d)
    while rd != x:
        if not primes[rd]:
            break
        d = rotate(d)
        rd = euler.num_from_digits(d)

    if rd == x:
        d = rotate(d)
        rd = euler.num_from_digits(d)
        circular[x] = 1
        while rd != x:
            circular[rd] = 1
            d = rotate(d)
            rd = euler.num_from_digits(d)

print('Total count: ', sum(circular))

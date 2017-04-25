#!/usr/bin/python
import euler


def divisors(factors):
    x = 0
    d = [1]
    prod = 1
    for perm in range(0,1 << len(f)):
        for pos in range(0, len(f)):
            if (x & (1 << pos)):
                x &= ~(1 << pos)
                prod /= f[pos]
            else:
                x |= (1 << pos)
                prod *= f[pos]
                break
        if (not prod in d):
            d.append(prod)
    return d

tn = 1
c  = 1
ld = 1
while ld < 500:
    c += 1
    tn += c
    f = euler.factors(tn)
    if (len(f) > 8):
        d = divisors(f)
        ld = len(d)

print(c, tn, ld)

#!/usr/bin/python
import euler

tn = 1
c  = 1
ld = 1
while ld < 500:
    c += 1
    tn += c
    f = euler.factors(tn)
    if (len(f) > 8):
        d = euler.divisors(f)
        ld = len(d)

print(c, tn, ld)

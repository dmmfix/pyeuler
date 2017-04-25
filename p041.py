#!/usr/bin/python
import euler

for pn in range(7,1,-1):
    digits = list(reversed(range(1,pn+1)))
    for p in euler.perms(digits, rev=True):
        n = euler.num_from_digits(reversed(p))
        if (n % 2 == 0 or
            n % 3 == 0 or
            n % 5 == 0 or
            n % 7 == 0 or
            n % 11 == 0):
            continue
        if euler.is_prime(n):
            print(n)
            exit(0)

#!/usr/bin/python
import euler
import math

def is_trunc(n):
    if not euler.is_prime(n):
        return False
    d = euler.digits(n)
    for c in range(1,len(d)):
        lt = euler.num_from_digits(d[:-c])
        rt = euler.num_from_digits(d[c:])
        if not (euler.is_prime(lt) and euler.is_prime(rt)):
            return False
    return True
    
# Not very elegant
TruncPrimes = {}
num = 0
n = 11
while num < 11:
    if (is_trunc(n)):
        TruncPrimes[n] = 1
        num += 1
    n += 2

print(TruncPrimes.keys())
print(sum(TruncPrimes.keys()))

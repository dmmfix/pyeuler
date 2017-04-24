#!/usr/bin/python
import euler

p = 0
n = 1
while p < 10001:
    n += 1
    if (n % 2 == 0) or (n % 3 == 0) or (n % 5 == 0):
        continue
    if len(euler.factors(n)) == 1:
        p += 1
       

print(n)

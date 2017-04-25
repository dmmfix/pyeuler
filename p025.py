#!/usr/bin/python
import euler

f0 = 1
f  = 1
n  = 2

ndig = 1000
while f < (10 ** (ndig-1)):
    f0, f, n = f, f0+f, n+1

print(n)

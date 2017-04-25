#!/usr/bin/python
import euler

Limit = 1000000
Collatz = {}
Collatz[1] = 1

def chain(n):
    global Collatz
    if (not n in Collatz):
        if n & 1:
            Collatz[n] = chain(3*n + 1) + 1
        else:
            Collatz[n] = chain(n/2) + 1
    return Collatz[n]

max    = 0
maxval = 0
for x in range(2,Limit):
    val = chain(x)
    if (val > maxval):
        max, maxval = x, val

print('{}: {}'.format(max, maxval))

#!/usr/bin/python
import euler
import math

TriSolns = [0] * 1001

Squares = {}
for x in range(1,1000):
    Squares[x*x] = 1

for a in range(1, 500):
    b = a-1
    while (a+b < 1000):
        b += 1

        c2  = a*a + b*b
        if c2 not in Squares:
            continue

        abc = int(a+b+math.sqrt(c2))
        if abc <= 1000:
            TriSolns[abc] += 1

print(max(TriSolns), TriSolns.index(max(TriSolns)))

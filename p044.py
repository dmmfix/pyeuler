#!/usr/bin/python
import euler

Pentagonal = map(lambda x: x * (3*x - 1)/2, range(1,10000))
PentagonalHash = {}
for p in Pentagonal:
    PentagonalHash[p] = 1

for k in range(len(Pentagonal)):
    for j in range(k):
        d = Pentagonal[k] - Pentagonal[j]
        s = Pentagonal[k] + Pentagonal[j]
        if d in PentagonalHash and s in PentagonalHash:
            print(d, k, j)
            exit(0)

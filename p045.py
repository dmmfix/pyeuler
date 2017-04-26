#!/usr/bin/python
import euler

def poly(fn):
    n = 1
    while True:
        yield fn(n)
        n += 1

triN  = poly(lambda x: x * (x + 1) / 2)
pentN = poly(lambda x: x * (3*x - 1) / 2)
hexN  = poly(lambda x: x * (2*x - 1))

# Eat the trivial one
triN.next()

Matches = []
currT = -2
currP = -1
currH = 0
while len(Matches) < 2:
    if currT == min(currT, currP, currH):
        currT = triN.next()
    elif currP == min(currT, currP, currH):
        currP = pentN.next()
    else:
        currH = hexN.next()
    if (currT == currP and currT == currH):
        Matches.append(currT)

print(Matches)

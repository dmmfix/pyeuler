#!/usr/bin/python
import euler
import math

def is_pand_multiple(n):
    for f in range(1,5):
        nd = euler.digits(n)
        basen = euler.num_from_digits(nd[-f:])
        currn = basen
        nd   = nd[:-f]
        while nd:
            currn += basen
            cnd = euler.digits(currn)
            if (nd[-len(cnd):] != cnd):
                break
            nd = nd[:-len(cnd)]
        if not nd:
            return True
    return False

for p in euler.perms(list(reversed(range(1,10))), rev=True):
    n = euler.num_from_digits(reversed(p))
    if (is_pand_multiple(n)):
        print(n)
        break

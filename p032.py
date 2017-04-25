#!/usr/local/bin/python3
import euler

def is_pandigital(n):
    if n == 0:
        return False

    pd = euler.proper_div(n)
    if len(pd) == 1:
        return False

    bd = euler.digits(n)
    bda = [0] * 10
    bda[0] = 1
    for d in bd:
        if bda[d]:
            return False
        bda[d] = 1

    for x in range(1, (len(pd)+1)//2):
        tda = bda.copy()
        for d in euler.digits(pd[x]):
            if tda[d]:
                continue
            tda[d] = 1
        for d in euler.digits(n // pd[x]):
            if tda[d]:
                continue
            tda[d] = 1
        if (sum(tda[1:]) == 9):
            return True
    return False


Sum = 0
ipd = list(map(is_pandigital, range(0, 10000)))
for pd in range(0, 10000):
    if ipd[pd]:
        print(pd)
        Sum += pd

print('Total sum:', Sum)

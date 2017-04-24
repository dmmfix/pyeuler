#!/usr/bin/python
from math import sqrt

for x0 in range(1000,0,-1):
    for x1 in range(x0,0,-1):
        c = x0*x0 + x1*x1
        isc = int(sqrt(c))
        if (x0+x1+isc == 1000 and sqrt(c) == isc):
            print('{}^2 + {}^2 = {}^2'.format(x1, x0, isc))
            print(x0 * x1 * isc)
            quit()

#!/usr/bin/python
import euler

OddFractions = []
def check_frac(n, d, bn, bd):
    global OddFractions
    if (bd == 0):
        return
    proper   = n  / float(d)
    improper = bn / float(bd)
    if abs(proper - improper) < 0.00000001:
        print('{} / {} = {} / {}'.format(n, d, bn, bd))
              
for n in range(10,100):
    nd = euler.digits(n)
    for d in range(n+1,100):
        if (n == d):
            continue
        dd = euler.digits(d)
        if nd[0] == dd[0] and dd[0] != 0: check_frac(n, d, nd[1], dd[1])
        if nd[1] == dd[0] and dd[0] != 0: check_frac(n, d, nd[0], dd[1])
        if nd[0] == dd[1] and dd[1] != 0: check_frac(n, d, nd[1], dd[0])
        if nd[1] == dd[1] and dd[1] != 0: check_frac(n, d, nd[0], dd[0])
            
        

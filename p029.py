#!/usr/bin/python
import euler
from sets import Set

Limit = 100

def powers(a):
    for b in range(2,Limit+1):
        yield a**b

AllPowers = Set()
for a in range(2, Limit+1):
    AllPowers |= Set(powers(a))

#print(sorted(AllPowers))
print('Count: ', len(AllPowers))

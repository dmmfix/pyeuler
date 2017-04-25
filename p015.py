#!/usr/bin/python
import euler
from math import factorial

def binomial(x, k):
    return factorial(x) // (factorial(k) * factorial(x - k))

print(binomial(40, 20))

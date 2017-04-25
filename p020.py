#!/usr/bin/python
import euler
from operator import add
from math import factorial

print(reduce(add, euler.digits(factorial(100)), 0))


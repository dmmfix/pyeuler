#!/usr/bin/python
import euler
from math import factorial

facts = list(map(factorial, range(10)))

Sum = 0
for n in range(3, 7 * factorial(9)):
    if n == sum(map(lambda x: facts[x], euler.digits(n))):
        print n
        Sum += n
    n += 1

print('Total sum: {}'.format(Sum))

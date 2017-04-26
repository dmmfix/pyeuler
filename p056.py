#!/usr/bin/python
import euler
import math

maxSum = sum(euler.digits(99**99))
max = [99, 99]

for a in range(99,1,-1):
    minB = int(math.floor((maxSum / 9) * math.log(10, a)))
    for b in range(99,minB,-1):
        s = sum(euler.digits(a**b))
        if (s > maxSum):
            maxSum = s
            max = [a,b]

print('maxSum = {}'.format(maxSum))
print('{}**{} = {}'.format(a, b, a**b))

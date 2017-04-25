#!/usr/bin/python
import euler

Power = 5
Sum = 0
for x in range(2,9**Power * Power):
    if x == sum(map(lambda x: x**Power, euler.digits(x))):
        Sum += x

print(Sum)

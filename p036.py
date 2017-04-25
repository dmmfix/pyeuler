#!/usr/bin/python
import euler

Sum = 0
for n in range(1,1000000):
    if euler.is_pal(n,10) and euler.is_pal(n,2):
        Sum += n

print(Sum)

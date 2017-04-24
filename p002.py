#!/usr/bin/python

sum = 0
f0 = 1
f  = 2
while f < 4000000:
    if (f % 2) == 0:
        sum += f
    f, f0 = f+f0, f

print(sum)

#!/usr/bin/python

ss = 0
s = 0
for x in range(1,101):
    ss += x*x
    s += x

print(s*s - ss)

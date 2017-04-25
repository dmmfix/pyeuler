#!/usr/bin/python
import euler
from operator import add

Limit = 10000
friends = [0] * Limit
for n in range(2,Limit):
    friends[n] = sum(euler.proper_div(n))

total = 0
for n in range(2,Limit):
    if (friends[n] >= Limit):
        continue

    if (friends[friends[n]] == n and friends[n] != n):
        total += n + friends[n]
        print(n, friends[n])
        friends[friends[n]] = 0
        friends[n] = 0

print(total)

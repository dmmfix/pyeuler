#!/usr/bin/python
import euler

Limit = 2000000

prime = euler.sieve(Limit)

sum = 0
for x in range(2,Limit):
    if (prime[x]):
        sum += x

print(sum)

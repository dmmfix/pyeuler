#!/usr/bin/python
import euler

Limit = 2000000

prime = [0, 1] * (Limit/2)
prime[1] = 0
prime[2] = 1

for x in range(3,Limit):
    if prime[x] != 0:
        for m in range(2*x,Limit,x):
            prime[m] = 0

sum = 0
for x in range(2,Limit):
    if (prime[x]):
        sum += x

print(sum)

#!/usr/bin/python
import euler

def modpow(a, b, mod):
    if b == 0: return 1
    if b == 1: return a % mod
    if b & 1:
        return (a * modpow(a*a, b//2, mod)) % mod
    else:
        return modpow(a*a, b//2, mod)

#    prod = 1
#    while b != 0:
#        if b & 1:
#            prod = (prod * a) % mod
#            b -= 1
#        else:
#            prod = (prod * prod) % mod
#            b //= 2
#    return prod


print(sum(map(lambda x: modpow(x, x, int(1e10)), range(1,1001))) % int(1e10))

from math import sqrt,ceil

def digits(x):
    d = []
    while x > 0:
        d.append(x % 10)
        x /= 10
    return d

#def factors(n):
#    sn = sqrt(n)
#    factors = []
#    total_product = 1
#    cn = n
#    x = 2
#    while total_product != n and x <= sn:
#        if (cn % x) == 0:
#            factors.append(x)
#            total_product *= x
#            cn /= x
#        else:
#            x += 1
#    if (cn != 1):
#        factors.append(cn)
#    return factors

def sieve(n):
    prime = [0, 1] * (n/2)
    prime[1] = 0
    prime[2] = 1
    for x in range(3,n):
        if prime[x] != 0:
            for m in range(2*x,n,x):
                prime[m] = 0
    return prime
    

FactorCache = {1:[]}
def factors_cache(n, start=2):
    global FactorCache
    if not n in FactorCache:
        sn = int(sqrt(n))
        for t in range(start, sn+1):
            if (n % t) == 0:
                FactorCache[n] = [t] + factors_cache(n // t, t)
                return FactorCache[n]
        FactorCache[n] = [n]
    return FactorCache[n]

def divisors(f):
    x = 0
    d = [1]
    prod = 1
    for perm in range(0,1 << len(f)):
        for pos in range(0, len(f)):
            if (x & (1 << pos)):
                x &= ~(1 << pos)
                prod /= f[pos]
            else:
                x |= (1 << pos)
                prod *= f[pos]
                break
        if (not prod in d):
            d.append(prod)
    return d

def proper_div(n):
    d = divisors(factors_cache(n))
    return d[:-1]


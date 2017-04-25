from math import sqrt

def digits(x):
    d = []
    while x > 0:
        d.append(x % 10)
        x /= 10
    return d

def factors(n):
    sn = sqrt(n)
    factors = []
    total_product = 1
    cn = n
    x = 2
    while total_product != n and x <= sn:
        if (cn % x) == 0:
            factors.append(x)
            total_product *= x
            cn /= x
        else:
            x += 1
    if (cn != 1):
        factors.append(cn)
    return factors

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
    d = divisors(factors(n))
    return d[:-1]


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

from math import sqrt,ceil

def digits(x):
    d = []
    while x > 0:
        d.append(x % 10)
        x //= 10
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
    prime = [0, 1] * (n//2)
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
                prod //= f[pos]
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

def next_perm(s):
    for x in range(len(s)-2, -1, -1):
        if s[x] < s[x+1]:
            sy = x+1
            for y in range(x+2,len(s)):
                if s[y] > s[x] and s[y] < s[sy]:
                    sy = y
            s[sy],s[x] = s[x],s[sy]
            s[x+1:] = sorted(s[x+1:])
            return s
    return None

def num_from_digits(d):
    f = 1
    s = 0
    for x in d:
        s += x*f
        f *= 10
    return s

def perms(s):
    s = sorted(s)
    while s:
        yield s
        s = next_perm(s)

def is_pal(x, base=10):
    if base == 10:
        str = '{:d}'.format(x)
    elif base == 2:
        str = '{:b}'.format(x)
    elif base == 16:
        str = '{:x}'.format(x)
    else:
        raise('Invalid base')
    return str == str[::-1]
        

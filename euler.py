from math import sqrt,ceil
import operator

def digits(x):
    d = []
    while x > 0:
        d.append(x % 10)
        x //= 10
    return d

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

def factors(n):
    return factors_cache(n)

def is_prime(n):
    if (n < 2):
        return False
    return len(factors_cache(n)) == 1

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

def next_perm(s, fCMP = cmp):
    for x in range(len(s)-2, -1, -1):
        if fCMP(s[x], s[x+1]) < 0:
            sy = x+1
            for y in range(x+2,len(s)):
                if fCMP(s[y], s[x]) > 0 and fCMP(s[y], s[sy]) < 0:
                    sy = y
            s[sy],s[x] = s[x],s[sy]
            s[x+1:] = sorted(s[x+1:], cmp=fCMP)
            return s
    return None

def num_from_digits(d):
    f = 1
    s = 0
    for x in d:
        s += x*f
        f *= 10
    return s

def perms(s, rev=False):
    while s:
        yield s
        s = next_perm(s) if not rev else next_perm(s, lambda x,y: -cmp(x,y))

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

def read_words(fn):
    return map(lambda x: x.strip('"'), open(fn).read().split(','))


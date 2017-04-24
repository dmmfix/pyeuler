#!/usr/bin/python
import euler

def is_pal(x):
    d = euler.digits(x)
    f = 0
    b = len(d) - 1
    while f < b:
        if d[f] != d[b]:
            return False
        f += 1
        b -= 1
    return True

largest = 0
for top in range(999,99,-1):
    for bottom in range(top,99,-1):
        if (top * bottom > largest) and is_pal(top * bottom):
            largest = top * bottom
            break

print(largest)

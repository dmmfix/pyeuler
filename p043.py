#!/usr/bin/python
import euler

def has_div(d, os, denom):
    s = 9 - os
    if denom == 2:
        return d[s-2] & 1 == 0
    if denom == 3:
        return sum(d[s:s-3:-1]) % 3 == 0
    if denom == 5:
        return d[s-2] == 5 or d[s-2] == 0
    return euler.num_from_digits(d[s-2:s+1]) % denom == 0

def has_property(d):
    return (has_div(d, 1, 2) and
            has_div(d, 2, 3) and
            has_div(d, 3, 5) and
            has_div(d, 4, 7) and
            has_div(d, 5, 11) and
            has_div(d, 6, 13) and
            has_div(d, 7, 17))

digits = range(10)
Valid = []

while digits:
    if (has_property(digits)):
        Valid.append(euler.num_from_digits(digits))
    digits = euler.next_perm(digits)

print(Valid)
print(sum(Valid))

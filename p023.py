#!/usr/bin/python
import euler

abundant = []
for x in range(12, 28123):
    if sum(euler.proper_div(x)) > x:
        abundant.append(x)

as_sum = [0] * 28124
for x in range(0, len(abundant)):
    abx = abundant[x]
    for y in range(x, len(abundant)):
        aby = abundant[y]
        if abx + aby > 28123:
            break
        else:
            as_sum[abx + aby] = 1

total = 0
for x in range(1, len(as_sum)):
    if as_sum[x] == 0:
        total += x

print(total)

#!/usr/bin/python
import euler

def scorename(pos, name):
    score = 0
    for x in name:
        score += ord(x) - ord('A') + 1
    return score * pos

names = sorted(euler.read_names('data/p022_names.txt'))

total = 0
for x in range(0, len(names)):
    total += scorename(x+1, names[x])

print(scorename(938, 'COLIN'))
print(total)

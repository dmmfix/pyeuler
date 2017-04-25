#!/usr/bin/python
import euler

largest = 0
for top in range(999,99,-1):
    for bottom in range(top,99,-1):
        if (top * bottom > largest) and euler.is_pal(top * bottom):
            largest = top * bottom
            break

print(largest)

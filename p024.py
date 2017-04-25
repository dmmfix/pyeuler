#!/usr/bin/python
import euler

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


arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(1, 1000000):
    arr = next_perm(arr)

print(arr)
print(''.join(arr))

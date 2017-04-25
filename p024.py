#!/usr/bin/python
import euler


arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(1, 1000000):
    arr = euler.next_perm(arr)

print(arr)
print(''.join(arr))

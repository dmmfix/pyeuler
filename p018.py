#!/usr/bin/python
import euler
import triangle

tri = triangle.read('data/triangle_018.txt')
print(triangle.max_path(tri, triangle.zero(tri), 0, 0))

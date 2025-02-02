from math import *

def vector_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_polygon(points):
    if len(points) < 3:
        return False
    start = min(points, key=lambda p: (p[1], p[0]))
    points.sort(key=lambda p: atan2(p[1] - start[1], p[0] - start[0]))
    for i in range(len(points)):
        o = points[i]
        a = points[(i + 1) % len(points)]
        b = points[(i + 2) % len(points)]
        if vector_product(o, a, b) <= 0:
            return False 
    return True

args = []
while a:= input():
    x, y = map(int, a.split(", "))
    args.append((x, y))
print(convex_polygon(args))
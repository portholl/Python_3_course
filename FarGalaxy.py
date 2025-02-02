import math

def distance(coord1, coord2):
    return (coord1[0] - coord2[0]) * (coord1[0] - coord2[0]) + (coord1[1] - coord2[1]) * (coord1[1] - coord2[1]) + (coord1[2] - coord2[2]) * (coord1[2] - coord2[2])

galaxies = dict()
a = input()
while " " in a:
    a = a.split()
    x, y, z =  map(float, a[:3])
    galaxies[(x, y, z)] = a[3]
    a = input()

galaxy_names = list(galaxies.keys())
pairs = [(galaxy_names[i], galaxy_names[j]) for i in range(len(galaxy_names)) for j in range(i + 1, len(galaxy_names))]
M = 0
for i in pairs:
    ma = distance(*i)
    if ma > M:
        M = ma 
        x, y  = i
print(*sorted((galaxies[x], galaxies[y])))
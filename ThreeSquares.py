seq = set(eval(input()))
from math import *
s = set()
M = max(seq)
for i in range(1, int(sqrt(M)) +1 ):
    for j in range(i, int(sqrt(M - i*i)) + 1):
        for k in range(j, int(sqrt(M - i*i - j*j)) + 1 ):
            s.add(i*i + j*j + k*k)
print(len(seq & s))
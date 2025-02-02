from math import *
flag = False
a = int(input())
for i in range(2, int(sqrt(a)) + 1):
    p = i
    while p <= a:
        if p == a:
            flag = True
        p *=i
if flag: print("YES")
else: print("NO")

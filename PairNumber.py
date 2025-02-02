res = []
while a:= input():
    res += a.split()
r = set()
for i in range(len(res)-1):
    r.add(frozenset({str(res[i]), str(res[i+1])}))
print(len(r))
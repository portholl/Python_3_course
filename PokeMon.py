name = dict()
deck = dict()
while True:
    a = input()
    if not a: break
    a = a.split(" / ")
    if a[0][0].isalpha():
        if a[0] in name:
            name[a[0]].append(a[1])
        else:
            name[a[0]] = [a[1]]
    else:
        if a[0] in deck:
            deck[a[0]].append(a[1])
        else:
            deck[a[0]] = [a[1]]
ansv = dict()
for i in name:
    myset = set()
    for j in name[i]:
        for k in deck[j]:
            myset.add(k)
    ansv[i] = len(myset)
        
    
M = max(ansv.values())
print(*sorted(i for i, d in ansv.items() if d == M), sep = "\n")
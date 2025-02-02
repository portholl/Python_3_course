def compare(a,b):
    a = sorted(a)
    b = sorted(b)
    return all((a[i] <= b[i] for i in range(3))) and any((a[i] != b[i] for i in range(3)))

ansv = list()
while a:= input():
    a = list(eval(a))
    ansv.append(a)

for k in range(len(ansv)):
    for i in range(k, len(ansv)):
        for j in range (i+1, len(ansv)):
            if compare(ansv[i] , ansv[j]):
                break
        else:
            new = ansv[i]
            ansv.pop(i)
            ansv.insert(k, new)
            break
for i in ansv:
  print(", ".join(str(x) for x in i))

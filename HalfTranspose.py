a = input()
ansv = list()
if a :
   a = eval(a)
   ansv.append(a)
result = list()
for i in range(len(a)-1):
    b = eval(input())
    ansv.append(b)
result = list()
for i in range(len(a)):
    di =[]
    for j in range(i+1):
        di.append(ansv[i][j])
    for j in range(i-1,-1, -1):
        di.append(ansv[j][i])
    result.append(di)
for i in result:
  print(",".join(str(x) for x in i))
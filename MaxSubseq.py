b = int(input())
count , MA = 1 , 0
while b != 0:
    a = int(input()) 
    if a == 0: 
        MA = max(MA, count)
        break
    if b <= a: count+=1
    else:
        if ( MA < count): MA = count
        count = 1
    b = a
print(MA)
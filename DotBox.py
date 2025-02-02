max1, max2, max3 = eval(input())
min1, min2, min3 = max1, max2, max3
a = input()
while a != "" and a!= "…":
    a = eval(a)
    max1 = max(max1, (a[0]))
    max2 = max(max2, (a[1]))
    max3 = max(max3, (a[2]))
    min1 = min(min1, a[0])
    min2 = min(min2, a[1])
    min3 = min(min3, a[2])
    a = input()
if (max1 == min1) or (max2 == min2) or (max3 == min3): 
    print(0) 
else:
    print(abs(max1 - min1)*abs(max2-min2)* abs(max3-min3))
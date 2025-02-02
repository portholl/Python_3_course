from math import *
a, b,c = eval((input()))
dis1 = b*b-4*a*c
if a==0:
    if b==0 :
        if c==0:
            print(-1)
        else: print(0)
    else: 
        if c ==0 :
            print(0)
        elif c/b < 0 : print(-sqrt(-c/b), sqrt(-c/b), sep =" " )
        else: print(0)
else:
    if b ==0:
        if c == 0:
            print(0) 
        elif -c/a > 0 : print(-pow(-c/a, 1/4), pow(-c/a, 1/4) )
        else: print(0)
    else:
        ansv = list()
        if (dis1 > 0):
            if (-b + sqrt(dis1))/2*a > 0 :
                ansv += ( -sqrt( (-b + sqrt(dis1))/2/a ), sqrt( (-b + sqrt(dis1))/2/a ) )
            if (-b - sqrt(dis1))/2*a > 0:
                ansv += ( -sqrt( (-b - sqrt(dis1))/2/a ), sqrt( (-b - sqrt(dis1))/2/a ) )
            if c==0: ansv.append(0)
            print(*sorted(ansv))
            if len(ansv) == 0: print(0)
        elif dis1 == 0: 
            if (-b/2/a > 0 ): print(-sqrt(-b/2/a),sqrt(-b/2/a) )
            else: print(0)
        else: print(0)
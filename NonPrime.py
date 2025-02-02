def nonprime(n = 0):
    n+=1
    while True:
        flag = False
        if n > 1:
            for i in range(2, int(n**0.5)+ 1):
                if n % i == 0:
                    flag = True
                    break
        if n == 1 or flag:
            yield n
        n+=1
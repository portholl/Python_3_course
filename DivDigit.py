def divdigit(N):
    count = 0
    for i in str(N):
        if int(i) != 0 and int(N) % int(i) == 0:
            count +=1
    return(count)
exec(__import__("sys").stdin.read(), globals())
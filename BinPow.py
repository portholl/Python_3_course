def BinPow(a, n, f):
    if n == 1:
        return a
    result = a
    n -= 1 
    while n > 1:
        if n % 2 == 1:
            result = f(result, a)
            n -= 1
        else:
            a = f(a, a)
            n //= 2
    return f(result, a) 
exec(__import__("sys").stdin.read(), globals())
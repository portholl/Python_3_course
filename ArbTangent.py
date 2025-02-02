import decimal
A = decimal.Decimal(input())
E = int(input())
decimal.getcontext().prec = E + 5  

def compute_pi():
    pi = decimal.Decimal(13591409)
    C = decimal.Decimal(1)
    for i in range(1, E + 1):
        C *= -decimal.Decimal((6 * i - 5) * (2 * i - 1) * (6 * i - 1)) / decimal.Decimal(i**3 * 26680 * 640320**2)
        L = C * (13591409 + 545140134 * i)
        pi += L
    pi = pi * decimal.Decimal(10005).sqrt() / 4270934400
    pi = pi**(-1)
    return pi

def grad_to_radians(g, pi):
    return decimal.Decimal(g * pi / 200)

def sin(x):
    x = x % (2 * pi)
    count = x
    s = x
    for n in range(1, 2000):  
        s *= -x**2 / ((2 * n) * (2 * n + 1))
        count += s
    return count

def cos(x):
    x = x % (2 * pi)
    count = 1
    s = 1
    for n in range(1, 2000):  
        s *=  -x**2 / ((2 * n - 1) * (2 * n))
        count += s
    return count


pi = compute_pi()
R = grad_to_radians(A, pi)
t = decimal.Decimal(sin(R) / cos(R))
decimal.getcontext().prec = E

print(f'{t:.{E}}')
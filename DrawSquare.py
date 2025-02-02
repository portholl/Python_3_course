def squares(w, h, *args):
    res = [['.' for _ in range(w)] for _ in range(h)]
    for i in args:
        x, y, s, c = i
        for k in range(y, y + s):
            for j in range(x, x + s):
                res[k][j] = c
    for i in res:
         print(''.join(i))

exec(__import__("sys").stdin.read(), globals())
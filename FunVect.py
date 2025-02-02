def superposition(funmod, funseq):
    funres = []
    for i in funseq:
        def f(x,j = i):
            return funmod(j(x))
        funres.append(f)
    return funres
from math import *
exec(__import__("sys").stdin.read(), globals())
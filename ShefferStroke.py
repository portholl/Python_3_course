def sheff(A, B):
    if not(A and B): 
        if (not A and not B): return True
        else: return (A or B)
    else: return False

exec(__import__("sys").stdin.read(), globals())
from itertools import *
def seesaw(sequence):
    n2, n1 = tee(sequence, 2)
    n1 = (i for i in n1 if i%2 !=0)
    n2 = (i for i in n2 if i%2 ==0)
    for i, j in zip_longest(n2, n1, fillvalue=""):
        if i != "": yield i
        if j != "": yield j
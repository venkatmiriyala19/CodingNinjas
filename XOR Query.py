from os import *
from sys import *
from collections import *
from math import *

def xorQuery(queries):
    a=[]
    xor=0
    for i in queries:
        if i[0]==1:
            a.append(i[1]^xor)
        else:
            xor=xor^i[1]
    for i in range(len(a)):
        a[i]=a[i]^xor
    return a
    # Write your code here.
    pass

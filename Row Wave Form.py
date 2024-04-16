from os import *
from sys import *
from collections import *
from math import *

def rowWaveForm(mat):
    a=[]
    flag=True
    for i in mat:
        if  flag:
            a.append(i)
            flag=False
        else:
            b=[]
            b[:]=i
            b.reverse()
            a.append(b)
            flag=True
            
    b=[]
    for i in a:
        b+=i
    return b
    # Write your code here.
    pass

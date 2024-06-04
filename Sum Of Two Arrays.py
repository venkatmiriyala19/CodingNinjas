from os import *
from sys import *
from collections import *
from math import *

def findArraySum(a, n, b, m):
    fnum=0
    snum=0
    for i in a:
        fnum=fnum*10+i
    for i in b:
        snum=snum*10+i
    c=fnum+snum
    d=[]
    while(c!=0):
        rem=c%10
        d.append(rem)
        c=c//10
    return d[::-1]

    # Write your code here.
    pass

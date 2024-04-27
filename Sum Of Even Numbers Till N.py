from os import *
from sys import *
from collections import *
from math import *

def evenSumTillN(n):
    s=0
    for i in range(n+1):
        if i%2==0:
            s+=i
    return s

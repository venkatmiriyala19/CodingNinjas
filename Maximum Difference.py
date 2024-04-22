from os import *
from sys import *
from collections import *
from math import *

def maximumDifferece(n, arr):
    a=max(arr)
    b=min(arr)
    if (a-b)%2==0:
        return "EVEN"
    return "ODD"

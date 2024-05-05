from os import *
from sys import *
from collections import *
from math import *

def boringFactorials(n, p):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact%p

    # Write your code here.
    pass

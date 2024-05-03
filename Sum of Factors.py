from os import *
from sys import *
from collections import *
from math import *

def sumOfFactors(arr):
    a=[]
    for i in arr:
        b=[]
        for j in range(1,i+1):
            if i%j==0:
                b.append(j)
        a.append(sum(b))
    return a
    # Write your code here.

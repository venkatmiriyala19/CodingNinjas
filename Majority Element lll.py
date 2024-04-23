from os import *
from sys import *
from collections import *
from math import *

def countTheNumber(arr, n, k):
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    a=[]
    for i in freq:
        if freq[i]>=n/k:
            a.append(i)
    return a
    # Write your code here.
    pass

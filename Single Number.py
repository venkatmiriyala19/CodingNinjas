from sys import *
from collections import *
from math import *

def occursOnce(a, n):
    freq={}
    for i in a:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for i in freq:
        if freq[i]==1:
            return i
    # Write your code here.
    pass

from os import *
from sys import *
from collections import *
from math import *

def dominantNumber(arr, n):
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
            continue
        freq[i]=1
    for i in freq:
        if freq[i]>n/3:
            return i
    return -1

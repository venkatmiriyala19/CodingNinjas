from math import *
from collections import *
from sys import *
from os import *

def ninjaAndSortedArrays(arr1,arr2,m,n):
    arr1[:]=arr1[:m]
    for i in range(n):
        arr1.append(arr2[i])
    arr1.sort()
    return arr1
    # Write your code here.
    pass

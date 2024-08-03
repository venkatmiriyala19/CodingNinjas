from os import *
from sys import *
from collections import *
from math import *

def maxOne(arr):
    min_col=len(arr[0])
    min_row=0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]==1:
                break
        if j<min_col:
            min_col=j
            min_row=i
    return min_row
    # Write your code here.
    pass

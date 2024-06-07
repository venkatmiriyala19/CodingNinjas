from os import *
from sys import *
from collections import *
from math import *

def kthSmallest(arr, k):
    a=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            a.append(arr[i]*arr[j])
    a.sort()
    # print(a)
    if k>len(a):
        return -1
    return a[k-1]
    # Write your code here
    pass

from os import *
from sys import *
from collections import *
from math import *

def moveZerosToLeft(arr, n):
    c=arr.count(0)
    b=c*[0]
    for i in arr:
        if i!=0:
            b.append(i)
        
    # print(b)
    # arr=arr[n:]
    #     # print(arr)
    # b=c*[0]

    # arr=b+arr
    arr[:]=b
    return b
    # Write your code here
    pass

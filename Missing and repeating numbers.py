from math import *
from collections import *
from sys import *
from os import *

def missingAndRepeating(arr, n):
    b=[]
    arr.sort()
    a=arr[0]
    for i in range(1,n):
        if arr[i]==a:
            b.append(arr[i])
            arr.remove(arr[i])
            break
        a=arr[i]
    for i in range(len(arr)):
        if arr[i]!=i+1:
            b.append(arr[i]-1)
            break
    if len(b)==2:
        return b[1],b[0]
    return n,b[0]
            
    # Write your code here
    pass

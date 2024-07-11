from os import *
from sys import *
from collections import *
from math import *

def firstNegativeInteger(arr, k, n):
    y=False
    nums=[]
    neg=[]
    l=0
    i=0
    for j in range(n):
        if arr[j]<0:
            neg.append(arr[j])
        if j>=k-1:
            if len(neg)==0:
                nums.append(0)
            else:
                nums.append(neg[0])
                if (arr[i]==neg[0]):
                    neg.pop(0)
            i+=1
    # nums.append(neg[0])
    return nums
            

    # Write your code here.
    pass

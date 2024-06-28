from os import *
from sys import *
from collections import *
from math import *

def countDistinctElements(arr, k):
    i=0
    freq={}
    a=[]
    count=0
    for l in arr:
        freq[l]=0
    for j in range(len(arr)):
        if j<k:
            if freq[arr[j]]==0:
                count+=1    
            freq[arr[j]]+=1
        else:
            a.append(count)
            freq[arr[i]]-=1
            if freq[arr[i]]==0:
                count-=1
            i+=1
            if freq[arr[j]]==0:
                count+=1
            freq[arr[j]]+=1
    a.append(count)
    return a


    # Write your code here

    pass

from os import *
from sys import *
from collections import *
from math import *

def isPossible(arr, n):
    count=0
    for i in range(0,n-1):
        if(arr[i]>arr[i+1]):
            count+=1
            if (i!=0 and arr[i-1]>arr[i+1]):
                if (i+2<n and arr[i]>arr[i+2]):
                    return False
    if(count<=1):
        return True
    return False
    # Write your code here.
    pass

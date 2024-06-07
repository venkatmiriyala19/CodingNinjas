from os import *
from sys import *
from collections import *
from math import *

def absDiff(arr, n):
    if n==1:
        return [arr[0],0]
    even=arr[0]
    odd=arr[1]
    for i in range(2,n):
        if i%2==0:
            even=abs(even-arr[i])
        else:
            odd=abs(odd-arr[i])
    return [even,odd]


    # Write your code here.
    pass

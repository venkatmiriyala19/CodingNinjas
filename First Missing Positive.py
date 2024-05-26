from os import *
from sys import *
from collections import *
from math import *

def firstMissing(arr, n):
    s=set(arr)
    for i in range(1,n+1):
        if i not in s:
            return i
    return n+1
    # Write your function here.
    pass



    

# Main Code
t=int(input())

for j in range(t):
    n=int(input())
    arr=[int(i) for i in input().split()]
    ans = firstMissing(arr,n)

    print(ans)

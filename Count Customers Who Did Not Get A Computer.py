from os import *
from sys import *
from collections import *
from math import *

def countCustomers(arr, k):
    left=0
    s=set()
    l=set()
    for i in arr:
        if i in s:
            s.remove(i)
            
            
           
        elif len(s)<k:
            if i in l:
                continue
                
            s.add(i)
            
            
        else:
            if i not in l: 
                l.add(i)
                left+=1
    return left

    #    Write your code here.
    pass

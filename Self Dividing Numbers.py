from os import *
from sys import *
from collections import *
from math import *

def findAllSelfDividingNumbers(lower, upper):
    arr=[]
    for i in range(lower,upper+1):
        a=i
        while(i>0):
            rem=i%10
            
            if  rem==0 or a%rem!=0 :
                break
            i=i//10
        
        if i==0:
            arr.append(a)
    return arr

    # Write your code here
    # This function returns a list of all the self-dividing numbers in the range [left, right]
    pass

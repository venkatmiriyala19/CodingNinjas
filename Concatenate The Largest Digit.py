from os import *
from sys import *
from collections import *
from math import *

def concatLargestDigit(a, b, c):
    def maxi(n):
        maximum=0
        while(n!=0):
            rem=n%10
            maximum=max(rem,maximum)
            n=n//10
        return maximum
    maxA=maxi(a)
    maxB=maxi(b)
    maxC=maxi(c)
    return maxA*100+maxB*10+maxC
    

    # Write your code here
    pass

from os import *
from sys import *
from collections import *
from math import *

def countOf3(x):
    def count(n):
        counter=0
        while(n!=0):
            rem=n%10
            if rem==3:
                counter+=1
            n=n//10
        return counter
    count3=0
    for i in range(0,x+1):
        count3+=count(i)
    return count3
    # Write your code here.
    pass

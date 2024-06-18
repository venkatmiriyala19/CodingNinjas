from os import *
from sys import *
from collections import *
from math import *

def printPatt(n):
    count=0
    for i in range(n,0,-1):
        # print(i)
        if(count%2==0):
            print('1'*i)
        else:
            print('0'*i)
        count+=1
    
    # Write your code here.


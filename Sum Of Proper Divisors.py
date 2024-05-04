from os import *
from sys import *
from collections import *
from math import *

def sumOfProperDivisors(n):
    s=0
    for i in range(1,(n//2)+1):
        if n%i==0:
            s+=i
    return s
    # Write your code here.

    

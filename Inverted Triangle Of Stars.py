from os import *
from sys import *
from collections import *
from math import *

def Triangle(n):
    a=[]
    for i in range(n):
        spaces=' '*i
        stars='*'*(2*(n-i)-1)
        a.append(spaces+stars)
    return a
    # Write your code here.

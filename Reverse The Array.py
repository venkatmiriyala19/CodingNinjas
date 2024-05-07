from os import *
from sys import *
from collections import *
from math import *

def reverseArray(arr, m):
    b=arr[m+1:]
    b=b[::-1]
    return arr[:m+1]+b
    # Write your code here.
    pass

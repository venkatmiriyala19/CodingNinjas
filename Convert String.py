from os import *
from sys import *
from collections import *
from math import *

def convertString(stri):
    a=stri[0].upper()
    s=a
    for i in range(1,len(stri)):
        b=stri[i]
        if stri[i-1]==" ":
            b=stri[i].upper()
        s+=b
    return s
    # Write your code here
    pass

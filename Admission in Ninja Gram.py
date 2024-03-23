from os import *
from sys import *
from collections import *
from math import *

def ninjaGram(str):
    str=str.lower()
    a=[x for x in str]
    s=set(a)
    b=len(s)
    # print(len(s))
    if b==26:
        return True
    return False

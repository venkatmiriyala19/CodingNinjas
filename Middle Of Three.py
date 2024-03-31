from sys import *
from collections import *
from math import *

def middleOfThree(x:int, y:int, z:int):
    
    a=(x+y+z)/3
    b,c,d=abs(x-a),abs(y-a),abs(z-a)
    if b<c and b<d:
        return x
    if c<b and c<d:
        return y
    return z
    

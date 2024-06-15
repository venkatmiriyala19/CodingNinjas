from sys import *
from collections import *
from math import *

def findFirstRepeatingDigit(digitPattern):
    s=set()
    for i in digitPattern:
        if i in s:
            return i
        s.add(i)
    return '-1'

    # Write your code here.
    # This function returns the first repeating digit integer value.
    pass

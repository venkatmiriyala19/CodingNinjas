from os import *
from sys import *
from collections import *
from math import *

def isReflectionEqual(s):
    z=s[::-1]
    if s!=z:
        return 'NO'
    for i in s:
        # print(i)
        if i not in "AHIMOTUVWXY":
            # print(i)
            return False
    return True
    # Write your code here.
    pass

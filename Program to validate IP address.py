from os import *
from sys import *
from collections import *
from math import *

def isValidIPv4(ipAddress):
    a=ipAddress.split('.')
    if len(a)!=4:
        return False
    # print(a)
    for i in a:
        if (i.isdigit())==False:
            return False
        b=int(i)
        if b<=255 and b>=0:
            continue
        return False
    return True
    # Write your code here.
    pass

from os import *
from sys import *
from collections import *
from math import *



def minNumToWin(n, mishaNum):
    mid=n//2
    if (mid>=mishaNum):
        return mishaNum+1
    else:
        return mishaNum-1


    # Write your Code here.

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import sys

def findSecondLargest(sequenceOfNumbers):
    a=set(sequenceOfNumbers)
    b=list(a)
    b.sort()
    if len(b)==1:
        return -1
    return b[-2]
    # Write your code here.
    pass
















# Taking input using fast I/O.
def takeInput():
    n = int(input())

    sequenceOfNumbers = list(map(int, input().strip().split(" ")))

    return sequenceOfNumbers, n

# Main.
t = int(input())
while t:
    sequenceOfNumbers, n = takeInput()
    print(findSecondLargest(sequenceOfNumbers))
    t = t-1

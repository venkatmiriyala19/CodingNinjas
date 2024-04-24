from os import *
from sys import *
from collections import *
from math import *

def fishEater(fishes):
    a=len(fishes)
    b=fishes[0]
    for i in range(1,a):
        if b>fishes[i]:
            a-=1
        else:
            b=fishes[i]
    return a
    # Write your code here.
    pass

# Main.
t = int(input())
for i in range(t):
    n = int(input())
    fishes = list(map(int,input().split()))
    print(fishEater(fishes))

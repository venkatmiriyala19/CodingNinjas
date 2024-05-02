from os import *
from sys import *
from collections import *
from math import *

def findShortestRoute(str):
    x=0
    y=0
    for i in str:
        if i=='E':
            x+=1
        if i=='W':
            x-=1
        if i=="N":
            y+=1
        if i=="S":
            y-=1
    s=''
    if x<0:
        if y>0:
            for i in range(y):
                s+='N'
        else:
            for i in range(-y):
                s+='S'
        for i in range(-x):
            s+='W'
    else:
        for i in range(x):
            s+='E'
        if y>0:
            for i in range(y):
                s+='N'
        else:
            for i in range(-y):
                s+='S'
        
    return s
    # Write your code here
    pass

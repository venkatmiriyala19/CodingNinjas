from os import *
from sys import *
from collections import *
from math import *

def addOneToNumber(arr):
    num=0
    for i in range(len(arr)):
        num=num*10+arr[i]
    # print(num)
    num+=1
    new=[]
    while(num>0):
        rem=num%10
        new.append(rem)
        num=num//10
    # print(new)
    new.reverse()
    return new
    #   Write your code here
    pass

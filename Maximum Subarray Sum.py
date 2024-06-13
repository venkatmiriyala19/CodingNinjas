from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :
    Max_sofar=0
    Max_endhere=0
    for num in arr:
        Max_endhere=max(num, Max_endhere+num) 
        Max_sofar=max(Max_sofar,Max_endhere)
	# Your code here
    # return the answer
    return Max_sofar































#taking inpit using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))

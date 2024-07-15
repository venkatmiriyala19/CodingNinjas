from os import *
from sys import *
from collections import *
from math import *


def splitString(string: str) -> bool:
    def checkVowels(string: str)-> int:
        count=0
        for i in range(len(string)):
            if string[i] in 'aeiouAEIOU':
                count+=1
        return count
    x=len(string)//2
    a=checkVowels(string[:x])
    b=checkVowels(string[x:])
    return a==b
    # Write your code here.
    pass

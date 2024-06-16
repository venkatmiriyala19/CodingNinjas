from os import *
from sys import *
from collections import *
from math import *

def checkMeta(str1, str2):
    freq1={}
    freq2={}
    for i in str1:
        if i in freq1:
            freq1[i]+=1
        else:
            freq1[i]=1
    for i in str2:
        if i in freq2:
            freq2[i]+=1
        else:
            freq2[i]=1
    count=0
    for i in range(len(str1)):
        if str1[i] not in str2:
            return False
        if freq1[str1[i]]!=freq2[str1[i]]:
            return False
        if str1[i]!=str2[i]:
            count+=1
    if count==2:
        return True
    return False
    # Write your code here.
    pass

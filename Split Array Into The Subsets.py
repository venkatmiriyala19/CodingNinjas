from os import *
from sys import *
from collections import *
from math import *

from typing import List


def isPossibleToSplit(n: int, arr: List[int]) -> bool:
    s=set()
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for i in freq:
        if freq[i]==1:
            return False
        else:
            s.add(freq[i])
    if len(s)==1:
        return True
    return False

    # write your code here
    pass

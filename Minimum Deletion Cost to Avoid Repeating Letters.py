from os import *
from sys import *
from collections import *
from math import *

from typing import List


def minimumCost(n: int, s: str, cost: List[int]) -> int:
    q=s[0]
    total=0
    maxi=0
    running=cost[0]
    y=False
    for i in range(0,n-1):
        if s[i]==s[i+1]:
            total+=cost[i]
            maxi=max(maxi,cost[i])
            y=True
            continue
        else:
            if (y==True):
                maxi=max(maxi,cost[i])
                total+=cost[i]
                total-=maxi
                maxi=0
                y=False
    if (y==True):
        maxi=max(maxi,cost[n-1])
        total+=cost[n-1]
        total-=maxi
        maxi=0
        y=False
            
           
    return total

    # write your code here
    pass

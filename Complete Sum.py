from sys import *
from collections import *
from math import *

from typing import *

def completeSum(a: List[int], n: int)-> List[int]:
    b=[]
    sum=0
    for i in a:
        sum+=i
        b.append(sum)
    return b

    # Write your Code here
    pass

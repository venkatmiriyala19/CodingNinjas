from os import *
from sys import *
from collections import *
from math import *



def sumOrProduct(n, q):
    if q==1:
        sum=n*(n+1)/2
        return int(sum)
    else:
        product=1
        for i in range(1,n+1):
            product*=i
        if len(str(product)) >= 9:
            product = (product % (10 ** 9 + 7))
        return product

    # Write your Code here.

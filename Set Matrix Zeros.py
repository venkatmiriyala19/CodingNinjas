from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
    b=len(matrix[0])
    row=set()
    column=set()
    for i in range(len(matrix)):
        for j in range(b):
            if matrix[i][j]==0:
                row.add(i)
                column.add(j)
    for i in range(len(matrix)):
        for j in range(b):
            if j in column or i in row:
                matrix[i][j]=0

	# Write your code here.
    pass

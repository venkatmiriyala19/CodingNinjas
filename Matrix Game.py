from os import *
from sys import *
from collections import *
from math import *

def matrixGame(mat):
    matrix=[]
    for i in range(len(mat)):
        temp=[]
        for j in range(len(mat[i])):
            temp.append(0)
        matrix.append(temp)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            for k in range(len(matrix)):
                matrix[i][j]+=mat[i][k]*mat[k][j]
    return matrix==mat


    # Write your Code Here.
    # Return a boolean variable 'True' or 'False'
    pass

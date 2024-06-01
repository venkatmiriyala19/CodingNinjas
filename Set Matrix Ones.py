from os import *
from sys import *
from collections import *
from math import *

def setMatrixOnes(MAT, n, m):
	row=set()
	col=set()
	for i in range(n):
		for j in range(m):
			if MAT[i][j]==1:
				row.add(i)
				col.add(j)
	for i in range(n):
		for j in range(m):
			if i in row or j in col:
				MAT[i][j]=1
	return MAT
	

	# Write your code here
	pass

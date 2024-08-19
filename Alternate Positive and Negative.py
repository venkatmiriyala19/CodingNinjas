from os import *
from sys import *
from collections import *
from math import *

def posAndNeg(arr):
	pos=[]
	neg=[]
	for i in arr:
		if i<0:
			neg.append(i)
		else:
			pos.append(i)
	res=[]
	for i in range(len(neg)):
		res.append(pos[i])
		res.append(neg[i])
	arr[:]=res
	return arr

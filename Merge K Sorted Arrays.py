from sys import *
from collections import *
from math import *

def mergeKSortedArrays(kArrays, k:int):
	a=[]
	for i in kArrays:
		a.extend(i)
	a.sort()
	return a
	# Write your code here.
	# kArrays is a list of 'k' lists.
	# Return a list.
	pass

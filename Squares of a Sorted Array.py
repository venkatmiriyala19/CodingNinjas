from os import *
from sys import *
from collections import *
from math import *

def sqsorted(arr):
	b=[]
	for i in arr:
		b.append(i*i)
	b.sort()
	return b
	# Write your code here.
	pass

from os import *
from sys import *
from collections import *
from math import *

def flipSomeBits(num, arr, n):
	for pos in arr:
		num=num^(1<<(pos-1))
	return num
			
	# Write your code here.
	pass

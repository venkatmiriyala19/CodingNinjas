from os import *
from sys import *
from collections import *
from math import *

def sumOfEvenOdd(num):
	even=0
	odd=0
	while(num>0):
		a=num%10
		if a%2==0:
			even+=a
		else:
			odd+=a
		num=num//10
	
	l=[even,odd]
	return l

	# Return a list of size 2 with even and odd sum respectively.
	# return [evenSum, oddSum]

	pass

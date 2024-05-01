from os import *
from sys import *
from collections import *
from math import *

def shakeHands(friends, n, k):
	for i in friends:
		if i==k:
			k+=k
	return k
	# Write your code here.
	pass

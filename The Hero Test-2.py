from os import *
from sys import *
from collections import *
from math import *

def theOrder(n, k):
	a=[]
	for i in range(1,n+1):
		a.append(i)
	b=[]
	i=0
	for j in range(n):
		i=(i+k)%len(a)
		b.append(a[i])
		a.remove(a[i])
	return b

			
	# Write your code here.
	pass

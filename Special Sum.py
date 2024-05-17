from os import *
from sys import *
from collections import *
from math import *

def specialSum(arr, n):
	spec_sum=[]
	tsum=sum(arr)
	isum=arr[0]
	jsum=arr[n-1]
	for i in range(len(arr)):
		if i==0:
			spec_sum.append(isum+jsum)
			continue
		isum+=arr[i]
		jsum+=arr[n-i-1]
		spec_sum.append(isum+jsum)
	# print(spec_sum)
	return min(spec_sum)




	# Write your code here. 
	pass

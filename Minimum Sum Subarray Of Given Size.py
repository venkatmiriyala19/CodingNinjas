from os import *
from sys import *
from collections import *
from math import *

def minSubarraySum(arr, n, k):
	window_sum=sum(arr[:k])
	min_sum=window_sum
	for i in range(n-k):
		window_sum=window_sum-arr[i]+arr[i+k]
		min_sum=min(min_sum,window_sum)
	return min_sum

	# Write your code here
	pass

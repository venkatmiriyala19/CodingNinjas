from os import *
from sys import *
from collections import *
from math import *

def checkPalindrome(s):
	s1=''
	s=s.lower()
	for i in s:
		if i in 'qwertyuiopasdfghjklzxcvbnm12347890':
			s1+=i
	return s1==s1[::-1]

    # Write your code here
	# Return a boolean
	pass

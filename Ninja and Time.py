def fenwickTree(arr, n):
	summer=[0]
	max=0;
	for i in range(1,n):
		max=0
		for j in range(i):
			if arr[j]>arr[i]:
				max+=arr[j]
		summer.append(max)
	return summer

def kthSmallLarge(arr, n, k):
    arr.sort()
    a=[]
    a.append(arr[k-1])
    a.append(arr[-k])
    return a
    # Write your code here
    pass

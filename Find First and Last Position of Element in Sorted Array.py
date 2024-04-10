def searchRange(arr: [int], x: int) -> [int]:
    if x not in arr:
        return [-1,-1]
    a=[]
    a.append(arr.index(x))
    n=len(arr)
    for i in range(1,n+1):
        if arr[-i]==x:
            a.append(n-i)
            break
    return a
    # Write your code here.
    pass

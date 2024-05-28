def getFloorAndCeil(a, n, x):
    # a=[]
    s=set(a)
    if x in s:
        return [x,x]
    for i in range(n):
        if a[i]>x and i!=0:
            return [a[i-1],a[i]]
        elif a[i]>x and i==0:
            return [-1,a[i]]
    return [a[-1],-1]
    # Write your code here.

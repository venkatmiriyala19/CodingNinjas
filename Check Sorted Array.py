def isSorted(n: int,  a: [int]) -> int:
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            return 0
    return 1
    # Write your code here.
    pass

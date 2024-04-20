def isKthBitSet(n: int, k: int) -> bool:
    a=bin(n)
    a=a[2:]
    a=a[::-1]
    if a[k-1]=='1':
    # print(a)
        return True
    return False

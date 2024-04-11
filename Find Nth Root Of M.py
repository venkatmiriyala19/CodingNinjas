def NthRoot(n: int, m: int) -> int:
    
    a=m**(1/n)    
    tolerance=1e-9
    if(abs(a-round(a))<tolerance):
        return round(a)
        # return -1
    return -1
    # Write Your Code Here
    pass

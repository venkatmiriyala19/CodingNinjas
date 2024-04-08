def median(a: int, b: int) -> float:
    a.extend(b)
    a.sort()
    b=len(a)
    c=b/2
    if b%2==0:
        c=int(c)
        return (a[c-1]+a[c])/2
    c=int(c)
    return float(a[c])
    # Write the function here.
    pass

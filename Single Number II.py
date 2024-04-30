def elementThatAppearsOnce(arr):
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for i in freq:
        if freq[i]==1:
            return i
    # Write your code here
    # Return the integer which appears only once.
    pass

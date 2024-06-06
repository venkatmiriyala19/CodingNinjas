from typing import List

def missingNumber(n: int, arr: List[int]) -> int:
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for i in freq:
        if freq[i]%2!=0:
            return i
    # Write your code here
    pass

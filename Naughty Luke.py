from typing import *

def getFinalGrid(a: List[List[int]], n: int) -> List[List[int]]:
    for i in range(n):
        a[i]=a[i][::-1]
    for i in range(n):
        for j in range(n):
            if a[i][j]==1:
                a[i][j]=0
            else:
                a[i][j]=1
    return a

    # Write your code here.
	

def rotateArray(arr: list, k: int) -> list:
    k=k%len(arr)
    arr=arr[k:]+arr[:k]
    # print(arr)
    return arr
    # Write your code here.
    pass

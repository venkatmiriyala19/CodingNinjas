def kthElement(arr1: [int], n: int, arr2: [int], m: int, k: int) -> int:
    arr3=arr1+arr2
    arr3.sort()
    return arr3[k-1]
    # Write your code from here.
    pass

def findPeakElement(arr: [int]) -> int:
    b=max(arr)
    for i in range(len(arr)):
        if arr[i]==b:
            return i

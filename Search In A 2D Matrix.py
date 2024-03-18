def searchMatrix(mat: [[int]], target: int) -> bool:
    for i in range(len(mat)):
        if target in mat[i]:
                return True
    return False

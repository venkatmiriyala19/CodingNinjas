from typing import List

def generateString(N: int) -> List[str]:
    def backtrack(current_string):
        if len(current_string)==N:
            res.append(current_string)
            return
        backtrack(current_string+'0')
        if not current_string or current_string[-1]=='0':
            backtrack(current_string+'1')
    res=[]
    backtrack("")
    return res
    # write your code here
    pass

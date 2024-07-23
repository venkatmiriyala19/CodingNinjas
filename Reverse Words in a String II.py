def reverseOrderWords(str):
    a=str.split(" ")
    s=a[-1]
    for i in range(2,len(a)+1):
        s=s+" "+a[-i]
    return s
        

    # Write your code here.
    pass

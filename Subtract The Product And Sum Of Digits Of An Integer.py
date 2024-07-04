def findProductSumDifference(n):
    a=n
    prod=1
    summ=0
    while(a!=0):
        rem=a%10
        prod*=rem
        summ+=rem
        a=a//10
    return prod-summ
    

    # Write your code here
    # The function returns the difference between the product and 
    # sum of the digits in the number
    pass

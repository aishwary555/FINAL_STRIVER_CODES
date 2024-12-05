def myPow(x,n):
    ans = 1.0
    for i in range(n):
        ans = ans * x
    return ans


print(myPow(2, 10))
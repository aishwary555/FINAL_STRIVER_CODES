def maxproduct(nums):
    
    maxi = float('-inf')
    n = len(nums)
    for i in range (n):
        for j in range (i,n):
            prod = 1
            for k in range (i, j+1):
                prod = prod * nums[k]
            
            maxi = max(maxi,prod)
    
    return maxi 

arr = [1, 2, -3, 0, 4, -5]
k = maxproduct(arr)
print (k)
def maxproduct(nums):
    
    maxi = float('-inf')
    n = len(nums)
    for i in range (n):
        prod = 1
        for j in range (i,n):

            prod = prod * nums[j]
            
            maxi = max(maxi,prod)
    
    return maxi 

arr = [-1,4,-5,-9,2,-7,-9]
k = maxproduct(arr)
print (k)
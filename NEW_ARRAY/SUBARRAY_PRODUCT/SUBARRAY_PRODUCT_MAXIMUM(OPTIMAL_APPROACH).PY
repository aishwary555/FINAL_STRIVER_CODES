
def maxProduct(nums):
    
        maxi = float('-inf')
        pre = 1
        suff = 1
        n = len(nums)
        for i in range (n):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1
            pre *= nums[i]
            suff *= nums[n-i-1]

            maxi = max(maxi,pre,suff)
        return maxi
    
arr = [-1,4,0,-5,-9,2,-7,-9]
k = maxProduct(arr)
print (k)
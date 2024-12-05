def nextgreatele(nums):
    
    
    n = len(nums)
    nge = [-1] *n
    for i in range(n):
        for j in range(i+1 , i+n):
            ind = j%n
            if(nums[ind] > nums[i]):
                nge[i] = nums[ind]
                break
    return nge

nums = [1,2,3,4,3]
res = nextgreatele(nums)
print(res)
                
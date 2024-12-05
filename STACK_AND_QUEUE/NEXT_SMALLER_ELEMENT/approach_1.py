def next_smaller_ele(nums):
    
    n = len(nums)
    nge = [-1] * n
    for i in range(n):
        for j in range(i+1 , n):
            if(nums[j] < nums[i]):
                nge[i] = nums[j]
                break
    return nge

s = [9,8,5,0,6,2]
res = next_smaller_ele(s)
print(res)
            
            
            
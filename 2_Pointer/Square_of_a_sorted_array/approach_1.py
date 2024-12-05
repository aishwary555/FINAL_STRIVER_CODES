def square_of_sorted_array(nums):
    
    n = len(nums)
    left = 0 
    right = n-1
    res = []
    
    while left <= right:
        if(abs(nums[left]) > abs(nums[right])):
            res.append(nums[left] ** 2)
            left += 1
        else:
            res.append(nums[right] ** 2)
            right -= 1
    
    res.reverse()
    
    return res

nums = [-4,-1,0,3,10]
res = square_of_sorted_array(nums)
print(res)
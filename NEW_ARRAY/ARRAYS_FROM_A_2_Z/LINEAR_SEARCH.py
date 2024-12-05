def linear(nums , key):
    
    for i in range(len(nums)):
        if key == nums[i]:
            return i
    
    return -1

nums = [213,6,5]
key = 6
result = linear(nums,key)
print(result)

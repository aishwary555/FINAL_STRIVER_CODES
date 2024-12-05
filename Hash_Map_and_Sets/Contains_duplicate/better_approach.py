def containsDuplicate(nums):
        
    n = len(nums)
    nums.sort()
    for i in range(n-1):
        if(nums[i] == nums[i+1]):
            return True
        
    return False

arr = [1,2,3,1]
res = containsDuplicate(arr)
print(res)
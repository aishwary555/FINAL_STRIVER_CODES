def containsDuplicate(nums):
        
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if(nums[i] == nums[j]):
                return True
    return False

arr = [1,2,3,1]
res = containsDuplicate(arr)
print(res)
def duplicate(nums):
    
    hash = set ()
    for num in nums:
        if num in hash:
            return True
        else:
            hash.add(num)
    return False

arr = [1,2,3,1]
res = duplicate(arr)
print(res)
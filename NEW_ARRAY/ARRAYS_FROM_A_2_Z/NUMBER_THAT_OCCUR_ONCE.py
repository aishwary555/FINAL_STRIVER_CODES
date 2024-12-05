def once_occur(nums):
    
    maxi = max(nums)
    hash = [0] * (maxi + 1)
    
    for num in nums:
        hash[num] += 1
        
    for i in nums:
        if hash[i] == 1:
            return i
   
    return -1

arr = [4, 1, 2, 1, 2]
ans = once_occur(arr)
print("The single element is:", ans)


    
    
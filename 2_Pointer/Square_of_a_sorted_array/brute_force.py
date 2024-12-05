def sortedSquares(nums):
        
    res = []
    for num in nums:
        res.append(num ** 2)
        
    res.sort()
    return res

nums = [-4,-1,0,3,10]
res = sortedSquares(nums)
print(res)
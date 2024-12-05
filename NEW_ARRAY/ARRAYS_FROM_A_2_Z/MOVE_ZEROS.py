
def moveZeroes(nums):
        
    temp = [0] * len(nums)
    n = len(nums)
    index = 0
    for i in range (len(nums)):
        if(nums[i] != 0):
            temp[index] = nums[i] 
            index = index+1
    for i in range(index,len(nums)):
        temp[i] = 0

    for u in range(len(nums)):
        nums[u] = temp[u]

    return nums
    
arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
ans = moveZeroes(arr)
for it in ans:
    print(it, end=" ")
print()
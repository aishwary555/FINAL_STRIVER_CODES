
def next( nums):
        
        n = len(nums)
        ind = -1

        for i in range(n-2,-1,-1):
            if(nums[i] < nums[i+1]):
                ind = i
                break
        
        if ind == -1:
            nums.reverse()
            return nums
        
        for i in range (n-1, ind,-1):
            if(nums[i] > nums[ind]):
                nums[i] , nums[ind] = nums[ind] , nums[i]
                break

        nums[ind+1:] = list(reversed(nums[ind+1:]))

        return nums
    
    

A = [1,2,3]
ans = next(A)
for it in ans:
    print(it, end=" ")

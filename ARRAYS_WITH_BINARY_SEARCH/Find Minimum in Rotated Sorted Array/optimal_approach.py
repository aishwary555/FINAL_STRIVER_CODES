def findMin(nums):
        
        ans = float('inf')
        n = len(nums)
        low = 0
        high = n - 1 
        while(low<=high):
            mid = (low + high)//2

            if(nums[low] <= nums[mid]):
                ans = min(ans , nums[low])
                low = mid + 1
            
            else:
                ans = min(ans , nums[mid])
                high = mid -1 
        return ans
    
arr = [4, 5, 6, 7, 9, 1, 2, 3]
ans = findMin(arr)
print("The minimum element is:", ans)


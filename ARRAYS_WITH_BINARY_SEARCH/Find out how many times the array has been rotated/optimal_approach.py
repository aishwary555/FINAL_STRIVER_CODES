def rotate(nums):
    
    n = len(nums)
    low = 0 
    high = n - 1
    index = -1
    ans = float('inf')
    
    while low <= high :
        mid = (low+high) // 2
        
        if(nums[low] <= nums[high]):
            if(nums[low] < ans):
                ans = nums[low]
                index = low
            break
        
        if(nums[low] <= nums[mid]):
            if(nums[low] < ans):
                ans = nums[low]
                index = low
            low = mid + 1 
        
        if(nums[mid] <= nums[high]):
            if(nums[mid] < ans):
                ans = nums[mid]
                index = mid 
            high = mid - 1 
        
    return index
    
arr = [3,4,5,1,2]
k = rotate(arr)
print(k)
                   
                
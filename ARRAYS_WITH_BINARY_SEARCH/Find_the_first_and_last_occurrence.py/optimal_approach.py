def search(nums, target):
        
        n = len(nums)
        low = 0
        high = n-1
        first = -1
        last = -1

        while low <= high:
            mid = (low+high) //2
            if(nums[mid] == target):
                first = mid
                high = mid-1
                
            elif(nums[mid] > target):
                high = mid-1
            else:
                low = mid+1
        
        low = 0 
        high = n-1
        
        
        while low <= high:
            mid = (low+high) //2
            if(nums[mid] == target):
                last = mid
                low = mid+1
                
            elif(nums[mid] > target):
                high = mid-1
            else:
                low = mid+1
                
        return [first,last]

arr = [5,7,7,8,8,10]
res = search(arr,8)
print(res)
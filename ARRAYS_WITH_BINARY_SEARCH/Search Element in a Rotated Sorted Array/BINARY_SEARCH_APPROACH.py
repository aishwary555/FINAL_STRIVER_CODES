
def search(nums , target):
        n = len(nums)
        high = n - 1
        low = 0
        while(low <= high):
            mid = (low + high)//2

            if(nums[mid] == target):
                return mid
            
            if(nums[low] <= nums[mid]):
                if(nums[low]<=target and target<=nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1

            else:
                if(nums[mid] <= target and target <= nums[high]):
                    low = mid + 1
                else:
                    high = mid -1 
        return -1
                
arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
k = 1
ans = search(arr, k)
if ans == -1:
    print("Target is not present.")
else:
    print("The index is:", ans)
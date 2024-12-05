def most_water(nums):
    
    n = len(nums)
    left = 0
    right = n-1
    area = 0
    
    while left <= right:
        widht = right-left
        height = min(nums[left],nums[right])
        
        area = max(area,widht*height)
        
        if(nums[left] < nums[right]):
            left += 1
        else: 
            right -= 1
    
    return area

height = [1,8,6,2,5,4,8,3,7]
res = most_water(height)
print(res)
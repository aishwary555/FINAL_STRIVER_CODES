def trapped_rainwater(height):
    
    maxleft = 0 
    maxright = 0
    res = 0
    n = len(height)
    left = 0 
    right = n-1
    
    while(left<=right):
        
        if(height[left] <= height[right]):
            if(height[left] >= maxleft):
                maxleft = height[left]
            else:
                res += maxleft - height[left]
            left += 1
                
        else:
            if(height[right] >= maxright):
                maxright = height[right]
            else:
                res += maxright - height[right]
            right -= 1
                
    return res


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
res = trapped_rainwater(arr)
print(res)
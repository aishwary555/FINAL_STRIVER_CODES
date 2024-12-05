def majority_ele(nums):
    
    candidate = None
    count = 0 
    
    for num in nums:
        
        if count == 0 :
            candidate = num
        if(num == candidate):
            count+=1
        else:
            count-=1
            
    return candidate


arr = [2,2,1,1,1,2,2]
res = majority_ele(arr)
print(res)
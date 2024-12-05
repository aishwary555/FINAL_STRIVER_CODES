def findMaxConsecutiveOnes(nums):
    
    count = 0
    i = 0
    max_count = 0
    while i<len(nums):
        if(nums[i]==1):
            count+=1  
            i=i+1      
        else:
            count = 0 
            i=i+1
        

        max_count = max(max_count,count)

    return max_count 

arr = [1,1,1,0,0,1,1,1,1,1,1,0]
result = findMaxConsecutiveOnes(arr)
print(result)
                
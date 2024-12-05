def next_greater_elements(num1,num2):
    
    result = []
    for num in num1:

        next_greater_ele = -1
        index = num2.index(num)
        for i in range(index+1,len(num2)):
            if(num2[i] > num):
                next_greater_ele = num2[i]
                break
        result.append(next_greater_ele)
    return result
            
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(next_greater_elements(nums1, nums2)) 
        
        
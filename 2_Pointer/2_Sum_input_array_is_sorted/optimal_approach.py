def twoSum(numbers, target):
        
    n = len(numbers)
    left = 0 
    right = n-1

    while left <= right:
        if(numbers[left]+numbers[right] == target):
            return [left+1,right+1]
        elif(numbers[left]+numbers[right] > target):
            right -= 1
        else:
            left += 1
    return -1

numbers = [2,7,11,15]
res = twoSum(numbers,9)
print(res)
        
        
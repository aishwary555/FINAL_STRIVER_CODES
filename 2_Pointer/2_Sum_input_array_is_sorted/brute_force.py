def twoSum(numbers, target):
        
        n = len(numbers)
        for i in range(n-1):
            for j in range(i+1,n):
                if(numbers[i] + numbers[j] == target):
                    return [i+1,j+1]

numbers = [2,7,11,15]
res = twoSum(numbers,9)
print(res)    
            
        
        
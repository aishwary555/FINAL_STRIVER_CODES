import math
def summ(arr,limit):
    
    n = len(arr)
    for d in range(1,max(arr)+1):
        summs = 0
        for i in range(n):
            summs = summs + math.ceil(arr[i]/d)
        if(summs <= limit):
            return d 
    return -1 

arr = [44,22,33,11,1]
limit = 5
ans = summ(arr, limit)
print("The minimum divisor is:", ans)
            
        





def subarray_min(arr):
    
    n = len(arr)
    sum = 0
    for i in range(n):
        mini = arr[i]
        for j in range(i,n):
            mini = min(mini , arr[j])
            sum += mini 
        
    return sum

arr = [3,1,2,4]
res = subarray_min(arr)
print(res)
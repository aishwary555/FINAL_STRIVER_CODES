def trapping_rainwater(arr):
    
    n = len(arr)
    maxpre = [0]*n
    maxsuf = [0]*n
    
    maxpre[0] = arr[0]
    for i in range(1,n):
        maxpre[i] = max(maxpre[i-1] , arr[i])
    
    maxsuf[n-1] = arr[n-1]
    for i in range (n-2,-1,-1):
        maxsuf[i] = max(maxsuf[i+1],arr[i])
    
    watertrapped = 0
    for i in range(n):
        watertrapped += min(maxpre[i],maxsuf[i]) - arr[i]
    
    return watertrapped

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
res = trapping_rainwater(arr)
print(res)
            
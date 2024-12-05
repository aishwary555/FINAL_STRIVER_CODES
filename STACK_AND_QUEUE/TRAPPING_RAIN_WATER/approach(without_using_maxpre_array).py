def trapping_rain_water(arr):
    
    n = len(arr)
    maxsuf = [0]*n
    
    maxsuf[n-1] = arr[n-1]
    for i in range(n-2,-1,-1):
        maxsuf[i] = max(maxsuf[i+1] , arr[i])
    
    watertrapped = 0 
    leftmax = arr[0]
    
    for i in range(n):
        leftmax = max(leftmax,arr[i])
        watertrapped += min(leftmax,maxsuf[i]) - arr[i]
    
    return watertrapped

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
res = trapping_rain_water(arr)
print(res)
    
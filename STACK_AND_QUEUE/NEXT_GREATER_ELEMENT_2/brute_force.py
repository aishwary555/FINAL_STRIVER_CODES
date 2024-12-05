def nextgreat(arr):
    
    n = len(arr)
    nge = [-1] * n
    for i in range(n):
        
        for j in range(i+1,n):
            if(arr[j] > arr[i]):
                nge[i] = arr[j]
                break
                
        if(nge[i] == -1):
            for j in range(0,i):
                if(arr[j] > arr[i]):
                    nge[i] = arr[j]
                    break
                
        
        
    return nge

nums = [1,2,3,4,3]
res = nextgreat(nums)
print(res)

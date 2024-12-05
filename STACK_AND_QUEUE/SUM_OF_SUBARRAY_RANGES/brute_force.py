def sum_subarray_ranges(arr):
    
    n = len(arr)
    res = 0
    for i in range(n):
        mini = arr[i]
        maxi = arr[i]
        for j in range(i,n):
            mini = min(mini,arr[j])
            maxi = max(maxi,arr[j])
            res += maxi - mini
    return res

arr = [1,4,3,2]
res = sum_subarray_ranges(arr)
print(res)
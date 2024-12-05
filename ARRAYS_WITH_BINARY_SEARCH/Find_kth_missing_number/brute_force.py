def kth_missing(arr,k):
    
    n = len(arr)
    for i in range(n):
        if(arr[i] <= k):
            k += 1
        else:
            break
    return k

arr = [4, 7, 9, 10]
k = 4
ans = kth_missing(arr,k)
print("The missing number is:", ans)
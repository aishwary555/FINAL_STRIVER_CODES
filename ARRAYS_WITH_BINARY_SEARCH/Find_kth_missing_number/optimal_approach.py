def k_thmissing(arr,k):
    
    n =len(arr)
    low = 0 
    high = n-1
    
    while low <= high:
        mid = (low+high) //2
        missing_numbers = arr[mid] - (mid+1)
        if(missing_numbers < k):
            low = mid + 1
        else:
            high = mid - 1
    return k+high+1

vec = [4, 7, 9, 10]
k = 6
ans = k_thmissing(vec,k)
print("The missing number is:", ans)
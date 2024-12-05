import math
def summition(arr,div):
    summ = 0
    n = len(arr)
    for i in range(n):
        summ += math.ceil(arr[i]/div)
    return summ

def smallest_divisor(arr,limit):
    
    low = 1
    high = max(arr)
    ans = -1
    
    while low <= high:
        mid = (low+high) // 2
        total = summition(arr,mid)
        if(total <= limit):
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans 


arr = [44,22,33,11,1]
limit = 5
ans = smallest_divisor(arr, limit)
print("The minimum divisor is:", ans)
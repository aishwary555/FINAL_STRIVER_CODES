def miss(nums):
    
    n = len(nums)
    v = [-1] * (n+1)            #her n+1 because n are the total numbers in array and 1 is for the missing element 
    
    for num in nums:
        v[num] = num
        
    for i in range(len(v)):
        if v[i]==-1:
            return i
    return 0

arr = [0,1,3]
k = miss(arr)
print(k)


def miss_sum(arr):
    
    sums = sum(arr)
    n = len(arr)
    t_sum = (n*(n+1))/2
    result = t_sum - sums
    return result

arr = [0,1,2,3,4,5,6,8]
m = miss_sum(arr)
print(m)

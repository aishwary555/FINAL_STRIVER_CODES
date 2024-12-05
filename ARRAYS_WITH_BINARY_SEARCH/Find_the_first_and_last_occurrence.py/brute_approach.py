def first_and_last(arr,target):
    
    last = -1 
    first = -1 
    n = len(arr)
    for i in range(n):
        if(arr[i] == target):
            if(first == -1):
                first = i
            last = i     #  last will be updated always in each loop iteration
    
    return first,last

arr = [2,4,6,8,8,8,11,13]
target = 8
res = first_and_last(arr,target)
print(res)
            
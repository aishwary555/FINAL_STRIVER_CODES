def occur(arr):
    
    hashmap = {}
    
    for num in arr:
        
        if num in hashmap:
            hashmap[num] += 1 
        else:
            hashmap[num] = 1
        
    for num,count in hashmap.items():
        if(count == 1):
            return num
    return -1

arr = [0, 9999999, 1, 1, 0]
ans = occur(arr)
print("The single element is:", ans)
def arr_union(arr1,arr2):
    
    i = 0
    j = 0
    union = []
    while i<len(arr1) and j<len(arr2):
        if(arr1[i]<arr2[j]):
            if(len(union) == 0 or arr1[i] != union[-1]):
                union.append(arr1[i])
            i =i+1
        
        else:
            if(len(union) == 0 or arr2[j] != union[-1]):
                union.append(arr2[j])
            j = j+1
                
    while i<len(arr1):
        if(union[-1]  !=  arr1[i] ):
            union.append(arr1[i])
        i = i+1
            
    while j<len(arr2):
        if(union[-1]  !=   arr2[j] ):
            union.append(arr2[j])    
        j = j+1    
    
    return union



arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

result = arr_union(arr1, arr2)

print(result)

                
                
            
            
    
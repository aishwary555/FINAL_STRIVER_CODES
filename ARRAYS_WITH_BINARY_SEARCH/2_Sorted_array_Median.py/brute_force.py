def median(a , b):
    n1 = len(a)
    n2 = len(b)
    i = 0 
    j = 0
    arr3 = []
    while i<n1 and j<n2:
        if(a[i]<b[j]):
            arr3.append(a[i])
            i = i+1
        else:
            arr3.append(b[j])
            j = j+1
    
    while i<n1:
        arr3.append(a[i])
        i = i+1
    
    while j<n2:
        arr3.append(b[j])
        j = j+1
        
    
    n = n1 + n2
    if(n % 2 == 1):
        return float(arr3[n//2])
    else:
        return (arr3[n//2] + arr3[(n//2)-1])/ 2.0


a = [1,3, 4, 7, 10, 12]
b = [2, 3, 6, 15]
res = median(a,b)
print(res)

print()
c = [1,3,4]
d = [2,3]
k = median(c,d)
print(k)

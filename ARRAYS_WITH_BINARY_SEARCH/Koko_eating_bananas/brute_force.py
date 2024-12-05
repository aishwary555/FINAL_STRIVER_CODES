import math

def finding_k(arr,h):
    
    n = len(arr)
    for i in range(1,max(arr)+1):
        res = koko_eating_bananas(arr,i)
        if(res <= h):
            return i

def koko_eating_bananas(arr,div):
    
    n = len(arr)
    summ = 0 
    for i in range(n):
        summ += math.ceil(arr[i]/div)
    return summ


arr = [30,11,23,4,20]
h = 6
result = finding_k(arr,h)
print(result)
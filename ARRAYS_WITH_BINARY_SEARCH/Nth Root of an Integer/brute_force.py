def nth(N , M):
    
    res = 0
    for i in range (M):
        
        res = pow(i,N)
        if(res == M):
            return i 
        else:
            if(res > M):
                return -1
            

k = nth(4,625)
print(k)

    
                
        
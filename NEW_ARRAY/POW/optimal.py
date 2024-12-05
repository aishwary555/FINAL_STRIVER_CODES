def myPow(x, n):        
        ans = 1.0
        nn = n
        if nn<0:
            nn = -1 * nn
        
        while nn > 0 :
            if(nn%2==1):
                ans = ans * x
                nn = nn -1 
            else:
                x = x * x
                nn = nn // 2
            
        if(n < 0):
            return 1/ans
        return ans   
    
print(myPow(3,4))     
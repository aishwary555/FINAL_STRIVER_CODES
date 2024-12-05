
def solve(A, B):
        
        n = len(A)
        count = 0 
        for i in range(n):
            xorr = 0
            for j in range (i,n):
                xorr = xorr ^ A[j]
            
                if xorr == B:
                    count+=1   
        return count 


a = [4, 2, 2, 6, 4]
k = 6
ans = solve(a, k)
print("The number of subarrays with XOR k is:", ans)

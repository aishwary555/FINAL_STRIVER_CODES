def nCr(n,r):
    
    res = 1
    for i in range(r):
        res = res*(n-i)
        res = res//(i+1)
    return res

def pascals_triangle_line(n):
    
    for c in range(1,n+1):
        print(nCr(n-1,c-1), end = " ")
    print()
    
n = 5
result = pascals_triangle_line(n)
print(result)
def nCr(n,r):
    
    res = 1
    for i in range(r):
        res = res*(n-i)
        res = res // (i+1)
    return res

def pascals_triangle(r,c):
    ele = nCr(r-1,c-1)
    return ele 

r = 5
c = 3
result = pascals_triangle(5,3)
print(result)
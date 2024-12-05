def nCr(n,r):
    
    res = 1
    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)
    return res

def pascals_triangle(n):
    res = []
    for row in range(1,n+1):
        temp = []
        for col in range(1,row+1):
            temp.append(nCr(row-1,col-1))
        res.append(temp)
    return res

n = 5
ans = pascals_triangle(n)

for it in ans :
    for ele in it:
        print(ele,end= " ")
    print()
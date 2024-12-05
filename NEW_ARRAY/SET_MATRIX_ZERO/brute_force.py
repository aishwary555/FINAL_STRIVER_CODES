def row_zero(matrix,n,m,i):
    
    for j in range(m):
        if(matrix[i][j] != 0):
            matrix[i][j] = -1
    

def column_zero(matrix,n,m,j):
    
    for i in range(n):
        if(matrix[i][j] != 0):
            matrix[i][j] = -1


def setmatrix_zero(matrix,n,m):
    
    for i in range(n):
        for j in range(m):
            if(matrix[i][j] == 0):
                row_zero(matrix,n,m,i)
                column_zero(matrix,n,m,j)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    return matrix      
            

matrix = [[1,1,1],[1,0,1],[1,1,1]]
n = len(matrix)
m = len(matrix[0])

ans = setmatrix_zero(matrix,n,m)
for it in ans:
    for ele in it:
        print(ele, end = " ")
    print()

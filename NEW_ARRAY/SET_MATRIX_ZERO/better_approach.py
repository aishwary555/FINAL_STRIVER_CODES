def set_matrix_zero(matrix,n,m):
    
    row_arr = [0]*n
    col_arr = [0]*m
    
    for i in range(n):
        for j in range(m):
            if(matrix[i][j] == 0):
                row_arr[i] = 1
                col_arr[j] = 1
    
    for i in range(n):
        for j in range(m):
            if(row_arr[i] == 1 or col_arr[j] == 1 ):
                matrix[i][j] = 0
    return matrix

matrix = [[1,1,1],[1,0,1],[1,1,1]]
n = len(matrix)
m = len(matrix[0])

ans = set_matrix_zero(matrix,n,m)
for it in ans:
    for ele in it:
        print(ele, end = " ")
    print()
            
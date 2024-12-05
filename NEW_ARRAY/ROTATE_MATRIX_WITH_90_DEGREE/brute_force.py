def rotate_by_90(matrix):
    
    n = len(matrix)
    m = len(matrix[0])
    ans = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            ans[j][n-i-1] = matrix[i][j]
    return ans 

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
res = rotate_by_90(matrix)
for it in res:
    for ele in it:
        print(ele,end = " ")
    print()
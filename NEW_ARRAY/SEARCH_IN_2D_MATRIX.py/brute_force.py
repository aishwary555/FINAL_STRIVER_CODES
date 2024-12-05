def searchMatrix(matrix, target):
        
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if(matrix[i][j] == target):
                    return True
        
        return False

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = searchMatrix(matrix, 8)
print(result)
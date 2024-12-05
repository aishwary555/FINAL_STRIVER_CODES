def searchElement(matrix, target):
        
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if(matrix[i][j] == target):
                    return True
        
        return False

matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

result = searchElement(matrix, 70)
print("true" if result else "false")
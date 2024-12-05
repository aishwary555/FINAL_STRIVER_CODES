def isvalidsudoku(board):
    
    #validating Rows 
    
    for i in range(9):
        s = set()
        for j in range(9):
            item = board[i][j]
            if item != '.':
                if item in s or not ('1' <= item <= '9'):
                    return False
                s.add(item)

    #Validating Columns
    
    for i in range(9):
        s = set()
        for j in range(9):
            item = board[j][i]
            if item != '.':
                if item in s or not ('1' <= item <= '9'):
                    return False
                s.add(item)
                
    starts = [
    (0, 0), (0, 3), (0, 6),  # Top row sub-boxes
    (3, 0), (3, 3), (3, 6),  # Middle row sub-boxes
    (6, 0), (6, 3), (6, 6)   # Bottom row sub-boxes
    ]
    
    for i,j in starts:
        si = set()
        for row in range(i,i+3):
            for col in range(j,j+3):
                item = board[row][col]
                if item != '.':
                    if item in si or not ('1' <= item <= '9'):
                        return False
                    si.add(item)
    return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

res = isvalidsudoku(board)
print(res)
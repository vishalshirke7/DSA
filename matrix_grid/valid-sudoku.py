"""
https://leetcode.com/problems/valid-sudoku/
"""

def isValidSudoku(board):
    seen = dict()
    for index_i in range(9):
        for index_j in range(9):
            if board[index_i][index_j] != '.':
                char = int(board[index_i][index_j])
                if (char, index_j) in seen or (char, index_i) in seen or (char, index_i // 3, index_j // 3) in seen:
                    print(seen, (char, index_i), (char, index_j), (char, index_i // 3, index_j // 3))
                    return False
                seen[(char, index_i)] = 1
                seen[(char, index_j)] = 1
                seen[(char, index_i // 3, index_j // 3)] = 1
    return True


print('Output', isValidSudoku([["5","3",".",".","7",".",".",".","."]
                              ,["6",".",".","1","9","5",".",".","."]
                              ,[".","9","8",".",".",".",".","6","."]
                              ,["8",".",".",".","6",".",".",".","3"]
                              ,["4",".",".","8",".","3",".",".","1"]
                              ,["7",".",".",".","2",".",".",".","6"]
                              ,[".","6",".",".",".",".","2","8","."]
                              ,[".",".",".","4","1","9",".",".","5"]
                              ,[".",".",".",".","8",".",".","7","9"]]))
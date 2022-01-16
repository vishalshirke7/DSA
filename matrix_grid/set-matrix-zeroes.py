"""
https://leetcode.com/problems/set-matrix-zeroes/
https://www.interviewbit.com/old/problems/set-matrix-zeros/
"""


def setZeroes(matrix):
    is_first_row, is_first_column = 0, 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == 0:
                if row == 0:
                    is_first_row = 1
                if column == 0:
                    is_first_column = 1
                matrix[row][0] = 0
                matrix[0][column] = 0

    for row in range(1, len(matrix)):
        for column in range(1, len(matrix[row])):
            if matrix[row][0] == 0 or matrix[0][column] == 0:
                matrix[row][column] = 0
    if is_first_row:
        for column in range(len(matrix[0])):
            matrix[0][column] = 0
    if is_first_column:
        for row in range(len(matrix)):
            matrix[row][0] = 0


def setZeroes(A):
    row, columns = set(), set()
    for index_i in range(len(A)):
        for index_j in range(len(A[index_i])):
            if A[index_i][index_j] == 0:
                row.add(index_i)
                columns.add(index_j)
    for index_i in range(len(A)):
        for index_j in range(len(A[index_i])):
            print(index_i, index_j)
            if index_i in row:
                A[index_i][index_j] = 0
            if index_j in columns:
                A[index_i][index_j] = 0
    print(A)


print('Output', setZeroes([[0,0], [1,0]]))    
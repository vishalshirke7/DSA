"""
https://leetcode.com/problems/search-a-2d-matrix/
https://www.interviewbit.com/old/problems/matrix-search/
"""

# own
def searchMatrix(A, B):
    row_len, column_len = len(A), len(A[0])
    start, end = 0, (row_len * column_len) - 1
    while start <= end:
        mid = (start + end) // 2
        row, column = mid // column_len, mid % column_len
        if A[row][column] == B:
            return 1
        if A[row][column] > B:
            end = mid - 1
        else:
            start = mid + 1
    return 0
    
def searchMatrix(matrix, target):
	start, end = 0, len(matrix) * len(matrix[0]) - 1
	total_columns = len(matrix[0])
	while start <= end:
		mid = (start + end) // 2
		row, column = mid // total_columns, mid % total_columns
		if matrix[row][column] == target:
			return True
		if matrix[row][column] > target:
			end = mid - 1
		else:
			start = mid + 1
	return False


print('Output', searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))	
print('Output', searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))	
print('Output', searchMatrix([[1,1,1,1],[11,11,11,11]], 1))


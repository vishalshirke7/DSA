"""
https://www.interviewbit.com/old/problems/maximum-sum-square-submatrix/
"""

# OWN 
def solve(A, B):
	matrix_size = len(A)
	for row in range(matrix_size):
		for column in range(1, matrix_size):
			A[row][column] += A[row][column - 1]				
	max_sum = -float('inf')
	for index in range(matrix_size - B + 1):
		for column in range(B - 1, matrix_size):
			cur_sum = 0
			for row in range(index, index + B):
				if column >= B:
					cur_sum += (A[row][column] - A[row][column - B])
				else:
					cur_sum += A[row][column]
			max_sum = max(max_sum, cur_sum)
	return max_sum

print('Output', solve([
        [1, 1, 1, 1, 1]
        ,[2, 2, 2, 2, 2]
        ,[3, 8, 6, 7, 3]
        ,[4, 4, 4, 4, 4]
        ,[5, 5, 5, 5, 5]
     ], 3))	
print('Output', solve([[2,2], [2,2]], 2))	

def valid(i, j, n):
    return (i>=0 and i<n and j>=0 and j<n)
    
def solve(self, A, B):
    n=len(A)
    if n==0:
        return 0
    ans=-10000000
    for i in range(n):
        for j in range(n):
            if valid(i-1, j, n):
                A[i][j]+=A[i-1][j]
            if valid(i, j-1, n):
                A[i][j]+=A[i][j-1]
            if valid(i-1, j-1, n):
                A[i][j]-=A[i-1][j-1]
    
    for i in range(n):
        for j in range(n):
            if i==B-1 and j==B-1:
                ans=max(ans, A[i][j])
            if i==B-1 and j-B>=0:
                curarea=A[i][j]-A[i][j-B]
                ans=max(ans, curarea)
            if j==B-1 and i-B>=0:
                curarea=A[i][j]-A[i-B][j]
                ans=max(ans, curarea)
            if valid(i-B, j-B, n):
                curarea=A[i][j]-A[i-B][j]-A[i][j-B]+A[i-B][j-B]
                ans=max(ans, curarea)
    return ans

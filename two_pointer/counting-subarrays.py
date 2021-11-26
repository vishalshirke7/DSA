"""
https://www.interviewbit.com/problems/counting-subarrays/
"""


def solve(A, B):
	count = 0
	cur_sum = 0
	start, end = 0, 0
	while end < len(A):
		cur_sum += A[end]
		while start <= end and cur_sum >= B:
			cur_sum -= A[start]
			start += 1
		count += end - start + 1
		end += 1
	return count



print('Output', solve([1, 11, 2, 3, 15], 10))
print('Output', solve([2, 5, 6], 10))
print('Output', solve([ 8, 5, 1, 10, 5, 9, 9, 3, 5, 6, 6, 2, 8, 2, 2, 6, 3, 8, 7, 2, 5, 3, 4, 3, 3, 2, 7, 9, 6, 8, 7, 2, 9, 10, 3, 8, 10, 6, 5, 4, 2, 3, 4, 4, 5, 2, 2, 4, 9, 8, 5 ], 32))
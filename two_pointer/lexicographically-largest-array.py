"""
https://www.interviewbit.com/problems/lexicographically-largest-array/
"""


def solve(A):
	index = 1
	cur_ptr = len(A) - 1
	last_seen = len(A) - 1
	while index <= cur_ptr:
		if A[cur_ptr] > A[cur_ptr - index]:
			last_seen = cur_ptr - index
		index += 1
	if last_seen == cur_ptr:
		return A
	else:
		start, end = last_seen, len(A) - 1 
		while start < end:
			A[start], A[end] = A[end], A[start]
			start += 1
			end -= 1
	return A

print('Output', solve([10, 20, 30, 40]))
print('Output', solve([40, 30, 20, 10]))
print('Output', solve([4, 1, 3, 2]))
print('Output', solve([4, 2, 1, 3, 10]))
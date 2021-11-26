"""
https://www.interviewbit.com/old/problems/triplets-with-sum-between-given-range/
"""


def solve(A):
	range_A, range_B, range_C = list(), list(), list()
	for val in A:
		if 0 < val < 2/3:
			range_A.append(val)
		elif 2/3 < val < 1:
			range_B.append(val)
		elif 1 < val < 2:
			range_C.append(val)
	first_min_C = float('inf')
	first_min_B, second_min_B = float('inf'), float('inf')
	first_min_A, second_min_A = float('inf'), float('inf')
	first_max_A, second_max_A, third_max_A = -float('inf'), -float('inf'), -float('inf')
	for index in range(len(range_A)):
		if range_A[index] > first_max_A:
			first_max_C = first_max_B
			first_max_B = first_max_A
			first_max_A = range_A[index]
		elif range_A[index] > first_max_B:
			first_max_C = first_max_B
			first_max_B = range_A[index]
		elif range_A[index] > first_max_C:
			first_max_C = range_A[index]
		if range_A[index] < first_min_A:
			second_min_A = first_min_A
			first_min_A = range_A[index] 
		elif range_A[index] < second_min_A:
			second_min_A = range_A[index]
	for index in range(len(range_B)):
		if range_A[index] < first_min_B:
			second_min_B = first_min_B
			first_min_B = range_A[index] 
		elif range_A[index] < second_min_B:
			second_min_B = range_A[index]
	for index in range(len(range_C)):
		if range_A[index] < first_min_C:
			first_min_C = range_A[index]
	if 1 < (first_max_A + second_max_A + third_max_A) < 2
		return 1
	elif 
print('Output', solve([0.6, 0.7, 0.8, 1.2, 0.4]))
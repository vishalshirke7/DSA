"""
https://www.interviewbit.com/problems/intersection-of-sorted-arrays/
"""

# O(m + n)
def intersect(A, B):
	A_len, B_len = len(A), len(B)
	ptr_A, ptr_B, output = 0, 0, list() 
	while ptr_A < A_len and ptr_B < B_len:
		if A[ptr_A] == B[ptr_B]:
			output.append(A[ptr_A])
			ptr_A += 1
			ptr_B += 1
		elif A[ptr_A] < B[ptr_B]:
			ptr_A += 1
		else:
			ptr_B += 1
	return output


print('Output', intersect([1,2,3,3,4,5,6], [3,5]))
print('Output', intersect([1,2,3,3,4,5,6], [3,3,5]))
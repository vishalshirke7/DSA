"""
https://www.geeksforgeeks.org/sort-array-converting-elements-squares/
"""

# Two pointer
def solve(A):
	start, end = 0, len(A) - 1
	output = list()
	while start <= end:
		start_sq = A[start] * A[start]
		end_sq = A[end] * A[end]
		if start_sq >= end_sq:
			output.append(start_sq)
			start += 1
		else:
			output.append(end_sq)
			end -= 1
	return output[::-1]


# divide and merge
def solve(A):


	
print('Output', solve([-6,-3,-1,2,4,5]))
print('Output', solve([-5, -4, -2, 0, 1]))

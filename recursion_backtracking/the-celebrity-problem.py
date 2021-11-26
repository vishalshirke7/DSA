"""
https://www.geeksforgeeks.org/the-celebrity-problem/
"""
# TWO POINTER

def celebrity(M, n):
	candidate = -1
	start, end = 0, n - 1
	while start < end:
		print(start, end, M[end][start])
		if M[end][start] == 1:
			end -= 1
		else:
			start += 1
	candidate = start
	for index in range(n):
		if candidate != index:
			if M[candidate][index] == 1 or M[index][candidate] == 0:
				return -1
	return candidate

print('Output', celebrity([[0, 0, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 1, 0]], 4))
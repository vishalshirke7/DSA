"""
https://www.interviewbit.com/old/problems/find-permutation/
"""

def findPerm(A, B):
	start, end = 1, A
	output = list()
	for char in B:
		if char == 'I':
			output.append(start)
			start += 1
		else:
			output.append(end)
			end -= 1					
	output.append(start)
	return output


print('Output', findPerm(10, 'IIDDIDIID'))	

# 1 2 10 9 3 8 4 5 7 6
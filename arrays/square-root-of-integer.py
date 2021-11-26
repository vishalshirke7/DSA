"""
https://www.interviewbit.com/old/problems/square-root-of-integer/

"""

def sqrt(A):
    x = 0
    base = 10**3
    while base>0:
        while (x+base)**2<=A: x+= base
        base //= 2
    return x

def sqrt(A):
	if A <= 3:
		return 1
	start, end = 1, A // 2
	while start <= end:
		mid = (start + end) // 2
		square = mid * mid
		if square == A:
			return mid
		elif square < A:
			start = mid + 1
		else:
			end = mid - 1
	return start - 1



print('Output', sqrt(66))	
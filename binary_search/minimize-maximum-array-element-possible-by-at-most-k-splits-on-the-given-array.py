"""
https://www.geeksforgeeks.org/minimize-maximum-array-element-possible-by-at-most-k-splits-on-the-given-array/
"""

# O(N * log M), M - maximum element
def possible(A, N, mid, K):
	count = 0
	print('mid', mid)
	for i in range(N):
		count += (A[i] - 1) // mid
		print('count', count)
	return count <= K

def minimumMaximum(A, N, K):
	lo, hi = 1, max(A)
	while (lo < hi):
		mid = (lo + hi) // 2
		if (possible(A, N, mid, K)):
			hi = mid
		else:
			lo = mid + 1
	return hi


arr = [ 2, 4, 8, 2 ]
K = 4
N = len(arr)
print(minimumMaximum(arr, N, K))

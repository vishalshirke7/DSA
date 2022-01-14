"""
https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
"""
# Recursion
def knapSack(W, wt, val, n):
	if n == 0 or W == 0:
		return 0
	if (wt[n-1] > W):
		return knapSack(W, wt, val, n-1)
	else:
		return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
					knapSack(W, wt, val, n-1))


# O(N * W)
# Recursion + Memoization, Top Down
def knapSack(W, wt, val, n, cache):
	if n == 0 or W == 0:
		return 0
	if cache[n][W] != -1:
		return cache[n][W]
	if (wt[n-1] > W):
		cache[n][W] = knapSack(W, wt, val, n-1, cache)
	else:
		cache[n][W] = max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1, cache),
					knapSack(W, wt, val, n-1, cache))
	return cache[n][W]

# Bottom Up
def knapSack(W, wt, val, n):
	K = [[0 for x in range(W + 1)] for x in range(n + 1)]

	for i in range(n + 1):
		for w in range(W + 1):
			if i == 0 or w == 0:
				K[i][w] = 0
			elif wt[i-1] <= w:
				K[i][w] = max(val[i-1]
						+ K[i-1][w-wt[i-1]],
							K[i-1][w])
			else:
				K[i][w] = K[i-1][w]

	return K[n][W]

#Driver Code
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
cache = [[-1 for j in range(W + 1)] for index in range(n + 1) ]
print(knapSack(W, wt, val, n, cache))
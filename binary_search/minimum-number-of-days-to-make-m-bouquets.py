"""
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
"""

#discuss 
def minDays(bloomDay, m, k):
	if m*k > len(bloomDay):
		return -1
	left, right = 1, max(bloomDay)
	while left < right:
		flowers = bouquets = 0
		mid = (left + right) // 2
		for day in bloomDay:
			flowers = flowers + 1 if day <= mid else 0
			if flowers >= k:
				bouquets += 1
				flowers = 0
				if bouquets == m:
					break
		if bouquets == m:
			right = mid
		else:
			left = mid + 1
	return left


print('Output', minDays([1,10,3,10,2], 3, 1))	
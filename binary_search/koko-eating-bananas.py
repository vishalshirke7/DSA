"""
https://leetcode.com/problems/koko-eating-bananas/
"""

def checkEatingHours(piles, k):
	hour_count = 0
	for pile in piles:
		hour_count += (pile) // k
		if pile % k != 0:
			hour_count += 1
	return hour_count

def minEatingSpeed(piles, h):
	left, right = 1, max(piles)
	while left <= right:
		mid = (left + right) // 2
		if checkEatingHours(piles, mid) <= h:
			right = mid - 1
		else:
			left = mid + 1
	return left


print('Output', minEatingSpeed([30,11,23,4,20], 5))	
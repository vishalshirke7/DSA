"""
https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
"""


import math

#own O(NlogM) where M = max(A)
def smallestDivisor(nums, threshold):
	left, right = 1, sum(nums)
	while left < right:
		result = 0
		mid = (left + right) // 2
		for val in nums:
			result += math.ceil(val/mid)
		if result <= threshold:
			right = mid
		else:
			left = mid + 1
	return left

print('Output', smallestDivisor([1,2,5,9], 6))
print('Output', smallestDivisor([44,22,33,11,1], 5))
print('Output', smallestDivisor([21212,10101,12121], 1000000))
print('Output', smallestDivisor([2,3,5,7,11], 11))

"""
https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/
"""


# Discuss 
def minimumSize(nums, maxOperations):
	left, right = 1, max(nums)
	while left < right:
		mid = (left + right) // 2
		operations = 0
		for val in nums:
			operations += (val - 1) // mid
		if operations > maxOperations:
			left = mid + 1
		else:
			right = mid
	return left


# print('Output', minimumSize([2,4,8,2], 4))
# print('Output', minimumSize([9], 2))
print('Output', minimumSize([7, 17], 2))
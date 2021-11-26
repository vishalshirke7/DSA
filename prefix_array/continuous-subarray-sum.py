"""
https://leetcode.com/problems/continuous-subarray-sum/
"""


def checkSubarraySum(nums, k):
	cur_sum, cur_sum_map = 0, {0: -1}
	for index in range(len(nums)):
		cur_sum += nums[index]
		if k!= 0:
			cur_sum %= k
		if cur_sum in cur_sum_map:
			if index - cur_sum_map[cur_sum] > 1:
				return True
		else:
			cur_sum_map[cur_sum] = index
	return False


# print('Output', checkSubarraySum([23,2,4,6,7], 6))	
# print('Output', checkSubarraySum([23,2,6,4,7], 6))
print('Output', checkSubarraySum([1, 2, 3], 5))
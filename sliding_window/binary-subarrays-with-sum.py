"""
https://leetcode.com/problems/binary-subarrays-with-sum/
"""

# Prefix Sum
# def numSubarraysWithSum(nums, goal):
# 	sum_map = {0:1}
# 	ans = cur_sum = 0
# 	for val in nums:
# 		cur_sum += val
# 		ans += sum_map.get(cur_sum - goal, 0)
# 		sum_map[cur_sum] = sum_map.get(cur_sum, 0) + 1
# 	return ans


# sliwding window
def numSubarraysWithSum(nums, goal):
	cur_sum, ans = 0, 0
	sum_map = dict()
	for index in range(len(nums)):
		cur_sum	+= nums[index]
		if cur_sum - goal in sum_map:
			ans += sum_map[cur_sum - goal]
		if cur_sum == goal:
			ans += 1
		sum_map[cur_sum] = sum_map.get(cur_sum, 0) + 1
	return ans		



print('Output', numSubarraysWithSum([1,0,1,0,1], 2))
print('Output', numSubarraysWithSum([0, 0, 0, 0, 0], 0))
"""
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
"""

# sliding_window
def minOperations(nums, x):
	target = sum(nums) - x
	if target < 0:
		return -1
	if target == 0:
		return len(nums)
	start = end = cur_sum = 0
	ans = -1
	while end < len(nums):
		cur_sum += nums[end]
		while cur_sum >= target:
			if cur_sum == target:
				ans = max(ans, end - start + 1)
			cur_sum -= nums[start]
			start += 1
		end += 1
	return -1 if ans == -1 else len(nums) - ans


# Two sum
def minOperations(nums, x):
	target = -x
	for val in nums:
		target += val
	if target == 0:
		return len(nums)
	sum_map = {0: -1}
	cur_sum = 0
	ans = -1
	for index in range(len(nums)):
		cur_sum += nums[index]
		if cur_sum - target in sum_map:
			ans = max(ans, index - sum_map[cur_sum - target])
		sum_map[cur_sum] = index
	return ans if ans == -1 else len(nums) - ans


print('Output', minOperations([1,1,4,2,3], 5))
print('Output', minOperations([5,6,7,8,9], 4))
print('Output', minOperations([3,2,20,1,1,3], 10))


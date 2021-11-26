"""
https://leetcode.com/problems/minimum-size-subarray-sum/
"""


#OWN
def minSubArrayLen(target, nums):
	start = 0
	ans = float('inf')
	for end in range(len(nums)):
		target -= nums[end]
		while target <= 0:
			ans = min(ans, end - start + 1)
			target += nums[start]
			start += 1
	return 0 if ans == float('inf') else ans




print('Output', minSubArrayLen(7, [2,3,1,2,4,3]))
print('Output', minSubArrayLen(4, [1, 4, 4]))
print('Output', minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
"""
https://leetcode.com/problems/split-array-largest-sum/
"""

"https://leetcode.com/problems/split-array-largest-sum/discuss/89846/Python-solution-with-detailed-explanation"

def splitArray(nums, m):
	ans, left, right = 0, max(nums), sum(nums)
	while left <= right:
		cur_val = splits = 0
		mid = (left + right) // 2
		for val in nums:
			cur_val += val
			if cur_val > mid:
				splits += 1
				cur_val = val
		splits += 1
		if splits <= m:
			ans = mid
			right = mid - 1
		else:
			left = mid + 1
	return ans


print('Output', splitArray([7,2,5,10,8], 2))
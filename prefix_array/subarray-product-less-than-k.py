"""
https://leetcode.com/problems/subarray-product-less-than-k/
"""




def numSubarrayProductLessThanK(nums, k):
	if k<=1:
		return 0
	product = 1
	left = ans = 0
	for index in range(len(nums)):
		product *= nums[index]
		while product >= k:
			product /= nums[left]
			left += 1
		ans += index - left + 1
	return ans


print('Output', numSubarrayProductLessThanK([10,5,2,6], 100))	

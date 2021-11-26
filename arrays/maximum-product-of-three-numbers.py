"""
https://www.geeksforgeeks.org/find-maximum-product-of-a-triplet-in-array/
https://leetcode.com/problems/maximum-product-of-three-numbers/
"""

# Sorting O(nlogn)
def maximumProduct(nums):
	nums.sort()
	return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])

# Suffix Array O(n)
def maximumProduct(nums):
	size, output = len(nums), -float('inf')
	left_max, left_min, right_max, right_min = [-1] * size, [-1] * size, [-1] * size, [-1] * size
	l_max = l_min = nums[0]
	for index in range(1, size):
		left_max[index] = l_max
		left_min[index] = l_min
		if nums[index] > l_max:
			l_max = nums[index]
		if nums[index] < l_min:
			l_min = nums[index]
	r_max = r_min = nums[-1]
	for index in range(size - 2, -1, -1):
		right_max[index] = r_max
		right_min[index] = r_min
		if nums[index] > r_max:
			r_max = nums[index]
		if nums[index] < r_min:
			r_min = nums[index]
	for index in range(1, size-1):
		max1 = max(nums[index] * left_max[index] * right_max[index], nums[index] * left_min[index] * right_min[index])
		max2 = max(nums[index] * left_max[index] * right_min[index], nums[index] * left_min[index] * right_max[index])		
		output = max(output, max(max1, max2))
	return output

# O(n)
def maximumProduct(nums):
	first_min = second_min = float('inf')
	first_max = second_max = third_max = -float('inf')
	for index in range(len(nums)):
		if nums[index] < first_min:
			second_min = first_min
			first_min = nums[index]
		elif nums[index] < second_min:
			second_min = nums[index]
	for index in range(len(nums)):
		if nums[index] > first_max:
			third_max = second_max
			second_max = first_max
			first_max = nums[index]
		elif nums[index] > second_max:
			third_max = second_max
			second_max = nums[index]
		elif nums[index] > third_max:
			third_max = nums[index]
	return max(first_min * second_min * first_max, first_max * second_max * third_max)

print('Output', maximumProduct([-1,-2,-3]))
print('Output', maximumProduct([1, 2, 3, 4]))
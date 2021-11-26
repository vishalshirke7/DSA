"""
https://leetcode.com/problems/next-permutation/
https://www.interviewbit.com/old/problems/next-permutation/
https://practice.geeksforgeeks.org/problems/next-permutation5226/1
"""


#accepted own 
def nextPermutation(nums):
	cur_index, last_index = len(nums) - 1, len(nums) - 1
	while cur_index > 0:
		if nums[cur_index] > nums[cur_index - 1]:
			break
		else:
			cur_index -= 1
	if cur_index <= 0:
		nums.sort()
	else:
		nums[cur_index:] = nums[last_index:cur_index - 1:-1]
		prev_index = cur_index - 1
		while cur_index <= last_index:
			if nums[cur_index] > nums[prev_index]:
				nums[cur_index], nums[prev_index] = nums[prev_index], nums[cur_index]
				break
			else:
				cur_index += 1
	print(nums)


# print('Output', nextPermutation([1,2,3]))
nextPermutation([3, 2, 1])
nextPermutation([1, 1, 5])
nextPermutation([1, 2, 3, 6, 5, 4])
nextPermutation([2, 3, 1])
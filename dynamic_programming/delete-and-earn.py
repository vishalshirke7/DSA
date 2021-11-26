"""
https://leetcode.com/problems/delete-and-earn/
"""


def deleteAndEarn(nums):
	total_sum, max_so_far, number_count = 0, 0, dict()
	for number in nums:
		number_count[number] = number_count.get(number, 0) + 1
	for number, count in number_count.items():
		total_sum += (number * count)
	print(number_count)
	for number, count in number_count.items():
		cur_sum = total_sum
		if number - 1 in number_count:
			cur_sum -= (number_count[number - 1] * (number - 1))
		if number + 1 in number_count:
			cur_sum -= (number_count[number + 1] * (number + 1))
		max_so_far = max(max_so_far, cur_sum)
	return max_so_far


# print('Output', deleteAndEarn([3, 4, 2]))
# print('Output', deleteAndEarn([2,2,3,3,3,4]))
print('Output', deleteAndEarn([1,1,1,2,4,5,5,5,6]))

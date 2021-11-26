"""
https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
"""

def canThreePartsEqualSum(arr):
	total_sum = sum(arr)
	cur_sum = count = 0
	average, remainder = total_sum // 3, total_sum % 3
	for index in range(len(arr)):
		cur_sum += arr[index]
		if cur_sum == average:
			count += 1
			cur_sum = 0
	return not remainder and count >= 3


print('Output', canThreePartsEqualSum())
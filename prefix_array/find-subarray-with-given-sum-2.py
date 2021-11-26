"""
https://leetcode.com/problems/subarray-sum-equals-k/
https://www.geeksforgeeks.org/find-subarray-with-given-sum/
Negative integers

"""

def findSubarraySum(arr, n, Sum):
	sum_map, cur_sum, ans = dict(), 0, 0
	for index in range(n):
		cur_sum += arr[index]
		if cur_sum == Sum:
			ans += 1
		if cur_sum - Sum in sum_map:
			ans += sum_map[cur_sum - Sum]
		sum_map[cur_sum] = sum_map.get(cur_sum, 0) + 1
	return ans


print('Output', findSubarraySum([10, 2, -2, -20, 10], 5, -10))
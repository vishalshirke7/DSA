"""
https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/
"""

def maximumSum(arr):
    array_length = len(arr)
    max_sum = arr[0]
    max_end, max_start = [0] * array_length, [0] * array_length
    max_end[0], max_start[array_length - 1] = arr[0], arr[array_length - 1]
    for index in range(1, array_length):
        max_end[index] = max(max_end[index - 1] + arr[index], arr[index])
        max_sum = max(max_end[index], max_sum)
    for index in range(array_length - 2, -1, -1):
        max_start[index] =  max(arr[index], max_start[index + 1] + arr[index])
    for index in range(1, array_length - 1):
        max_sum = max(max_sum, max_start[index + 1] + max_end[index - 1])
    return max_sum
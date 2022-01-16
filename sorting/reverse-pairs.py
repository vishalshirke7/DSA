"""
https://leetcode.com/problems/reverse-pairs/
"""

import math

def find(nums, target):
    start, end = 0, len(nums) - 1
    final = -1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1                
    return end - final


def reversePairs(nums):
    total = 0
    for index in range(len(nums)):
        total += find(sorted(nums[index + 1:]), math.ceil(nums[index]/2) - 1)
    return total


print('Output', reversePairs([1,3,2,3,1]))    
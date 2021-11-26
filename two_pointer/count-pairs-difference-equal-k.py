"""
https://leetcode.com/problems/k-diff-pairs-in-an-array/
https://www.geeksforgeeks.org/count-pairs-difference-equal-k/
https://www.interviewbit.com/problems/pair-with-given-difference/
"""

import collections

# Hashing O(n)
def TotalPairs(nums, k):
    if k < 0:
        return 0
    number_map, total_pairs = dict(), 0
    for number in nums:
        if number in number_map:
            if k == 0 and number_map[number] == 1:
                total_pairs += 1 
            number_map[number] += 1
        else:
            if number - k in number_map:
                total_pairs += 1
            if number + k in number_map:
                total_pairs += 1
            number_map[number] = 1
    return total_pairs

def findPairs(nums, k):
    res = 0
    c = collections.Counter(nums)
    for i in c:
        if k > 0 and i + k in c or k == 0 and c[i] > 1:
            res += 1
    return res

# Sorting O(nlogn)
def TotalPairs(nums, k):
    if k < 0:
        return 0
    nums.sort()
    start, end, total_pairs = 0, 1, 0
    while start < end and end < len(nums):
        if nums[end] - nums[start] < k:
            end += 1
        else:
            if nums[end] - nums[start] == k:
                if start == 0 or nums[start] != nums[start - 1]:
                    total_pairs += 1
            start += 1
            if start == end:
                end += 1
    return total_pairs


print('Output', TotalPairs([1, 5, 4, 1, 2], 0))
print('Output', TotalPairs([8, 12, 16, 4, 0, 20], 4)) 
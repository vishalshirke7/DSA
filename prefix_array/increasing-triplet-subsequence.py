"""
https://leetcode.com/problems/increasing-triplet-subsequence/
"""

# OWN O(n)
def increasingTriplet(nums):
    left_min, right_max = [0] * len(nums), [0] * len(nums)
    left_min[0] = nums[0]
    right_max[-1] = nums[-1]
    for index in range(1, len(nums)):
        left_min[index] = min(nums[index], left_min[index - 1])
    for index in range(len(nums) - 2, -1, -1):
        right_max[index] = max(nums[index], right_max[index + 1])
    for index in range(len(nums)):
        if left_min[index] < nums[index] < right_max[index]:
            return True
    return False


def increasingTriplet(nums):
    first = second = float('inf')
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False


print('Output', increasingTriplet([2,1,5,0,4,6]))
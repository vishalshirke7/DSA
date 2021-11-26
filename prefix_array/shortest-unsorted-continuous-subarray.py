"""
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
https://www.interviewbit.com/old/problems/maximum-unsorted-subarray/
https://www.geeksforgeeks.org/minimum-length-unsorted-subarray-sorting-which-makes-the-complete-array-sorted/
"""

def findUnsortedSubarray(nums):
    left_max, right_min = [-1] * len(nums), [-1] * len(nums)
    left_max[0], right_min[-1] = 0, len(nums) - 1
    left, right = float('inf'), -float('inf')
    for index in range(1, len(nums)):
        if nums[left_max[index - 1]] > nums[index]:
            left_max[index] = left_max[index - 1]
        else:
            left_max[index] = index
    for index in range(len(nums) - 2, -1, -1):
        if nums[right_min[index + 1]] < nums[index]:
            right_min[index] = right_min[index + 1]
        else:
            right_min[index] = index            
    for index in range(len(nums)):
        if right_min[index] - index >= 1:
            left = min(left, index)
        if index - left_max[index] >= 1:
            right = max(index, right)
    if left != float('inf'):
        return right - left + 1
    return 0


print('Output', findUnsortedSubarray([1]))
print('Output', findUnsortedSubarray([1,2,3,4]))
print('Output', findUnsortedSubarray([1, 3, 2, 4, 5]))
print('Output', findUnsortedSubarray([2,6,4,8,10,9,15]))
print('Output', findUnsortedSubarray([0, 1, 15, 25, 6, 7, 30, 40, 50]))
print('Output', findUnsortedSubarray([10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]))


"""
class Solution(object):
    def findUnsortedSubarray(self, nums):
        if len(nums) <2:
            return 0
        
        prev = nums[0]
        end = 0
        # find the largest index not in place
        for i in range(0, len(nums)):
            if nums[i] < prev:
                end = i
            else:
                prev = nums[i]

        start = len(nums) - 1
        prev = nums[start]
        # find the smallest index not in place
        for i in range(len(nums)-1, -1, -1):
            if prev < nums[i]:
                start = i
            else:
                prev = nums[i]
        if end != 0:
            return end - start + 1
        else: 
            return 0
"""
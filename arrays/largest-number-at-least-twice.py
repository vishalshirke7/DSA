"""
https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/
"""

def dominantIndex(nums):
    if len(nums)==1:
        return 0
    first_max, second_max, max_index = -1, -1, 0
    for i in range(len(nums)):
        if nums[i] > first_max:
            max_index = i
            second_max = first_max
            first_max = nums[i]
        elif nums[i] > second_max:
            second_max = nums[i]
    print(first_max, second_max)
    if first_max >= (2 * second_max):
        return max_index
    return -1

print(dominantIndex([1, 0]))
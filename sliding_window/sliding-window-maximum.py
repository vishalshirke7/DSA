"""
https://leetcode.com/problems/sliding-window-maximum/
https://www.interviewbit.com/old/problems/sliding-window-maximum/
"""


def maxSlidingWindow(nums, k):
    size = len(nums)
    left_max, right_max = [-1] * size, [-1] * size
    left_max[0], right_max[-1] = nums[0], nums[-1]
    for index in range(1, size):
        if index % k == 0:
            left_max[index] = nums[index]
        else:
            left_max[index] = max(left_max[index - 1], nums[index])
        right_index = size - index - 1
        if right_index % k == 0:
            right_max[right_index] = nums[right_index]
        else:
            right_max[right_index] = max(right_max[right_index + 1], nums[right_index])     
    start, end, output = 0, 0, [0] * (size - k + 1)
    while start + k <= size:
        output[end] = max(right_max[start], left_max[start + k - 1])
        start += 1
        end += 1
    return output


print('Output', maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
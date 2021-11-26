"""
https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/
"""


def rangeSum(nums, n, left, right):
    new_arr = nums
    total = sum(nums)
    new_arr += [total]
    start, end = 0, n - 1
    while start <= end:
        new_arr.append(total - nums[start])
        new_arr.append(total - nums[end])
        new_arr.append(total - nums[start] - nums[end])
        start += 1
        end -= 1
    new_arr.sort()
    print(new_arr)
    return sum(new_arr[left-1:right])


print('Output', rangeSum([1,2,3,4], 4, 1, 5))
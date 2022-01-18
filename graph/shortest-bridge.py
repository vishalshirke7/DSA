"""
https://leetcode.com/problems/shortest-bridge/
"""

def sumOfMaxAndMin(nums, n, k):
    # write your code here
    # return an integer denoting the answer
    cmin, cmax = min(nums[:k]), max(nums[:k])
    ans = cmin + cmax
    start, end = 1, k
    while end < n:
        cmin = min(nums[start], nums[end], cmin)
        cmax = max(nums[start], nums[end], cmax)       
        ans += cmin + cmax
        start += 1
        end += 1
    return ans
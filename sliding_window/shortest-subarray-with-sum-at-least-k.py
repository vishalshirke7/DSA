"""
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
"""
import collections

def shortestSubarray(nums, K):
    d = collections.deque([[0, 0]])
    res, cur = float('inf'), 0
    for i, a in enumerate(nums):
        cur += a
        while d and cur - d[0][1] >= K:
            res = min(res, i + 1 - d.popleft()[0])
        while d and cur <= d[-1][1]:
            d.pop()
        d.append([i + 1, cur])
    return res if res < float('inf') else -1


# print('Output', shortestSubarray([1], 1))
# print('Output', shortestSubarray([1, 2], 4))
# print('Output', shortestSubarray([2, -1, 2], 3))
# print('Output', shortestSubarray([77,19,35,10,-14], 19))
print('Output', shortestSubarray([48,99,37,4,-31], 140))
"""
https://leetcode.com/problems/find-the-most-competitive-subsequence/
"""

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = list()
        size = len(nums)
        if size <= k:
            return nums
        for index, val in enumerate(nums):
            while stack and stack[-1] > val:
                if len(stack) + (size - index) > k:
                    stack.pop()
                else:
                    break
            stack.append(val)
        return stack[:k]
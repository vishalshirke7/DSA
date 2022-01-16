"""
https://leetcode.com/problems/contiguous-array/
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        count_map = {0 : -1}
        max_len = 0
        for index, val in enumerate(nums):
            if val == 0:
                count -= 1
            else:
                count += 1
            if count in count_map:
                max_len = max(max_len, index - count_map[count])
            else:
                count_map[count] = index
        return max_len        
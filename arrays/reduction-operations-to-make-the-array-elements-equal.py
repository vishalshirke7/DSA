"""
https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/
"""


#own 
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count_map, ans = dict(), 0
        for val in nums:
            count_map[val] = count_map.get(val, 0) + 1
        count_map = sorted(count_map.items(), key=lambda x:x[0])
        for index in range(len(count_map) - 1, 0, -1):
            ans += (count_map[index][1] * index)
        return ans
"""
https://leetcode.com/problems/subsets-ii/
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        size = len(nums)
        nums.sort()
        
        def dfs(index, cur_path):
            result.append(cur_path)
            for new_index in range(index, size):
                if new_index > index and (nums[new_index] == nums[new_index - 1]):
                    continue
                new_cur_path = cur_path + [nums[new_index]]
                dfs(new_index + 1, new_cur_path)
                
        dfs(0, [])
        return result
"""
https://leetcode.com/problems/permutations/
"""

# O(n!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        size = len(nums)
        def backtrack(index, cur_path, visited):
            if len(cur_path) == size:
                result.append(cur_path)
                return
            for new_index in range(size):
                if not visited[new_index]:
                    visited[new_index] = True
                    new_cur_path = cur_path + [nums[new_index]]
                    backtrack(new_index + 1, new_cur_path, visited)
                    visited[new_index] = False
                    
        
        visited = [False] * size
        backtrack(0, [], visited)
        return result

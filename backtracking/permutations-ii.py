"""
https://leetcode.com/problems/permutations-ii/
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        size = len(nums)
        nums.sort()
        def backtrack(index, cur_path, visited):
            if len(cur_path) == size:
                result.append(cur_path)
                return
            for new_index in range(size):
                if visited[new_index] or ((new_index > 0) and (nums[new_index] == nums[new_index - 1]) and (visited[new_index - 1] == False)):
                    continue
                visited[new_index] = True
                backtrack(new_index + 1, cur_path + [nums[new_index]], visited)
                visited[new_index] = False
                    
        
        visited = [False] * size
        backtrack(0, [], visited)
        return result
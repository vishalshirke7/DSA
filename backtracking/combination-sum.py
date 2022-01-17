"""
https://leetcode.com/problems/combination-sum/
"""

# O(2 ^ n)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = list()
        candidates.sort()
        def dfs(result, temp, candidates, target, start):
            if target < 0:
                return 
            elif target == 0:
                t = temp[:]
                result.append(t)
            else:
                for index in range(start, len(candidates)):
                    if target - candidates[index] >= 0:
                        dfs(result, temp + [candidates[index]], candidates, target - candidates[index], index)
                    else:
                        return
        dfs(result, [], candidates, target, 0)
        return result
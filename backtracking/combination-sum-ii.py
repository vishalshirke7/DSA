"""
https://leetcode.com/problems/combination-sum-ii/
"""

# O(2 ^ n) SC - O(N)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
                    if index > start  and candidates[index] == candidates[index - 1]:
                        continue
                    if target - candidates[index] >= 0:
                        dfs(result, temp + [candidates[index]], candidates, target - candidates[index], index + 1)
                    else:
                        return
        dfs(result, [], candidates, target, 0)
        return result        



class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(comb, remain, curr, counter, results):
            if remain == 0:
                results.append(list(comb))
                return
            elif remain < 0:
                return

            for next_curr in range(curr, len(counter)):
                candidate, freq = counter[next_curr]
                if freq <= 0:
                    continue
                comb.append(candidate)
                counter[next_curr] = (candidate, freq-1)
                backtrack(comb, remain - candidate, next_curr, counter, results)
                counter[next_curr] = (candidate, freq)
                comb.pop()

        results = []
        counter = Counter(candidates)
        counter = [(c, counter[c]) for c in counter]
        backtrack(comb = [], remain = target, curr = 0,
                  counter = counter, results = results)
        return results        



class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(comb, remain, curr, results):

            if remain == 0:
                results.append(list(comb))
                return

            for next_curr in range(curr, len(candidates)):
                if next_curr > curr and candidates[next_curr] == candidates[next_curr-1]:
                    continue

                pick = candidates[next_curr]
                if remain - pick < 0:
                    break
                comb.append(pick)
                backtrack(comb, remain - pick, next_curr + 1, results)
                comb.pop()

        candidates.sort()

        comb, results = [], []
        backtrack(comb, target, 0, results)

        return results        
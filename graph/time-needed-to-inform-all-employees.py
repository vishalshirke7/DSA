"""
https://leetcode.com/problems/time-needed-to-inform-all-employees/
"""

#OWN
import collections
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)
        for node, parent in enumerate(manager):
            graph[parent].append(node)

        def dfs(node):
            sub_time = 0
            localt = informTime[node]
            for subord in graph[node]:
                time_need = dfs(subord)
                sub_time = max(sub_time, time_need)
            return sub_time + localt
        
        return dfs(headID)

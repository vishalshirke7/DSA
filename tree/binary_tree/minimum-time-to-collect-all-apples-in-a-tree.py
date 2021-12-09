"""
https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
"""

#OWN
import collections
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])            

        time = 0
        def dfs(node, par):
            nonlocal graph, time
            child_apples = 0
            for child in graph[node]:
                if child != par:
                    child_apples += dfs(child, node)
            time += (2 * child_apples)
            return int(hasApple[node]) or int(child_apples > 0)
         
        dfs(0, 0)
        return time
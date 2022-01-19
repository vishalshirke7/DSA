"""
https://leetcode.com/problems/number-of-provinces/
"""
# OWN
import collections
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province = 0
        rows, cols = len(isConnected), len(isConnected[0])
        graph = collections.defaultdict(list)
        for row in range(rows):
            for col in range(cols):
                if isConnected[row][col] and row != col:
                    graph[row].append(col)
        visited = [False] * rows
        def dfs(node, par):
            visited[node] = True
            for nei in graph[node]:
                if nei != par and not visited[nei]:
                    dfs(nei, node)

        for node in range(rows):
            if not visited[node]:
                dfs(node, node)
                province += 1
        return province


def findCircleNum(self, A):
    N = len(A)
    seen = set()
    def dfs(node):
        for nei, adj in enumerate(A[node]):
            if adj and nei not in seen:
                seen.add(nei)
                dfs(nei)
    
    ans = 0
    for i in xrange(N):
        if i not in seen:
            dfs(i)
            ans += 1
    return ans
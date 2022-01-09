"""
https://leetcode.com/problems/all-paths-from-source-to-target/
"""

#OWN Backtracking
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = list()
        total_nodes = len(graph) - 1
        
        def dfs(edges, path):
            for child in edges:
                if child == total_nodes:
                    result.append(path + [child])
                else:
                    dfs(graph[child], path + [child])
        
        for child in graph[0]:
            if child == total_nodes:
                result.append([0, child])
            else:
                dfs(graph[child], [0, child])
        return result


# Stack DFS 
def allPathsSourceTarget(graph):
        if not graph:
            return []
        
        d = {}
        for i in range(len(graph)):
            d[i] = graph[i]
        
        n = len(graph)
        stack = [(0, [0])]
        res = []
        while stack:
            node, path = stack.pop()
            if node == n - 1:
                res.append(path)
            for nei in d[node]:
                stack.append((nei, path+[nei]))
        return res
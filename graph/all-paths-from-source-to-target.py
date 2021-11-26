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
        
        #edges cases:
        if not graph:
            return []
        
        # build di-graph
        d = {}
        for i in range(len(graph)):
            d[i] = graph[i] # one-way link
        
        # apply DFS on DAG
        n = len(graph)
        stack = [(0, [0])] # - store noth the (node, and the path leading to it)
        res = []
        while stack:
            node, path = stack.pop()
            # check leaf
            if node == n - 1:
                res.append(path)
            # traverse rest
            for nei in d[node]:
                stack.append((nei, path+[nei]))
        return res        
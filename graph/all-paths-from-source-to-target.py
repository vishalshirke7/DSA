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

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        self.dfs(graph, [0], 0, res)
        
        return res
        
        
    def dfs(self, graph: List[List[int]], cur_res: List[int], cur_node: int, res: List[List[int]]) -> None:
        if cur_node == len(graph)-1:
            res.append(list(cur_res))
        
        for node in graph[cur_node]:
            cur_res.append(node)
            self.dfs(graph, cur_res, node, res)
            cur_res.pop()        


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
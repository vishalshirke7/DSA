"""
https://www.interviewbit.com/old/problems/cycle-in-directed-graph/
"""

# DFS
import collections
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        graph = collections.defaultdict(list)
        for v1, v2 in B:
            graph[v1].append(v2)
            
        visited = set()
        dfs_visited = [0] * A
        
        def dfs(node):
            nonlocal graph, visited, dfs_visited
            visited.add(node)
            dfs_visited[node - 1] = 1
            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei):
                    	return 1
                else:
                    if dfs_visited[nei - 1]:
                        return 1
            dfs_visited[node - 1] = 0
            return 0

        for node in range(1, A + 1):
            if node not in visited:
                if dfs(node):
                    return 1
        return 0


obj = Solution()
print(obj.solve(5, [[1, 2],[1, 3],[2, 3],[1, 4],[4, 3],[4, 5],[3, 5]]))        


# BFS

# IT IS DONE ONLY ON DAG USING TOPOLIGICAL SORT
import collections

class Graph:
    def __init__(self, vertices):
        self.graph = collections.defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortBFS(self):
        topo_order = []
        in_degree = [0] * self.V
        queue = collections.deque()
        for index in range(self.V):
            for neighbour in self.graph[index]:
                in_degree[neighbour] += 1

        for index in range(self.V):
            if in_degree[index] == 0:
                queue.append(index)
        while queue:
            cur_node = queue.popleft()
            topo_order.append(cur_node)
            for neighbour in self.graph[cur_node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
        print(topo_order)

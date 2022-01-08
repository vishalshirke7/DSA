"""
https://www.geeksforgeeks.org/topological-sorting/
"""
# IT IS DONE ONLY ON DAG
import collections

class Graph:
    def __init__(self, vertices):
        self.graph = collections.defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortDFSUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortDFSUtil(i, visited, stack)
        stack.append(v)

    def topologicalSortDFS(self):
        visited = [False]*self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortDFSUtil(i, visited, stack)
        print(stack[::-1])


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


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
print ("Following is a Topological Sort of the given graph using BFS")
g.topologicalSortBFS()
print ("Following is a Topological Sort of the given graph using DFS")
g.topologicalSortDFS()



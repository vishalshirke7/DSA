import collections 
 
class Graph:
 
    def __init__(self,vertices):
    
        self.V= vertices
        self.graph = collections.defaultdict(list)

 
    def addEdge(self,v,w):
        self.graph[v].append(w)
        self.graph[w].append(v)
 
    def shortestPath(self, source):
        distance = [float('inf')] * self.V
        distance[source] = 0
        queue = collections.deque()
        queue.append(source)
        while queue:
            node = queue.popleft()
            for neighbour in self.graph[node]:
                if distance[node] + 1 < distance[neighbour]:
                    distance[neighbour] = distance[node] + 1
                    queue.append(neighbour)
        print(distance)


g = Graph(5)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
g.shortestPath(2)
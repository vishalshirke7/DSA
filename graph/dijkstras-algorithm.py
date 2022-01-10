"""
Provided that all of the vertices are reachable from the source vertex; 
Dijkstra’s algorithm can be used to find the shortest distance from the source vertex to all other vertices in a weighted graph. 
The graph can be directed or undirected, cyclic or acyclic, but the weights on all edges need to be nonnegative.
"""

 class Solution(object):
    def dijkstra(self, edges, vertices, source):
        graph = collections.defaultdict(list)
        for v1, v2, cost in edges:
            graph[v1].append((v2, cost))

        priority_q = [(0, source)]
        dist = {}
        while priority_q:
            d, node = heapq.heappop(priority_q)
            if node in dist: continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(priority_q, (d+d2, nei))

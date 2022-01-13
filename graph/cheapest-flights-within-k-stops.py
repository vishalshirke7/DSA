"""
https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""

# TLE
class Solution:
     def findCheapestPrice(self, n, flights, src, dst, k):
        graph = collections.defaultdict(list)
        for v1, v2, cost in flights:
            graph[v1].append([v2, cost])
        heap, seen = [(0, src, k + 1)], dict()
        while heap:
            cost, node, stops = heapq.heappop(heap)
            if node == dst:
                return cost
            if node in seen and seen[node] >= stops:
                continue
            if stops:
                for nei, nei_cost in node[node]:
                    heapq.heappush(heap, (cost + nei_cost, nei, seen - 1))
        return -1

# Accepted
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for v1, v2, cost in flights:
            graph[v1].append([v2, cost])
        heap, seen = [(0, src, k + 1)], dict()
        while heap:
            cost, node, stops = heapq.heappop(heap)
            if node == dst:
                return cost
            if node in seen and seen[node] >= stops:
                continue
            if stops:
                for nei, nei_cost in graph[node]:
                    heapq.heappush(heap, (cost + nei_cost, nei, seen - 1))
        return -1        
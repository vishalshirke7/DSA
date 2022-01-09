"""
https://leetcode.com/problems/network-delay-time/
"""
# THIS IS A CYCLIC GRAPH PROBLEM AND HENCE TOPO SORT CAN NOT BE USED
# WE HAVE TO USE DIJKSTRA

# USING NORMAL DFS

import collections
class Solution:
    def networkDelayTime(self, times, n, k):
        graph = collections.defaultdict(list)
        for v1, v2, cost in times:
            graph[v1].append((cost, v2))
        
        distace = {node: float('inf') for node in range(1, n + 1)}
        
        def dfs(node, elapsed_time):
            if elapsed_time >= distace[node]:
                return
            distace[node] = elapsed_time
            for cost, nei in sorted(graph[node]):
                dfs(nei, elapsed_time + cost)
        
        dfs(k, 0)
        ans = max(distace.values())
        return -1 if ans == float('inf') else ans
        
 # USING DIJKSTRA with O(N^2) 

class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in range(1, N+1)}

        seen = [False] * (N+1)
        dist[K] = 0

        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in range(1, N+1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i

            if cand_node < 0: break
            seen[cand_node] = True
            for nei, d in graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + d)

        ans = max(dist.values())
        return ans if ans < float('inf') else -1

 # USING DIJKSTRA with O(Nlog N) USING HEAP

 class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, K)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist: continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))

        return max(dist.values()) if len(dist) == N else -1

# USING QUEUE

class Solution:
    def networkDelayTime(self, times, N, K):
        t, graph, q = [0] + [float("inf")] * N, collections.defaultdict(list), collections.deque([(0, K)])
        for u, v, w in times:
            graph[u].append((v, w))
        while q:
            time, node = q.popleft()
            if time < t[node]:
                t[node] = time
                for v, w in graph[node]:
                    q.append((time + w, v))
        mx = max(t)
        return mx if mx < float("inf") else -1        
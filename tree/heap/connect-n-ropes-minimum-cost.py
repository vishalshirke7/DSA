"""
https://www.geeksforgeeks.org/connect-n-ropes-minimum-cost/
"""

import heapq

class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
        cost = 0
        heapq.heapify(arr)
        while len(arr) > 1:
            first, sec = heapq.heappop(arr), heapq.heappop(arr)
            cost += first + sec
            heapq.heappush(arr, first + sec)
            
        return cost
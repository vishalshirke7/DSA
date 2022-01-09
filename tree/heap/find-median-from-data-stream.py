"""
https://leetcode.com/problems/find-median-from-data-stream/
https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/
"""

from heapq import *
from sortedcontainers import SortedList


class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -num)
        heappush(self.minHeap, -heappop(self.maxHeap))
        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0]) / 2


class MedianFinder:

    def __init__(self):
        self.arr = SortedList()

    def addNum(self, num: int) -> None:
        self.arr.add(num)

    def findMedian(self) -> float:
        n = len(self.arr)
        if n % 2 == 1:
            return self.arr[n//2]
        return (self.arr[n//2] + self.arr[n//2-1]) / 2        

# class MedianFinder:

#     def __init__(self):
#         self.minh = [] # elements right of median
#         self.maxh = [] # elements left of median
#         self.idx = -1

#     def addNum(self, num: int) -> None:
#         self.idx += 1

#         if self.idx == 0:
#             heappush(self.minh, (num, self.idx, num))
#             return

#         if len(self.minh) > len(self.maxh):
#             if num > self.minh[0][-1]:
#                 prio, idx, el = heappop(self.minh)
#                 heappush(self.maxh, (-prio, idx, el))
#                 heappush(self.minh, (num, self.idx, num))
#             else:
#                 heappush(self.maxh, (-num, self.idx, num))
#         else:
#             if num < self.maxh[0][-1]:
#                 prio, idx, el = heappop(self.maxh)
#                 heappush(self.minh, (-prio, idx, el))
#                 heappush(self.maxh, (-num, self.idx, num))
#             else:
#                 heappush(self.minh, (num, self.idx, num))

#     def findMedian(self) -> float:
#         if len(self.minh) < len(self.maxh):
#             return self.maxh[0][-1]
#         elif len(self.minh) > len(self.maxh):
#             return self.minh[0][-1]
#         else:
#             return (self.minh[0][-1] + self.maxh[0][-1]) / 2


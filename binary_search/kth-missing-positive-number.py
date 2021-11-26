"""
https://leetcode.com/problems/kth-missing-positive-number/
"""

#Own O(n)

def findKthPositive(arr, k):
    visited = [False] * 2001
    for val in arr:
        visited[val] = True
    for index in range(1, 2001):
        if not visited[index]:
            if k == 1:
                return index
            k -= 1
        

#discuss O(logn)

def findKthPositive(self, arr, k):
    beg, end = 0, len(arr)
    while beg < end:
        mid = (beg + end) // 2
        if arr[mid] - mid - 1 < k:
            beg = mid + 1
        else:
            end = mid
    return end + k
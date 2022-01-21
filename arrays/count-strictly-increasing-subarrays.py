"""
https://www.geeksforgeeks.org/count-strictly-increasing-subarrays/
"""

# OWN

class Solution:

    def countIncreasing(self,arr, n):
        # code here
        ans = 0
        small_index = 0
        for index in range(1, n):
            if arr[index] > arr[index - 1]:
                ans += index - small_index
            else:
                small_index = index
        return ans

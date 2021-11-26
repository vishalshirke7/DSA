"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

# (m + n)log(m + n)

class Solution:
    
    def find_median(self, numbers, size):
        mid = (size - 1) // 2
        if size % 2 == 0:
            return (numbers[mid] + numbers[mid + 1]) / 2
        else:
            return numbers[mid]
            
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if not m:
            return self.find_median(nums2, n)
        if not n:
            return self.find_median(nums1, m)
        combined = nums1 + nums2
        combined.sort()
        return self.find_median(combined, m+n)



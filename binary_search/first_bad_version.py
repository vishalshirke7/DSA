"""
https://leetcode.com/problems/first-bad-version/submissions/
"""

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n
        start, end = 1, n
        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                if mid - 1 > 0:
                    if isBadVersion(mid - 1):
                        end = mid - 1
                    else:
                        return mid
                else:
                    return mid
            else:
                start = mid + 1
                

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n
        start, end = 1, n
        while start < end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
        return start
        
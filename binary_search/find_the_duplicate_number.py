"""
https://leetcode.com/problems/find-the-duplicate-number/
"""

"https://keithschwarz.com/interesting/code/?dir=find-duplicate"

def findDuplicate(nums):
        low = 1
        high = len(nums)-1
        
        while low < high:
            mid = low+(high-low)/2
            count = 0
            for i in nums:
                if i <= mid:
                    count+=1
            if count <= mid:
                low = mid+1
            else:
                high = mid
        return low
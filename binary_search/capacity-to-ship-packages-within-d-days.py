"""
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
"""


def shipWithinDays(weights, D):
        low, high = max(weights), sum(weights)
        while low < high:
            mid = (low + high) // 2
            total, days = 0, 1
            for wet in weights:
                if total + wet > mid:
                    days += 1
                    total = wet
                else:
                    total += wet
            if days <= D:
                high = mid
            else:
                low = mid + 1
        return low


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:        
        def can_ship(capacity):
            total_days = days
            total_wt = 0
            for wt in weights:
                if wt > capacity:
                    return False
                if wt + total_wt > capacity:
                    total_wt = wt
                    total_days -= 1
                else:
                    total_wt += wt
                if total_days <= 0:
                    return False
            return True
        
        ans = float('inf')
        start, end = 0, sum(weights)
        while start <= end:
            mid = (start + end) // 2
            if can_ship(mid):
                ans = min(ans, mid)
                end = mid - 1
            else:
                start = mid + 1
        return ans
        
print('Output', shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))        
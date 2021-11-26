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


print('Output', shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))        
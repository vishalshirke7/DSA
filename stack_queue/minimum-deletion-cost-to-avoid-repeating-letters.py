"""
https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/
"""


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        size = len(s)
        if size <= 1:
            return 0
        mincost = 0
        stack = [0]
        for index in range(1, size):
            if s[index] == s[stack[-1]]:
                if cost[index] > cost[stack[-1]]:
                    minindex = stack.pop()
                    stack.append(index)
                else:
                    minindex = index
                mincost += cost[minindex]
            else:
                stack.append(index)
        return mincost
                


# Two pointer + Greedy

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        left, ans = 0, 0
        for right in range(1, len(s)):
            if s[left] == s[right]:
                if cost[left] < cost[right]:
                    ans += cost[left]
                else:
                    ans += cost[right]
                    continue 

            left = right
        return ans                
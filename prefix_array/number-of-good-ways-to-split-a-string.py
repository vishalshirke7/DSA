"""
https://leetcode.com/problems/number-of-good-ways-to-split-a-string/
"""
#OWN
class Solution:
    def numSplits(self, s: str) -> int:
        left_u, right_u = [1] * len(s), [1] * len(s)
        l_m, r_m = dict(), dict()
        cnt = 0
        for index in range(len(s)):
            if s[index] not in l_m:
                cnt += 1
                l_m[s[index]] = 1
            left_u[index] = cnt                
        cnt = 0
        for index in range(len(s) - 1, -1, -1):
            if s[index] not in r_m:
                cnt += 1
                r_m[s[index]] = 1
            right_u[index] = cnt
        ans = 0 
        for index in range(len(s) - 1):
            if left_u[index] == right_u[index + 1]:
                ans += 1
        # print(left_u, right_u)
        return ans
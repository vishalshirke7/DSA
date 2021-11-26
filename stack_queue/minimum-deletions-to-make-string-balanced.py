"""
https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
"""


# class Solution:
#     def minimumDeletions(self, s: str) -> int:
#         # track the minimum number of deletions to make the current string balanced ending with 'a', 'b'
#         end_a, end_b = 0,0 
#         for val in s:
#             if val == 'a':
#                 # to end with 'a', nothing to do with previous ending with 'a'
#                 # to end with 'b', need to delete the current 'a' from previous ending with 'b'
#                 end_b += 1
#             else:
#                 # to end with 'a', need to delete the current 'b' from previous ending with 'a'
#                 # to end with 'b', nothing to do, so just pick smaller of end_a, end_b
#                 end_a, end_b = end_a+1, min(end_a, end_b)
#         return min(end_a, end_b)

# O(n)
def minimumDeletions(s):
    cnt_b = 0
    dp = [0]
    for c in s:
        if c == 'b':
            cnt_b+=1
            dp.append( dp[-1] )
        else:
            dp.append( min(cnt_b,dp[-1]+1) )
    return dp[-1]


print('Output', minimumDeletions('aababbab'))    

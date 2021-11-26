"""
https://leetcode.com/problems/count-number-of-teams/
"""


def numTeams(rating):
	output = 0
	for index_i in range(len(rating)):
		left_smaller, right_larger, left_larger, right_smaller = 0, 0, 0, 0
		for index_l in range(0, index_i):
			if rating[index_l] < rating[index_i]:
				left_smaller += 1
			else:
				left_larger += 1
		for index_r in range(index_i + 1, len(rating)):
			if rating[index_r] > rating[index_i]:
				right_larger += 1
			else:
				right_smaller += 1
		output += left_smaller * right_larger + left_larger * right_smaller
	return output

print('Output', numTeams([2,5,3,4,1]))	
print('Output', numTeams([2, 1, 3]))
"""
from collections import defaultdict

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0
        
        greater = defaultdict(int)
        less = defaultdict(int)
        res = 0
        
		# greater[i] is the number of elements after index i greater than ratings[i]
        for i in range(len(rating)-1):
            for j in range(i+1, len(rating)):
                if rating[j] > rating[i]:
                    greater[i] += 1
                else:
                    less[i] += 1
        
		# Accumulate counts
        for i in range(len(rating)-2):
            for j in range(i+1, len(rating)):
                if rating[i] < rating[j]:
                    res += greater[j]
                else:
                    res += less[j]
        
        return res
"""
"""
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        
        up = [0] * n
        down = [0] * n
        
        teams = 0
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if rating[i] < rating[j]:
                    up[i] += 1
                    teams += up[j]
                else:
                    down[i] += 1
                    teams += down[j]
        
        return teams
"""        
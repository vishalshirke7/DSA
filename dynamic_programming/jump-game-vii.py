"""
https://leetcode.com/problems/jump-game-vii/
"""
"https://leetcode.com/problems/jump-game-vii/discuss/1224936/DP-%2B-Sliding-Window-or-O(N)-or-Single-Pass"
"https://leetcode.com/problems/jump-game-vii/discuss/1230326/Java-or-Full-explanation%3A-Brute-Force-O(n2)-DP-greater-O(n)-Partial-Sum-greater-O(n)-Sliding-Window"


import collections

def canReach(s, minJump, maxJump):
    q, max_reached = collections.deque([0]), 0
    while q:
        print(q)        
        curr_i = q.popleft()
        if curr_i == len(s) - 1:
            return True
        start = max(curr_i + minJump, max_reached)
        for i in range(start, min(curr_i + maxJump + 1, len(s))):
            if s[i] == '0':
                q.append(i)
        max_reached = curr_i + maxJump
    return False
    

print('Output', canReach("01101110", 2, 3))
# print('Output', canReach("011010", 2, 3))
# print('Output', canReach("00", 1, 1))
# print('Output', canReach("01", 1, 1))
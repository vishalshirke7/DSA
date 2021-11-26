"""
https://leetcode.com/problems/sum-of-subarray-minimums/
"""

def sumSubarrayMins(A):
    res = 0
    stack = []  #  non-decreasing 
    A = [float('-inf')] + A + [float('-inf')]
    for i, n in enumerate(A):
        while stack and A[stack[-1]] > n:
            cur = stack.pop()
            res += A[cur] * (i - cur) * (cur - stack[-1]) 
        stack.append(i)
    return res % (10**9 + 7)

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        A = [0]+A
        result = [0]*len(A)
        stack = [0]
        for i in range(len(A)):
            while A[stack[-1]] > A[i]:
                stack.pop() 
            j = stack[-1]
            result[i] = result[j] + (i-j)*A[i]
            stack.append(i)
        return sum(result) % (10**9+7)
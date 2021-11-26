"""
https://leetcode.com/problems/3sum/
https://www.interviewbit.com/old/problems/3-sum/
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        ans, closest = 0, float('inf')
        for index in range(len(A)):
            start, end = index + 1, len(A) - 1
            while start < end:
                cur_sum = A[index] + A[start] + A[end]
                if abs(B - cur_sum) < closest:
                    closest = abs(B - cur_sum)
                    ans = cur_sum
                if cur_sum == B:
                    return cur_sum 
                elif cur_sum > B:
                    end -= 1
                else:
                    start += 1
        return ans
                    
                    
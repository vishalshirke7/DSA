"""https://www.interviewbit.com/old/problems/valid-bst-from-preorder/"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if not A:
            return 1
        stack = [-1]
        root = A[0]
        for pre in A:
            if pre < root:
                return 0
            while stack and pre > stack[-1]:
                root = stack.pop()
            stack.append(pre)
        return 1

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        low = -1
        for i in range(1,len(A)):
            if A[i-1] < A[i]:
                low = A[i-1]
            if A[i] < low:
                return 0
        return 1

"""
https://www.interviewbit.com/old/problems/last-node-in-a-complete-binary-tree/
"""

class Solution:
    
    def getLeftHeight(self, A):
        c = 0
        while A:
            c += 1
            A = A.left
        return c

    def lastNode(self, A):
        h = self.getLeftHeight(A)

        if h == 1:
            return A.val
        
        if h - 1 == self.getLeftHeight(A.right):
            return self.lastNode(A.right)
        
        return self.lastNode(A.left)
"""
https://www.interviewbit.com/old/problems/inorder-traversal-of-cartesian-tree/
"""
#OWN
class Solution:

    def buildTree(self, A):
        if not A:
            return None
        root = TreeNode(A[0])
        stack = [root]
        for val in A[1:]:
            new_node = TreeNode(val)
            last_small = None
            while stack and stack[-1].val < val:
                last_small = stack.pop()
            new_node.left = last_small
            if stack:
                stack[-1].right = new_node
            stack.append(new_node)
            if val > root.val:
                root = new_node
        return root

class Solution:
    
    def getMaxNode(self,A):
        maxInd = -1
        maxNum = -1*float("inf")
        if(len(A) == 0):
            return None
        for i in range(len(A)):
            if(A[i] > maxNum):
                maxInd = i
                maxNum = A[i]
        left = A[:maxInd]
        right = A [maxInd+1:]
        currNode = TreeNode(maxNum)
        currNode.left = self.getMaxNode(left)
        currNode.right = self.getMaxNode(right)
        return currNode
    
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        return self.getMaxNode(A)
        
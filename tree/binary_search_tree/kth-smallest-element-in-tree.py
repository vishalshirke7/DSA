"""
https://www.interviewbit.com/old/problems/kth-smallest-element-in-tree/
"""

class Solution:

    def kthsmallest(self, A, B):
        def inorder(root, traversal):
            if root:
                inorder(root.left, traversal)
                traversal.append(root.val)
                inorder(root.right, traversal)
        
        traversal = list()
        inorder(A, traversal)
        return traversal[B-1]






class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        self.ans = None
        self.nvisited = 0
        self.inorder(A, B)
        return self.ans
    
    
    #just using inorder technique by remembering position of a node in inorder transversal    
    def inorder(self, root, k):
        if root == None:
            return 
        self.inorder(root.left, k)
        self.nvisited += 1
        if self.nvisited == k:
            self.ans = root.val
            return
        if self.nvisited > k:
            return
        self.inorder(root.right, k)
        return        
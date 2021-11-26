"""
https://leetcode.com/problems/symmetric-tree/
"""

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [root.left, root.right]
        while stack:
            node1, node2 = stack.pop(), stack.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            if node1 and node2:
                stack.append(node1.left)
                stack.append(node2.right)               
                stack.append(node1.right)
                stack.append(node2.left)
        return True




class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(left, right):
            if not left or not right:
                return left == right
            if left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)




class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        
        q = collections.deque([root.left, root.right])
        
        while q:
            t1, t2 = q.popleft(), q.popleft()

            if not t1 and not t2:
                continue
            elif (not t1 or not t2) or (t1.val != t2.val):
                return False
            
            q += [t1.left, t2.right, t1.right, t2.left]
            
        return True
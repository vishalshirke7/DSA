"""https://leetcode.com/problems/merge-two-binary-trees/"""

# OWN Creating new Tree
class Solution:
    
    def pre_order(self, r1, r2):
        if not r1 and not r2:
            return None
        if r1 and r2:
            node = TreeNode(r1.val + r2.val)
            node.left = self.pre_order(r1.left, r2.left)
            node.right = self.pre_order(r1.right, r2.right)
            return node
        else:
            return r1 or r2
            
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.pre_order(root1, root2)


# In place
class Solution:

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.left = self.mergeTrees(root1.right, root2.right)
        return root1


# BFS

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not (t1 and t2):
            return t1 or t2
        queue1, queue2 = collections.deque([t1]), collections.deque([t2])
        while queue1 and queue2:
            node1, node2 = queue1.popleft(), queue2.popleft()
            if node1 and node2:
                node1.val = node1.val + node2.val
                if (not node1.left) and node2.left:
                    node1.left = TreeNode(0)
                if (not node1.right) and node2.right:
                    node1.right = TreeNode(0)
                queue1.append(node1.left)
                queue1.append(node1.right)
                queue2.append(node2.left)
                queue2.append(node2.right)
        return t1        
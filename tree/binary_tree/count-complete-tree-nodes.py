"""
https://leetcode.com/problems/count-complete-tree-nodes/
"""

class Solution:
    
    def leftHeight(self, root):
        if not root:
            return 0 
        return 1 + self.leftHeight(root.left)

    def rightHeight(self, root):
        if not root:
            return 0 
        return 1 + self.rightHeight(root.right)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height = self.leftHeight(root)
        right_height = self.rightHeight(root)
        if left_height == right_height:
            return (2 ** left_height) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

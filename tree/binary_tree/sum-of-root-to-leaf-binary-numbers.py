"""
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
"""

# Iterative
class Solution:
    
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = 0
        if not root:
            return total
        stack = [(root, 0)]
        while stack:
            cur_node, cur_number = stack.pop()
            cur_number = cur_number << 1 | cur_node.val
            if not cur_node.left and not cur_node.right:
                total += cur_number
            else:
                stack.append((cur_node.left, cur_number))
                stack.append((cur_node.right, cur_number))
        return total


# RECURSION        

class Solution:
    
    def sumRootToLeaf(self, root, val=0):
            if not root: return 0
            val = val * 2 + root.val
            if root.left == root.right: return val
            return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)
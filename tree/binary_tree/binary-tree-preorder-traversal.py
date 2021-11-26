"""
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""

#Recursion
class Solution:
    
    def pre_order(self, root, traverse):
        if root:
            traverse.append(root.val)
            self.pre_order(root.left, traverse)
            self.pre_order(root.right, traverse)
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        self.pre_order(root, res)
        return res


#ITERATIVE
def preorderTraversal(root):
    res = list()
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            res.append(node)
            stack.append(node.right)
            stack.append(node.left)         
    return res
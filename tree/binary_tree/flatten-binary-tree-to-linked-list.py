"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root:
            stack = list()
            cur = root
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            cur.left = None
            while stack:
                cur.right = stack.pop()
                if cur.right.right:
                    stack.append(cur.right.right)
                if cur.right.left:
                    stack.append(cur.right.left)
                cur = cur.right
                cur.left = None


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root:
            stack = [root]
            while stack:
                cur = stack.pop()
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
                if stack:
                    cur.right = stack[-1]
                cur.left = None


class Solution:
    def __init__(self):
        self.prev = None
        
    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
"""
https://leetcode.com/problems/binary-tree-postorder-traversal/
"""
from collections import deque

#1.
def postorderTraversal(root):
    stack = []
    result = []
    last = None
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            top = stack[-1]
            if top.right and top.right != last:
                root = top.right
            else:
                top = stack.pop()
                result.append(top.val)
                last = top


# 2.
def postorderTraversal(self, root):
    traversal, stack = [], [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                # add to result if visited
                traversal.append(node.val)
            else:
                # post-order
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

    return traversal                
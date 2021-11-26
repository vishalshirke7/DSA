"""https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/"""
from collections import deque

#1. OWN
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        stack = []
        total = 0
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
                    top = stack[-1]
                    size = len(stack)
                    if size - 3 >= 0 and stack[size - 3].val % 2 ==0:
                        total += top.val
                    last = stack.pop()
        return total


#2. DFS 

class Solution:

    total = 0
    def dfs(self, cur, parent, grand_parent):
        if not cur:
            return 
        if grand_parent and grand_parent.val % 2 == 0:
            self.total += cur.val
        self.dfs(cur.left, cur, parent)
        self.dfs(cur.right, cur, parent)        

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.dfs(root, None, None)
        return self.total


# 3. BFS

class Solution:

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        queue = deque()
        if not root:
            return 0
        total = 0
        queue.append(root)
        while queue:
            cur = queue.popleft()
            if cur.left:
                queue.append(cur.left)
                if cur.val % 2 == 0:
                    if cur.left.left:
                        total += cur.left.left.val
                    if cur.left.right:
                        total += cur.left.right.val
            if cur.right:
                queue.append(cur.right)
                if cur.val % 2 == 0:
                    if cur.right.right:
                        total += cur.right.right.val
                    if cur.right.left:
                        total += cur.right.left.val
        return total
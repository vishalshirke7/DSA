"""
https://leetcode.com/problems/find-bottom-left-tree-value/
"""

#BFS
from collections import deque

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        while queue:
            path = []            
            for index in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                path.append(node.val)
        return path[0]


#DFS
class Solution:

    max_level = 0
    left_val = 0

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def dfs(root, level):
            if root:
                if level > self.max_level:
                    self.max_level = level
                    self.left_val = root.val
                dfs(root.left, level + 1)
                dfs(root.right, level + 1)
        dfs(root, 0)
        return self.left_val

"""
https://leetcode.com/problems/even-odd-tree/
"""

# OWN
class Solution:
    
        
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, level):
            nonlocal level_map
            if not root:
                return True
            if (level & 1):
                if (root.val & 1):
                    return False
            elif not (root.val & 1):
                return False
            if level in level_map:
                if (level & 1):
                    if root.val >= level_map[level]:
                        return False
                else:
                    if root.val <= level_map[level]:
                        return False
            level_map[level] = root.val
            return dfs(root.left, level + 1) and dfs(root.right, level + 1)
        
        if not root:
            return True
        level_map = dict()        
        return dfs(root, 0)


# 2. Discuss BFS
import collections
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        queue = collections.deque([root])
        is_even = True
        while queue:
            prev = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if is_even:
                    if node.val % 2 == 0: return False
                    if prev and prev.val >= node.val: return False
                else:
                    if node.val % 2 == 1: return False
                    if prev and prev.val <= node.val: return False
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                prev = node
            is_even = not is_even
        return True                      
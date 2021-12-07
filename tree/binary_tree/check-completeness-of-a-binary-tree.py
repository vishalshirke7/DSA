"""
https://leetcode.com/problems/check-completeness-of-a-binary-tree/
"""
#OWN
import collections 

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        queue = collections.deque()
        queue.append(root)
        inc_levels = 0
        while queue:
            queue_size = len(queue)
            null_node_found = False
            for index in range(queue_size):
                node = queue.popleft()
                if node:
                    if null_node_found:
                        return False
                    queue.append(node.left)
                    queue.append(node.right)                                
                else:
                    null_node_found = True
                last_node = node
            if null_node_found:
                inc_levels += 1
        return inc_levels <= 2
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


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        queue = collections.deque()
        queue.append(root)
        end = False
        while queue:
            ndoe = queue.popleft()
            if node is None:
                end = True
            else:
                if end:
                    return False
                queue.append(ndoe.left)
                queue.append(ndoe.right)
        return True



class Solution(object):
    node_count = 0
    max_position = 0

    def isCompleteTree(self, root):
        self.isCompleteTreeHelper(root, 1)
        return self.max_position == self.node_count

    def isCompleteTreeHelper(self, root, position):
        if root is None:
            return
        self.node_count += 1
        self.max_position = max(self.max_position, position)
        self.isCompleteTreeHelper(root.left, 2 * position)
        self.isCompleteTreeHelper(root.right, 2 * position + 1)
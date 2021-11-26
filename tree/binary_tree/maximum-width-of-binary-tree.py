"""
https://leetcode.com/problems/maximum-width-of-binary-tree/
"""
import collections

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        queue  = collections.deque()
        queue.append((root, 0))
        while queue:
            first, last = queue[0][1], queue[-1][1]
            for index in range(len(queue)):
                cur_node, cur_index = queue.popleft()
                if cur_node.left:
                    queue.append((cur_node.left, 2 * cur_index))
                if cur_node.right:
                    queue.append((cur_node.right, (2 * cur_index) + 1))
            max_width = max(max_width, last - first + 1)
        return max_width
                
            

"""
https://www.interviewbit.com/old/problems/right-view-of-binary-tree/
https://leetcode.com/problems/binary-tree-right-side-view/
"""

#OWN
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [(root, 0)]
        prev_level = 0
        prev_node = root
        right_view = []
        while queue:
            element = queue.pop(0)
            cur_node = element[0]
            cur_level = element[1]
            if cur_level != prev_level:
                prev_level = cur_level
                right_view += [prev_node.val]
            prev_node = cur_node
            if cur_node.left:
                queue.append((cur_node.left, cur_level + 1))
            if cur_node.right:
                queue.append((cur_node.right, cur_level + 1))
        if prev_node:
            right_view.append(prev_node.val)
        return right_view

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = dict()
        def dfs(node, level):
            nonlocal result
            if node:
                if level not in result:
                    result[level] = node.val
                dfs(node.right, level + 1)
                dfs(node.left, level + 1)
        final = []
        index = 0
        dfs(root, 0)
        while index in result:
            final.append(result[index])
            index += 1
        return final

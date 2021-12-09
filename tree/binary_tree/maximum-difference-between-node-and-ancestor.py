"""
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
"""

# OWN
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_diff = 0
        def dfs(root, par):
            nonlocal max_diff
            if not root:
                return par, par
            l_min, l_max = dfs(root.left, root.val)
            r_min, r_max = dfs(root.right, root.val)
            final_min, final_max = min(l_min, r_min), max(l_max, r_max)
            max_diff = max(max_diff, max(abs(root.val - final_min), abs(root.val - final_max)))
            return min(final_min, root.val), max(final_max, root.val)
        dfs(root, root.val)        
        return max_diff

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        # record the required maximum difference
        self.result = 0

        def helper(node, cur_max, cur_min):
            if not node:
                return
            # update `result`
            self.result = max(self.result, abs(cur_max-node.val),
                              abs(cur_min-node.val))
            # update the max and min
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            helper(node.left, cur_max, cur_min)
            helper(node.right, cur_max, cur_min)

        helper(root, root.val, root.val)
        return self.result


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0

        def helper(node, cur_max, cur_min):
            # if encounter leaves, return the max-min along the path
            if not node:
                return cur_max - cur_min
            # else, update max and min
            # and return the max of left and right subtrees
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            left = helper(node.left, cur_max, cur_min)
            right = helper(node.right, cur_max, cur_min)
            return max(left, right)

        return helper(root, root.val, root.val)        
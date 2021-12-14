"""
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
"""

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root, is_left=True):
            nonlocal ans
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right, False)
            ans = max(ans, max(left, right))
            if is_left:
                return 1 + right
            return 1 + left
        
        dfs(root)
        return ans
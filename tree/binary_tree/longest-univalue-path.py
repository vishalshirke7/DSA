"""
https://leetcode.com/problems/longest-univalue-path/
"""

#OWN
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        longest = 0
        
        def dfs(root, parent):
            nonlocal longest
            if not root:
                return 0
            left = dfs(root.left, root.val)
            right = dfs(root.right, root.val)
            longest = max(longest, left + right)            
            return max(left, right) + 1 if root.val == parent else 0
        
        if not root:
            return 0
        dfs(root, -root.val)
        return longest
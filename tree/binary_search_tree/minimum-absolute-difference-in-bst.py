"""
https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_dis = float('inf')
        prev = None
        
        def dfs(root):
            nonlocal min_dis, prev
            if not root:
                return 
            dfs(root.left)
            if prev is not None:
                min_dis = min(min_dis, root.val - prev)
            prev = root.val
            dfs(root.right)                

        dfs(root)
        return min_dis
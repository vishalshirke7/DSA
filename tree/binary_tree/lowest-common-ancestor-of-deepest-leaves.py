"""
https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
"""


#OWN

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lca, max_depth = root, -1
        def dfs(root, depth):
            nonlocal lca, max_depth
            if not root:
                return True, depth
            left_f, left_d = dfs(root.left, depth + 1)
            right_f, right_d = dfs(root.right, depth + 1)
            if left_f and right_f and left_d == right_d:
                if left_d >= max_depth:
                    lca = root
                    max_depth = left_d
                return True, max(left_d, right_d)
            return left_f or right_f, max(left_d, right_d)
        dfs(root, 0)
        return lca
        
   def lcaDeepestLeaves(self, root):
        def helper(root):
            if not root: return 0, None
            h1, lca1 = helper(root.left)
            h2, lca2 = helper(root.right)
            if h1 > h2: return h1 + 1, lca1
            if h1 < h2: return h2 + 1, lca2
            return h1 + 1, root
        return helper(root)[1]
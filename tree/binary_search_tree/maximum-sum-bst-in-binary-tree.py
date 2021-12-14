"""
https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/
"""

#OWN WORKED
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans
            if not root:
                return None, None, None, True
            left_min, left_max, l_val, l_bst = dfs(root.left)
            right_min, right_max, r_val, r_bst = dfs(root.right)
            if l_bst and r_bst:
                if left_min is None and left_max is None and right_min is None and right_max is None:
                    ans = max(ans, root.val)
                    return root.val, root.val, root.val, True
                if left_min is None and left_max is None:
                    if root.val < right_min and root.val < right_max:
                        ans = max(ans, r_val + root.val)
                        return min(root.val, right_min), max(root.val, right_max), r_val + root.val, True
                    return None, None, None, False
                if right_min is None and right_max is None:
                    if root.val > left_min and root.val > left_max:
                        ans = max(ans, l_val + root.val)
                        return min(root.val, left_min), max(root.val, left_max), l_val + root.val, True
                    return None, None, None, False
                if root.val < right_min and root.val < right_max and root.val > left_min and root.val > left_max:
                    ans = max(ans, l_val + r_val + root.val)
                    return min(root.val, right_min, left_min), max(root.val, right_max, left_max), l_val + r_val + root.val, True
            return None, None, None, False

        dfs(root)
        return ans


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        res = 0
        def traverse(root):
            '''return status_of_bst, size_of_bst, left_bound, right_bound'''
            nonlocal res
            if not root: return 1, 0, None, None # this subtree is empty
            
            ls, l, ll, lr = traverse(root.left)
            rs, r, rl, rr = traverse(root.right)
            
            if ((ls == 2 and lr < root.val) or ls == 1) and ((rs == 2 and rl > root.val) or rs == 1):
                # this subtree is a BST
                size = root.val + l + r
                res = max(res, size)
                return 2, size, (ll if ll is not None else root.val), (rr if rr is not None else root.val)
            return 0, None, None, None # this subtree is not a BST
        
        traverse(root)
        return res        
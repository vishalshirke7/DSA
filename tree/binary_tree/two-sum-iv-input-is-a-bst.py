"""https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
https://www.interviewbit.com/old/problems/2sum-binary-tree/"""

# OWN
class Solution:
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def inorder(root, k):
            nonlocal diff_map
            if not root:
                return False
            if k - root.val in diff_map:
                return True
            diff_map[root.val] = 1
            return inorder(root.left, k) or inorder(root.right, k)
        
        diff_map = dict()
        return inorder(root, k)
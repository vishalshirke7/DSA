"""https://leetcode.com/problems/path-sum/"""

#1. Recusrive 

class Solution:
    
    def dfs(self, root, target, cur_sum):
        if not root:
            return False
        if not root.left and not root.right:
            if cur_sum + root.val == target:
                return True
            return False
        return self.dfs(root.left, target, cur_sum + root.val) or self.dfs(root.right, target, cur_sum + root.val)
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root, targetSum, 0)


# 2. Iterative


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = list()
        def dfs(root, path, prev):
            nonlocal result
            if not root:
                return 
            dfs(root.left, path + [root.val], prev + root.val)
            dfs(root.right, path + [root.val], prev + root.val)
            if not root.left and not root.right:
                if prev + root.val == targetSum:
                    result.append(path + [root.val])
        dfs(root, [], 0)
        return result 
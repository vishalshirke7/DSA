"""
https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
"""

#OWN
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total = 0
        def total_sum(root):
            nonlocal total
            if root:
                total += root.val
                total_sum(root.left)
                total_sum(root.right)
        total_sum(root)
        max_product = 1
        def dfs(root):
            nonlocal max_product
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            tree_sum = left + right + root.val
            max_product = max(max_product, (total - tree_sum) * tree_sum)
            return tree_sum
        dfs(root)
        return max_product % (10**9 + 7)



class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root == None: return 0
            currSum = dfs(root.left) + dfs(root.right) + root.val
            self.ans = max(self.ans, currSum * (self.totalSum - currSum))
            return currSum

        self.ans, self.totalSum = 0, 0
        self.totalSum = dfs(root)  # Firstly, get total sum of all nodes in the Binary Tree
        dfs(root)  # Then dfs in post order to calculate sum of each subtree and its complement
        return self.ans % (10 ** 9 + 7)
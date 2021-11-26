"""
https://leetcode.com/problems/distribute-coins-in-binary-tree/
"""

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0
        def dfs(root):
            nonlocal moves
            if not root:
                return 0
            left_balance = dfs(root.left)
            right_balance = dfs(root.right)
            moves += abs(left_balance) + abs(right_balance)
            return root.val + left_balance + right_balance - 1

        dfs(root)
        return moves

class Solution:
    def distributeCoins(self, root, pre=None):
        if not root:
            return 0
        res = self.distributeCoins(root.left, root) + self.distributeCoins(root.right, root)
        if pre:
            pre.val += root.val - 1
        return res + abs(root.val - 1)

int distributeCoins(TreeNode* r, TreeNode* p = nullptr) {
  if (r == nullptr) return 0;
  int res = distributeCoins(r->left, r) + distributeCoins(r->right, r);
  if (p != nullptr) p->val += r->val - 1;
  return res + abs(r->val - 1);
}
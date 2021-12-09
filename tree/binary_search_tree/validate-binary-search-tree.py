"""
https://leetcode.com/problems/validate-binary-search-tree/
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lower, upper):
            if not root:
                return True
            left = dfs(root.left, lower, root.val)
            right = dfs(root.right, root.val, upper)
            return left and right and lower < root.val < upper
        return dfs(root, -float('inf'), float('inf'))
        

"""
public boolean isValidBST(TreeNode root) {
   if (root == null) return true;
   Stack<TreeNode> stack = new Stack<>();
   TreeNode pre = null;
   while (root != null || !stack.isEmpty()) {
      while (root != null) {
         stack.push(root);
         root = root.left;
      }
      root = stack.pop();
      if(pre != null && root.val <= pre.val) return false;
      pre = root;
      root = root.right;
   }
   return true;
}
"""
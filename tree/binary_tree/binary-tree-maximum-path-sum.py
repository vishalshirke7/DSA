"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_num = -float('inf')
        max_sum = -float('inf')
        
        def dfs(root):
            nonlocal max_sum, max_num
            if not root:
                return 0
            max_num = max(max_num, root.val)
            left = dfs(root.left)
            right = dfs(root.right)
            max_sum = max(max_sum, root.val + left + right)
            max_sum = max(max_sum, root.val + left)
            max_sum = max(max_sum, root.val + right)            
            return max(root.val + left, root.val + right, root.val)
        
        dfs(root)
        return max(max_sum, max_num)

def find_max_sum(root):
    if root is None:
        return 0

    # Recursive calls to children:
    left = find_max_sum(root.left)
    right = find_max_sum(root.right)

    # Max of first three cases:
    return_max = max(max(left, right) + root.val, root.val)

    # Max of all four cases:
    maximum = max(return_max, left + right + root.val)

    # Update globalMax:
    global globalMax
    if maximum > globalMax:
        globalMax = maximum

    return return_max


"""
public class Solution {
    int max = Integer.MIN_VALUE;
    
    public int maxPathSum(TreeNode root) {
        helper(root);
        return max;
    }
    
    // helper returns the max branch 
    // plus current node's value
    int helper(TreeNode root) {
        if (root == null) return 0;
        
        int left = Math.max(helper(root.left), 0);
        int right = Math.max(helper(root.right), 0);
        
        max = Math.max(max, root.val + left + right);
        
        return root.val + Math.max(left, right);
    }
}
"""    
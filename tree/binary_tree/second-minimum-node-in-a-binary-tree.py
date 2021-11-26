"""
https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
"""
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        min1, min2 = root.val, float('inf')
        
        def dfs(root):
            nonlocal min1, min2
            if root:
                if min1 < root.val < min2:
                        min2 = root.val
                elif root.val == min1:
                    dfs(root.left)
                    dfs(root.right)
        
        dfs(root)
        return min2 if min2 < float('inf') else -1


"""
public int findSecondMinimumValue(TreeNode root) {
        if(root.left == null) return -1;
        
        int l = root.left.val == root.val ? findSecondMinimumValue(root.left) : root.left.val;
        int r = root.right.val == root.val ? findSecondMinimumValue(root.right) : root.right.val;
        
        return l == -1 || r == -1 ? Math.max(l, r) : Math.min(l, r);
    }

"""        
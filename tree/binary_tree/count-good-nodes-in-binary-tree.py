"""
https://leetcode.com/problems/count-good-nodes-in-binary-tree/
"""

# Time - O(n), Space - O(h)
class Solution:

    total = 0
    
    def inorder(self, root, cur_max):
        if root:
            if root.val >= cur_max:
                self.total += 1
                cur_max = root.val
            self.inorder(root.left, cur_max)
            self.inorder(root.right, cur_max)
                
    
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.inorder(root, root.val)
        return self.total

"""
    public int goodNodes(TreeNode root) {
        return preorder(root, root.val);
    }
    private int preorder(TreeNode n, int v) {
        if (n == null) // base cases.
            return 0;
        int max = Math.max(n.val, v); // maximum so far on the path.
        return (n.val >= v ? 1 : 0) + preorder(n.left, max) + preorder(n.right, max); // recurse to children.
    }
"""            
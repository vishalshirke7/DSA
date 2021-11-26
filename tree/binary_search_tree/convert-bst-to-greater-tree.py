"""https://leetcode.com/problems/convert-bst-to-greater-tree/"""

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        global_p = 0
        def bst(root):
            nonlocal global_p
            if not root:
                return 0
            bst(root.right)
            global_p += root.val
            root.val = global_p
            left = bst(root.left)
        bst(root)
        return root

"""
public TreeNode convertBST(TreeNode root) {
    dfs(root, 0);
    return root;
}
public int dfs(TreeNode root, int val) {
    if(root == null) return val;
    int right = dfs(root.right, val);
    int left = dfs(root.left, root.val + right);
    root.val = root.val + right;
    return left;
}
"""

class Solution(object):
    def convertBST(self, root):
        total = 0
        
        node = root
        stack = []
        while stack or node is not None:
            # push all nodes up to (and including) this subtree's maximum on
            # the stack.
            while node is not None:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total

            # all nodes with values between the current and its parent lie in
            # the left subtree.
            node = node.left

        return root
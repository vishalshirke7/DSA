"""
https://leetcode.com/problems/balanced-binary-tree/
https://www.interviewbit.com/problems/balanced-binary-tree/
"""
#OWN
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0, True
            left_d, l_bb = dfs(root.left)
            right_d, r_bb = dfs(root.right)
            if l_bb and r_bb:
                if abs(left_d - right_d) > 1:
                    return 0, False
                return 1 + max(left_d, right_d), True
            else:
                return 0, False
        d, bb = dfs(root)
        return bb


"""class solution {
public:
int dfsHeight (TreeNode *root) {
        if (root == NULL) return 0;
        
        int leftHeight = dfsHeight (root -> left);
        if (leftHeight == -1) return -1;
        int rightHeight = dfsHeight (root -> right);
        if (rightHeight == -1) return -1;
        
        if (abs(leftHeight - rightHeight) > 1)  return -1;
        return max (leftHeight, rightHeight) + 1;
    }
    bool isBalanced(TreeNode *root) {
        return dfsHeight (root) != -1;
    }
};

class Solution(object):
    def isBalanced(self, root):
        stack, node, last, depths = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1: return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True        """
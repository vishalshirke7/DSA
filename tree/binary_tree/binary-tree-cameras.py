"""
https://leetcode.com/problems/binary-tree-cameras/
"""

class Solution(object):
    def minCameraCover(self, root):
        self.ans = 0
        covered = {None}

        def dfs(node, par = None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if (par is None and node not in covered or node.left not in covered or node.right not in covered):
                    self.ans += 1
                    covered.update({node, par, node.left, node.right})

        dfs(root)
        return self.ans


class Solution {
    int result = 0;
    
    public int minCameraCover(TreeNode root) {
        Type cover = dfs(root);
        if(cover == Type.LEAF) {
            result++;
        }
        
        return result;
    }
    
    Type dfs(TreeNode node) {
        
        if(node == null) {
            return Type.COVERED;
        }
        
        Type left = dfs(node.left);
        Type right = dfs(node.right);
        
        if(left == Type.LEAF || right == Type.LEAF) {
            result++;
            return Type.PARENT;
        }
        
        return left == Type.PARENT || right == Type.PARENT ? Type.COVERED: Type.LEAF;
    }
    
    static enum Type {
        LEAF, PARENT, COVERED;
    }


class Solution {
    private int NOT_MONITORED = 0;
    private int MONITORED_NOCAM = 1;
    private int MONITORED_WITHCAM = 2;
    private int cameras = 0;
	
    public int minCameraCover(TreeNode root) {
        if (root == null) return 0;
        int top = dfs(root);
        return cameras + (top == NOT_MONITORED ? 1 : 0);
    }
    
    private int dfs(TreeNode root) {
        if (root == null) return MONITORED_NOCAM;
        int left = dfs(root.left);
        int right = dfs(root.right);
        if (left == MONITORED_NOCAM && right == MONITORED_NOCAM) {
            return NOT_MONITORED;
        } else if (left == NOT_MONITORED || right == NOT_MONITORED) {
            cameras++;
            return MONITORED_WITHCAM;
        } else {
            return MONITORED_NOCAM;
        }
    }
}
    
"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""

# OWN
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root 


# iterative solution
def lca(root , v1 , v2):
    # make sure v2 > v1
    if v1 > v2: v1, v2 = v2, v1
    while True:
        if v1 < root.info and v2 < root.info:
            root = root.left
        elif v1 > root.info and v2 > root.info:
            root = root.right
        else:
            return(root)        

"""
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* cur = root;
        while (true) {
            if (p -> val < cur -> val && q -> val < cur -> val) {
                cur = cur -> left;
            } else if (p -> val > cur -> val && q -> val > cur -> val) {
                cur = cur -> right;
            } else {
                break;
            }
        }
        return cur;
    }
};            
"""
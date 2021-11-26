"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
"""

class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def recurse(root):
            nonlocal ans
            if not root:
                return 0
            left = recurse(root.left)
            right = recurse(root.right)
            mid = root == p or root == q
            if mid + left + right >= 2:
                ans = root
            return mid or left or right
        recurse(root)
        return ans

def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
                # If looking for me, return myself
        if root == p or root == q:
            return root
        
        left = right = None
        # else look in left and right child
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        # if both children returned a node, means
        # both p and q found so parent is LCA
        if left and right:
            return root
        else:
        # either one of the chidren returned a node, meaning either p or q found on left or right branch.
        # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is
        # somewhere below node where 'p' was found we dont need to search all the way, 
        # because in such scenarios, node where 'p' found is LCA
            return left or right


def lowestCommonAncestor(self, root, p, q):
    if root in (None, p, q): return root
    left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
    return root if left and right else left or right


def lowestCommonAncestor(self, root, p, q):
    if root in (None, p, q): return root
    subs = [self.lowestCommonAncestor(kid, p, q)
            for kid in (root.left, root.right)]
    return root if all(subs) else max(subs)            
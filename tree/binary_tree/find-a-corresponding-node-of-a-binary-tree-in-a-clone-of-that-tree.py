"""https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/"""

# 1. DFS Recursive Inorder

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def inorder(original, cloned):
            nonlocal ans
            if original:
                inorder(original.left, cloned.left)
                if original == target:
                    ans = cloned
                inorder(original.right, cloned.right)

        ans = None
        inorder(original, cloned) 
        return ans
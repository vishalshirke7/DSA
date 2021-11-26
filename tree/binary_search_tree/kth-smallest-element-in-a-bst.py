"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""
#OWN
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = list()
        def dfs(root):
            if root:
                total = 0
                if root.left:
                    total += dfs(root.left)
                if total == k:
                    return 
                dfs(root.right)
        dfs(root)
        return inorder[k-1]


def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    ans = -1
    index = 1
    def dfs(root):
        nonlocal ans, index
        if not root:
            return 
        dfs(root.left)
        if k == index:
            ans = root.val
            index += 1
            return 
        else:
            index += 1
        dfs(root.right)
    dfs(root)
    return ans

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right    
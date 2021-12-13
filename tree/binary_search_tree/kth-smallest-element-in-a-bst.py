"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""
#OWN
class Solution:
    def kthSmallest(self, root, k):
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []    
        return inorder(root)[k - 1]


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
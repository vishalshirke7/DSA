"""
https://leetcode.com/problems/recover-binary-search-tree/
"""

# OWN
#O(nlogn)
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        inorder = []
        node1, node2 = None, None
        def dfs(root):
            nonlocal inorder
            if root:
                if root.left:
                    dfs(root.left)
                inorder.append(root.val)
                if root.right:
                    dfs(root.right)        
        index = 0
        def dfs1(root):
            nonlocal node1, node2, index
            if root:
                if root.left:
                    dfs1(root.left)
                if root.val != inorder[index]:
                    if not node1:
                        node1 = root
                    elif not node2:
                        node2 = root
                    else:
                        return
                index += 1
                if root.right:
                    dfs1(root.right)
        dfs(root)
        inorder.sort()
        dfs1(root)
        node1.val, node2.val = node2.val, node1.val



class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        prev, node1, node2 = None, None, None
        def inorder(root):
            nonlocal prev, node1, node2
            if root:
                inorder(root.left)
                if prev and prev.val > root.val:
                    if not node1:
                        node1 = prev
                    if node1 and (not node2):
                        node2 = root
                prev = root
                inorder(root.right)
        inorder(root)
        node1.val, node2.val = node2.val, node1.val



def recoverTree(self, root):
    cur, prev, drops, stack = root, TreeNode(float('-inf'))
    while cur or stack:                                                    
        while cur:                                                         
            stack.append(cur)                                              
            cur = cur.left                                                 
        node = stack.pop()                                                 
        if node.val < prev.val: drops.append((prev, node))                 
        prev, cur = node, node.right                                       
    drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val         
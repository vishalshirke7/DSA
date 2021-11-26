"""
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
"""

# Recursive O(n^2)

class Solution:
    
    def find_max_index(self, ls, start, val):
        for index in range(start, len(ls)):
            if ls[index] > val:
                return index
        return len(ls)
    
    def bst(self, ls):
        if not ls:
            return None
        node = TreeNode(ls[0])
        max_index = self.find_max_index(ls, 1, ls[0])
        node.left = self.bst(ls[1:max_index])
        node.right = self.bst(ls[max_index:])
        return node
    
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.bst(preorder)
        
# Stack O(n)

class Solution:

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        for val in preorder[1:]:
            node = TreeNode(val)
            if val < stack[-1]:
                stack[-1].left = node
                stack.append(node)
            else:
                while stack[-1] < val:
                    last = stack.pop()
                last.right = node
                stack.append(node)
        return root

# 3. O(n)

i = 0
def bstFromPreorder(self, A, bound=float('inf')):
    if self.i == len(A) or A[self.i] > bound:
        return None
    root = TreeNode(A[self.i])
    self.i += 1
    root.left = self.bstFromPreorder(A, root.val)
    root.right = self.bstFromPreorder(A, bound)
    return root
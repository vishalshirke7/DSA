"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
https://www.interviewbit.com/old/problems/construct-binary-tree-from-inorder-and-preorder/
"""

#OWN

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = dict()
        for index, val in enumerate(inorder):
            inorder_index_map[val] = index
        pre_index = 0
        def construct(mid, left, right):
            nonlocal pre_index
            node = TreeNode(inorder[mid])
            if mid == left == right:
                return node
            if mid != left:
                pre_index += 1
                node.left = construct(inorder_index_map[preorder[pre_index]], left, mid - 1)
            if mid != right:
                pre_index += 1
                node.right = construct(inorder_index_map[preorder[pre_index]], mid + 1, right)
            return node
        return construct(inorder_index_map[preorder[pre_index]], 0, len(preorder) - 1)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def array_to_tree(left, right):
            nonlocal preorder_index
            if left > right: return None
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)
            preorder_index += 1
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)
            return root

        preorder_index = 0
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)


class Solution:
    def buildTree(self, A, B):
        if not A or not B:
            return None            
        p_idx = 1
        i_idx = 0        
        root = current = TreeNode(A[0])        
        stack = [current]        
        while p_idx < len(A):
            if stack and stack[-1].val == B[i_idx]:
                while stack and stack[-1].val == B[i_idx]:
                    i_idx += 1
                    current = stack.pop()
                    
                current.right = TreeNode(A[p_idx])
                current = current.right
            else:
                current.left = TreeNode(A[p_idx])
                current = current.left
                
            stack.append(current)
            p_idx += 1
            
        return root

def buildTree(self, preorder, inorder):
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(preorder, inorder[0:ind])
        root.right = self.buildTree(preorder, inorder[ind+1:])
        return root        
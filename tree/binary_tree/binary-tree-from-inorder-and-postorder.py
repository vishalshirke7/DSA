"""
https://www.interviewbit.com/old/problems/binary-tree-from-inorder-and-postorder/
"""
#OWN
class Solution:
    def buildTree(self, A, B):
        inorder_index_map = dict()
        for index, val in enumerate(A):
            inorder_index_map[val] = index
        pre_index = len(B) - 1
        def construct(mid, left, right):
            nonlocal pre_index
            node = TreeNode(A[mid])
            if mid == left == right:
                return node
            if mid != right:
                pre_index -= 1
                node.right = construct(inorder_index_map[B[pre_index]], mid + 1, right)                
            if mid != left:
                pre_index -= 1
                node.left = construct(inorder_index_map[B[pre_index]], left, mid - 1)
            return node
        return construct(inorder_index_map[B[pre_index]], 0, len(B) - 1)


class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder:return None
        root = postorder.pop()
        i = inorder.index(root)
        return TreeNode(root, self.buildTree(inorder[:i], postorder[:i]), self.buildTree(inorder[i+1:], postorder[i:]))


class Solution:
    def buildTree(self, inorder, postorder):
        self.postIdx, mp = len(postorder)-1, {val: idx for idx, val in enumerate(inorder)}
        def build(inStart, inEnd):
            if inStart > inEnd: return None
            root = TreeNode(postorder[self.postIdx])
            self.postIdx -= 1
            root.right = build(mp[root.val]+1, inEnd)
            root.left  = build(inStart, mp[root.val]-1)
            return root        
        return build(0, len(inorder)-1)                

# ITERATIVE
class Solution:
    def buildTree(self, A, B):
        post = B
        ino = A
        root = TreeNode(post.pop())
        stack = [root]
        while True:
            if ino[-1] == stack[-1].val:
                temp = stack.pop()
                ino.pop()
                if len(ino) == 0:
                    break
                if stack:
                    if ino[-1] == stack[-1].val:
                        continue
                temp.left = TreeNode(post.pop())
                stack.append(temp.left)
            else:
                temp = TreeNode(post.pop())
                stack[-1].right = temp
                stack.append(temp)
            # print(stack[-1].val,ino[0])
        return root        
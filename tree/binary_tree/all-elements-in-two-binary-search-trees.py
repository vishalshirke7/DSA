"""https://leetcode.com/problems/all-elements-in-two-binary-search-trees/"""

# 1. Recusrive
class Solution:
    
    def inorder(self, root, values):
        if not root:
            return
        self.inorder(root.left, values)
        values.append(root.val)
        self.inorder(root.right, values)
            
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1, l2 = list(), list()
        self.inorder(root1, l1)
        self.inorder(root2, l2)
        l1 += l2
        return sorted(l1)


# 2. Simultaneous Inorder 

def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
    stack1, stack2, result = list(), list(), list()
    while stack1 or stack2 or root1 or root2:
        while root1:
            stack1.append(root1)
            root1 = root1.left
        while root2:
            stack2.append(root2)
            root2 = root2.left
        if not stack2 or (stack1 and stack1[-1].val <= stack2[-1].val):
            root1 = stack1.pop()
            result.append(root1.val)
            root1 = root1.right
        else:
            root2 = stack2.pop()
            result.append(root2.val)
            root2 = root2.right
    return result
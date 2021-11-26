"""https://leetcode.com/problems/binary-search-tree-iterator/"""

# OWN - Space O(h), hasNext - O(1), next - O(1) average
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.inorder(root)
        
    def inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left
        
    def next(self) -> int:
        top = self.stack.pop()
        self.inorder(top.right)
        return top.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
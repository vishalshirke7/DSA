"""
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

#RECURSIVE
def inorder(self, root, res):
    if root:
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

def inorderTraversal(root):
    res = list()
    self.inorder(root, res)
    return res



#ITERATIVE
def inorderTraversal(root):
	stack = []
	result = []
	cur = root
	while cur or stack:
		while cur:
			stack.append(cur)
			cur = cur.left
		cur = stack.pop()
		result.append(cur.val)
		cur = cur.right
	return result

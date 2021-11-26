"""
https://leetcode.com/problems/n-ary-tree-preorder-traversal/
"""


from collections import deque

# Recursive
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = list()
        self.dfs(root, output)
        return output
    
    def dfs(self, root, output):
        if not root:
            return None
        output.append(root.val)
        for child in root.children:
            self.dfs(child, output)


# Iterative
def preorder(self, root: 'Node') -> List[int]:
    stack = list()
    output = list()
    if not root:
        return output
    stack.append(root)
    while stack:
        cur = stack.pop()
        output.append(cur.val)
        temp = list()
        for child in cur.children:
            if child:
                temp = [child] + temp
        stack += temp
    return output
        
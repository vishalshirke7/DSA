"""
https://leetcode.com/problems/n-ary-tree-postorder-traversal/
"""
from collections import deque

# RECURSIVE OWN
class Solution:
    
    def dfs(self, root, op):
        for child in root.children:
            if child:
                self.dfs(child, op)
        op.append(root.val)
                
    def postorder(self, root: 'Node') -> List[int]:
        op = list()
        if not root:
            return op
        self.dfs(root, op)
        return op


# ITERATIVE OWN
class Solution:
    
    def postorder(self, root: 'Node') -> List[int]:
        output = list()
        queue = deque()
        if not root:
            return output
        queue.append(root)
        visited = list()
        while queue:
            top = queue[0]
            if top.children and top not in visited:
                visited.append(top)
                childrens = len(top.children)
                for child in range(childrens - 1, -1, -1):
                    queue.appendleft(top.children[child])
            else:
                output.append(queue.popleft().val)
        return output

# Editorial
def postorder(self, root):
    if root == None:
        return []
    
    stack = [root]
    ret = []
    prev = None
    
    while len(stack) > 0:
        peek = stack[len(stack)-1]
        
        isLeaf = len(peek.children) == 0
        
        isChildDone = not isLeaf and prev == peek.children[len(peek.children)-1]
        
        if isLeaf or isChildDone:
            ret.append(peek.val)
            stack.pop()
            prev = peek
        else:
            for child in reversed(peek.children):
                stack.append(child)
    
    return ret        
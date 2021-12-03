"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""
from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        output = list()
        if not root:
            return output
        queue.append(root)
        while queue:
            level = [node.val for node in queue]
            output.append(level)
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
        return output[::-1]


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def dfs(root, depth):
            nonlocal result
            if not root:
                return
            if depth < len(result):
                result[depth].append(root.val)
            else:
                result.append([root.val])
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 0)        
        return result[::-1]        

# dfs recursively
def levelOrderBottom1(self, root):
    res = []
    self.dfs(root, 0, res)
    return res

def dfs(self, root, level, res):
    if root:
        if len(res) < level + 1:
            res.insert(0, [])
        res[-(level+1)].append(root.val)
        self.dfs(root.left, level+1, res)
        self.dfs(root.right, level+1, res)

# dfs + stack
def levelOrderBottom2(self, root):
    stack = [(root, 0)]
    res = []
    while stack:
        node, level = stack.pop()
        if node:
            if len(res) < level+1:
                res.insert(0, [])
            res[-(level+1)].append(node.val)
            stack.append((node.right, level+1))
            stack.append((node.left, level+1))
    return res
 
# bfs + queue   
def levelOrderBottom(self, root):
    queue, res = collections.deque([(root, 0)]), []
    while queue:
        node, level = queue.popleft()
        if node:
            if len(res) < level+1:
                res.insert(0, [])
            res[-(level+1)].append(node.val)
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
    return res        
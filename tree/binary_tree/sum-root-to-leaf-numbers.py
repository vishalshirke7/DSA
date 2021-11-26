"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/

"""
from collections import deque

# 1. Recursive DFS
class Solution:
    total = 0
    def dfs(self, root, cur_sum):
        if not root:
            return 
        cur_sum = cur_sum * 10 + root.val
        if not root.left and not root.right:
            self.total += cur_sum
        else:
            self.dfs(root.left, cur_sum)
            self.dfs(root.right, cur_sum)
            
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0)
        return self.total


# 2. BFS 
class Solution:
            
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        if not root:
            return 0
        queue.append(root)
        total = 0
        while queue:
            cur_node = queue.popleft()
            if not cur_node.left and  not cur_node.right:
                total += cur_node.val
            if cur_node.right:
                cur_node.right.val += (10 * cur_node.val)
                queue.append(cur_node.right)
            if cur_node.left:
                cur_node.left.val += (10 * cur_node.val)
                queue.append(cur_node.left)
        return total


# 3. DFS with stack

def sumNumbers(self, root): # DFS with stack
    stack, res = [], 0
    if root:
        stack.append(root)
    while stack:
        node = stack.pop()
        if not node.left and not node.right:
            res += node.val
        if node.right:
            node.right.val += node.val*10
            stack.append(node.right)
        if node.left:
            node.left.val += node.val*10
            stack.append(node.left)
    return res


class Solution:
    # @param A : root node of tree
    # @return an integer
    total = 0
    def sumNumbers(self, A):
        
        def dfs(root, parent_val):
            if root.left:
               dfs(root.left, ((10 * parent_val) + root.val))
            if root.right:
               dfs(root.right, ((10 * parent_val) + root.val))
            if not root.left and not root.right:
                self.total += ((parent_val * 10) + root.val)
            
        dfs(A, 0)
        # print(self.total)
        # self.total -= root.val
        return self.total % 1003    
"""https://leetcode.com/problems/deepest-leaves-sum/"""

#OWN
class Solution:
    
    def depth(self, root):
        if not root or (not root.left and not root.right):
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))    
    
    def get_total(self, root, height, depth):
        if not root:
            return 0
        if not root.left and not root.right:
            if height == depth:
                return root.val
            return 0
        return self.get_total(root.left, height + 1, depth) + self.get_total(root.right, height + 1, depth)
                
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        depth = self.depth(root)
        total = self.get_total(root, 0, depth)  
        return total


#2. 
def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    level = [root]
    prev = level
    while level:
        prev, level = level, [child for node in level for child in [node.left, node.right] if child]
    return sum(prev.val for node in prev)


#3. 
class Solution:
    total, max_d = 0, 0
    def dfs(self, root, cur_d):
        if not root:
            return 0
        if not root.left and not root.right:
            if cur_d == self.max_d:
                self.total += root.val
            elif cur_d > self.max_d:
                self.total = root.val                
                self.max_d = cur_d
        self.dfs(root.left, cur_d + 1)
        self.dfs(root.right, cur_d + 1)
    
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0)
        return self.total    
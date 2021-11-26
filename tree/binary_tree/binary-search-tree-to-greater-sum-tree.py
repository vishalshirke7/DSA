"""https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/"""

#OWN

class Solution:
    
    def inorder(self, root, values, modified):
        if not root:
            return None
        self.inorder(root.left, values, modified)
        if modified:
            root.val = values.popleft()
        else:
            values.append(root.val)
        self.inorder(root.right, values, modified)
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        values = deque()
        temp = root
        self.inorder(temp, values, False)
        total = sum(values)
        for index in range(len(values)):
            total -= values[index]
            values[index] += total
        self.inorder(root, values, True)
        return root

#OWN
class Solution:
    
    def dfs(self, root, val):
        if not root:
            return val
        right_sum = self.dfs(root.right, val)
        cur_sum = right_sum + root.val
        root.val = cur_sum
        left_sum = self.dfs(root.left, cur_sum)
        return left_sum
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        temp = root
        self.dfs(temp, 0)
        return root        


# Discuss Reversed Inorder 
class Solution:
    
    total = 0
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root.right:
            self.bstToGst(root.right)
        self.total += root.val
        root.val = self.total
        if root.left:
            self.bstToGst(root.left)
        return root        


"""
 public TreeNode bstToGst(TreeNode root) {
        Deque<TreeNode> stk = new ArrayDeque<>();
        TreeNode cur = root;
        int sum = 0;
        while (cur != null || !stk.isEmpty()) {
            while (cur != null) { // save right-most path of the current subtree
                stk.push(cur);
                cur = cur.right;
            }
            cur = stk.pop(); // pop out by reversed in-order.
            sum += cur.val; // update sum.
            cur.val = sum; // update node value.
            cur = cur.left; // move to left branch.
        }    
        return root;
    }
"""
"""
https://leetcode.com/problems/path-sum-iii/
"""
# Brute Force O(n^2)

class Solution:
    
    def dfs(self, root, rem_sum):
        if not root:
            return 0
        return (1 if rem_sum == root.val else 0) + self.dfs(root.left, rem_sum - root.val) + self.dfs(root.right, rem_sum - root.val)
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return self.dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

# O(n) - prefix_sum
class Solution:

    def dfs(self, root, cur_sum, target, prefix_map):
        if not root:
            return 0
        cur_sum += root.val
        paths = prefix_map.get(cur_sum - target, 0)
        prefix_map[cur_sum] = prefix_map.get(cur_sum, 0) + 1
        paths += self.dfs(root.left, cur_sum, target, prefix_map) + self.dfs(root.right, cur_sum, target, prefix_map)
        prefix_map[cur_sum] -= 1
        return paths
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_map = {0:1}
        return self.dfs(root, 0, targetSum, prefix_map)
        

# 2.

class Solution(object):
    def pathSum(self, root, target):
        self.result = 0
        cache = {0:1}
        self.dfs(root, target, 0, cache)
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        if root is None:
            return  
        currPathSum += root.val
        oldPathSum = currPathSum - target
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        cache[currPathSum] -= 1

# 3. 
def pathSum(self, root, s):
        def dfs(root, curr_s):
            curr_s += root.val
            res[0] += pre_sums.get(curr_s - s, 0)
            pre_sums[curr_s] = pre_sums.get(curr_s, 0) + 1
            if root.left:
                dfs(root.left, curr_s)
            if root.right:
                dfs(root.right, curr_s)
            pre_sums[curr_s] -= 1
            if pre_sums[curr_s] == 0:
                del pre_sums[curr_s]
        
        res = [0]
        pre_sums = {0: 1}
        if not root:
            return res[0]
        dfs(root, 0)
        return res[0]        
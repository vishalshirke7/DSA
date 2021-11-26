"""https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/"""

# BFS
def maxLevelSum(self, root: TreeNode) -> int:
    max_sum, level, maxLevel = -float('inf'), 0, 0
    q = collections.deque()
    q.append(root)
    while q:
        level += 1
        cur_sum = 0
        for _ in range(len(q)):
            node = q.popleft()
            cur_sum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if max_sum < cur_sum:
            max_sum, maxLevel = cur_sum, level        
    return maxLevel


# DFS
def maxLevelSum(root):
    def dfs(node, level_path, level):
        if not node:
            return
        if len(level_path) == level:
            level_path.append(node.val)
        else:
            level_path[level] += node.val
        dfs(node.left, level_path, level + 1)
        dfs(node.right, level_path, level + 1)
    level_path = []    
    dfs(root, level_path, 0)
    return 1 + level_path.index(max(level_path))


def maxLevelSum(self, root: TreeNode) -> int:
    
    sum = [0]*100
    
    def traverse(root,level):
        sum[level] += root.val
        if root.left:
            traverse(root.left,level+1)
        if root.right:
            traverse(root.right,level+1)
            
    traverse(root,0)
    #print(sum)
    return sum.index(max(sum))+1    
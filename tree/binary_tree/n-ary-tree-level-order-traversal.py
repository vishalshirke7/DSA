"""
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
"""
# 1.
# RECURSIVE DFS
class Solution:
    
    def bfs(self, root, level, output):
        if len(output) < level + 1:
            output.append(list())
        output[level].append(root.val)
        for child in root.children:
            if child:
                self.bfs(child, level + 1, output)
        
    def levelOrder(root):
        output = list()
        if not root:
            return output
        self.bfs(root, 0, output)
        return output

#2. BFS
def levelOrder(root):
    q, ret = [root], []
    while any(q):
        ret.append([node.val for node in q])
        q = [child for node in q for child in node.children if child]
    return ret

# 3. BFS
def levelOrder(root):
    if root == None: return []
    q = deque([root])
    ans = []
    while q:
        level = []
        for _ in range(len(q)):
            curr = q.popleft()
            level.append(curr.val)
            for child in curr.children:
                q.append(child)
        ans.append(level)
    return ans
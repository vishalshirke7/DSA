"""https://leetcode.com/problems/path-sum-ii/"""

from collections import deque

# Recursive
class Solution:
        
    def dfs(self, root, cur_sum, ls, res):
        if root:
            if not root.left and not root.right and cur_sum == root.val:
                ls.append(root.val)
                res.append(ls)
            self.dfs(root.left, cur_sum-root.val, ls+[root.val], res)
            self.dfs(root.right, cur_sum-root.val, ls+[root.val], res)
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, targetSum, [], res)
        return res


#BFS Queue
class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = deque()
        queue.append((root, root.val, [root.val]))
        while queue:
            node, val, path = queue.popleft()
            if not node.left and not node.right and val == targetSum:
                result.append(path)
            if node.left:
                queue.append((node.left, val + node.left.val, path + [node.left.val]))
            if node.right:
                queue.append((node.right, val + node.right.val, path + [node.right.val]))
        return result

# DFS Stack I:

def pathSum4(self, root, sum): 
    if not root:
        return []
    res = []
    stack = [(root, sum-root.val, [root.val])]
    while stack:
        curr, val, ls = stack.pop()
        if not curr.left and not curr.right and val == 0:
            res.append(ls)
        if curr.right:
            stack.append((curr.right, val-curr.right.val, ls+[curr.right.val]))
        if curr.left:
            stack.append((curr.left, val-curr.left.val, ls+[curr.left.val]))
    return res 
    
# DFS + stack II   
def pathSum5(self, root, s): 
    if not root:
        return []
    res = []
    stack = [(root, [root.val])]
    while stack:
        curr, ls = stack.pop()
        if not curr.left and not curr.right and sum(ls) == s:
            res.append(ls)
        if curr.right:
            stack.append((curr.right, ls+[curr.right.val]))
        if curr.left:
            stack.append((curr.left, ls+[curr.left.val]))
    return res



    """
    def getMaxToys (N, P, k, x, toys):
    max_toys = sum(toys)
    prefix = list()
    for index in range(N):
        prefix.append(abs(x[index] - P))
    start, end = 0, N - 1
    steps = 0
    while start < end:
        steps = prefix[start] + prefix[end]
        if steps <= k:
            return max_toys
        if prefix[start] > k:
            max_toys -= toys[start]
            start += 1
        else:
            max_toys -= toys[end]
            end -= 1
    return max_toys

T = int(input())
for _ in range(T):
    N ,P, k = map(int, input().split())
    x = list(map(int, input().split()))
    toys = list(map(int, input().split()))

    out_ = getMaxToys(N, P, k, x, toys)
    print (out_)

    
10 20 39
-17 -15 -11 -9 -3 2 5 11 13 14
72 16 22 72 18 86 61 22 85 72

72
526

10 9 15
-18 -6 -1 1 7 11 12 16 17 20
77 50 73 86 57 50 6 27 91 76
10 -13 8
-19 -18 -12 -11 -9 -6 -3 4 12 19
46 73 77 32 77 76 14 21 46 16
10 -19 35
-20 -11 -2 1 2 8 9 10 15 16
87 54 81 45 100 26 93 17 24 77

307
262
517
"""
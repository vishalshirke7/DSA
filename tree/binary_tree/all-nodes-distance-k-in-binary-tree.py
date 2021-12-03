"""
https://www.interviewbit.com/old/problems/nodes-at-distance-k/
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
https://www.geeksforgeeks.org/print-nodes-distance-k-given-node-binary-tree/
"""

from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent=None):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        visited = set()
        visited.add(target)
        queue = deque()
        queue.append((target, 0))
        while queue:
            if queue[0][1] == k:
                return [node.val for node, distance in queue]
            node, distance = queue.popleft()            
            for neighbour in [node.parent, node.left, node.right]:
                if neighbour and neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, distance + 1))
        return []



class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        result = []
        path_map = dict()

        def find_target_path(root):
            if not root:
                return -1
            if root == target:
                path_map[root] = 0
                return 0
            left = find_target_path(root.left)
            if left >= 0:
                path_map[root] = left + 1
                return left + 1
            right = find_target_path(root.right)
            if right >= 0:
                path_map[root] = right + 1
                return right + 1
            return -1

        def dfs(root, route_sum):
            if root:
                if root in path_map:
                    route_sum = path_map[root]
                if route_sum == k:
                    result.append(root.val)
                dfs(root.left, route_sum + 1)
                dfs(root.right, route_sum + 1)
        find_target_path(root)
        dfs(root, path_map.get(root, 0))
        return result
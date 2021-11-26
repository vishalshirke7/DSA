"""
https://leetcode.com/problems/validate-binary-tree-nodes/
"""

from collections import deque

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = 0
        all_childs = leftChild + rightChild
        for index in range(n):
            if index not in all_childs:
                root = index
        queue, visited = deque(root), set()
        while queue:
            node = queue.popleft()
            if node in visited:
                return False
            visited.add(node)
            if leftChild[node] != -1:
                queue.append(leftChild[node])
            if rightChild[node] != -1:
                queue.append(rightChild[node])
        return len(visited) == n

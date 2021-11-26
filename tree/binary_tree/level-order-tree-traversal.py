"""https://www.geeksforgeeks.org/level-order-tree-traversal/"""
from collections import deque


# 1. Iterative
def levelOrder(root):
    queue = deque()
    level_order = list()
    if not root:
        return level_order
    queue.append(root)
    while queue:
        cur_node = queue.popleft()
        level_order.append(cur_node.data)
        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)
    return level_order


# 2. 
def levelOrder(root):
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
    return output
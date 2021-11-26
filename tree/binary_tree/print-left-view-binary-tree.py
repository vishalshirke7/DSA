"""https://www.geeksforgeeks.org/print-left-view-binary-tree/"""

from collections import deque

# OWN
def LeftView(root):
    prev_level = -1
    left = list()
    queue = deque()
    if not root:
        return left
    queue.append((root, 0))
    while queue:
        element = queue.popleft()
        cur_node = element[0]
        cur_level = element[1]
        if cur_level > prev_level:
            prev_level = cur_level
            left.append(cur_node.data)
        if cur_node.left:
            queue.append((cur_node.left, cur_level + 1))
        if cur_node.right:
            queue.append((cur_node.right, cur_level + 1))
    return left
    


def printRightView(root):
 
    if (not root):
        return
 
    q = []
    q.append(root)
 
    while (len(q)):
 
        # number of nodes at current level
        n = len(q)
 
        # Traverse all nodes of current level
        for i in range(1, n + 1):
            temp = q[0]
            q.pop(0)
 
            # Print the left most element
            # at the level
            if (i == 1):
                print(temp.data, end=" ")
 
            # Add left node to queue
            if (temp.left != None):
                q.append(temp.left)
 
            # Add right node to queue
            if (temp.right != None):
                q.append(temp.right)

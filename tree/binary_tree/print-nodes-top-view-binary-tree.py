"""
https://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/
"""

import collections
class Solution:
    
    def topView(self,root):
        col_map = dict()
        queue = collections.deque()
        queue.append((root, 0))
        col_map[0] = root.data
        while queue:
            for i in range(len(queue)):
                cur_node, index = queue.popleft()
                if index not in col_map:
                    col_map[index] = cur_node.data
                if cur_node.left:
                    queue.append((cur_node.left, index - 1))
                if cur_node.right:
                    queue.append((cur_node.right, index + 1))
        
        col_map = sorted(col_map.items(), key=lambda x:x[0])
        return [val[1] for val in col_map]

def topView(head, dis, level, dict):

    if head is None:
        return

    if dis not in dict or level < dict[dis][1]:
        dict[dis] = (head.key, level)
    topView(head.left, dis - 1, level + 1, dict)
    topView(head.right, dis + 1, level + 1, dict)

def printTopView(head):
    dict = {}

    topView(head, 0, 0, dict)
    for key in sorted(dict.keys()):
        print(dict.get(key)[0], end=' ')               
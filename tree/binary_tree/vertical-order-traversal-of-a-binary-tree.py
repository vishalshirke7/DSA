"""
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
"""

#OWN
import collections

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_map = collections.defaultdict(list)
        queue = collections.deque()
        queue.append((root, 0))
        while queue:
            level_dict = collections.defaultdict(list)
            for i in range(len(queue)):
                cur_node, index = queue.popleft()
                level_dict[index].append(cur_node.val)
                if cur_node.left:
                    queue.append((cur_node.left, index - 1))
                if cur_node.right:
                    queue.append((cur_node.right, index + 1))                    
            for index, values in level_dict.items():
                col_map[index].extend(sorted(values))
        sorted_order = sorted(col_map.items(), key=lambda x:x[0])        
        return [val[1] for val in sorted_order]
"""
https://leetcode.com/problems/count-nodes-with-the-highest-score/
"""

import collections

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        graph = collections.defaultdict(list)
        for node, parent in enumerate(parents):
            graph[parent].append(node)
        max_product_map = collections.Counter()
        nodes = len(parents)

        def dfs(node):
            product, total_nodes = 1, 0
            for child in graph[node]:
                child_total_nodes = dfs(child)
                product *= child_total_nodes
                total_nodes += child_total_nodes
            product *= max(1, nodes - 1 - total_nodes)
            max_product_map[product] += 1
            return total_nodes + 1

        dfs(0)
        return max_product_map[max(max_product_map.keys())]


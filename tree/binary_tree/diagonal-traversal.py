"""
https://www.interviewbit.com/old/problems/diagonal-traversal/
"""

#OWN
class Solution:
    def solve(self, A):
        result = list()
        def dfs(node, d):
            nonlocal result
            if not node:
                return
            dfs(node.right, d)
            if d > len(result):
                result.append([node.val])
            else:
                result[d - 1].append(node.val)
            dfs(node.left, d + 1)
        dfs(A, 1)
        final = []
        for res in result:
            final += res[::-1]
        return final


import collections  

class Solution:
    def solve(self, A):
        result = collections.defaultdict(list)
        def dfs(node, d):
            nonlocal result
            if not node:
                return
            result[d].append(node.val)
            dfs(node.left, d + 1)
            dfs(node.right, d)
        dfs(A, 0)
        final = []
        start = 0 
        while start in result:
            final += result[start]
            start += 1
        return final        
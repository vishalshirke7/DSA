"""
https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
"""
#OWN
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        if not traversal:
            return None
        index, stack = 0, []
        while index < len(traversal):
            level, number = 0, ""
            while index < len(traversal) and traversal[index] == '-':
                level += 1
                index += 1
            while index < len(traversal) and traversal[index] != '-':
                number += traversal[index]
                index += 1
            cur_node = TreeNode(int(number))
            if stack and level > stack[-1][1]:
                stack[-1][0].left = cur_node
            else:
                while stack and stack[-1][1] >= level:
                    stack.pop()
                if stack:
                    stack[-1][0].right = cur_node
            stack.append((cur_node, level))
        return stack[0][0]


  def recoverFromPreorder(self, S):
        stack, i = [], 0
        while i < len(S):
            level, val = 0, ""
            while i < len(S) and S[i] == '-':
                level, i = level + 1, i + 1
            while i < len(S) and S[i] != '-':
                val, i = val + S[i], i + 1
            while len(stack) > level:
                stack.pop()
            node = TreeNode(val)
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]        
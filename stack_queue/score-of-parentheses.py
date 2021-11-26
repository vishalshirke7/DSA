"""
https://leetcode.com/problems/score-of-parentheses/
"""

# OWN
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = list()
        for char in s:
            if char == '(':
                stack.append('(')
            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    total = 0
                    while stack[-1] != '(':
                        total += stack.pop()
                    stack.pop()
                    stack.append(total * 2)
        return sum(stack)


def scoreOfParentheses(self, S):
    stack, cur = [], 0
    for i in S:
        if i == '(':
            stack.append(cur)
            cur = 0
        else:
            cur += stack.pop() + max(cur, 1)
    return cur        
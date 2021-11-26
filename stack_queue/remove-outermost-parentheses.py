"""
https://leetcode.com/problems/remove-outermost-parentheses/
"""

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = list()
        openb = 0
        for char in s:
            if char == '(' and openb > 0:
                res.append('(')
            elif char == ')' and openb > 1:
                res.append(')')
            openb += 1 if char == '(' else -1
        return "".join(res)
            
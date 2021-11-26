"""
https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
"""

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = list()
        for char in s:
            if char == ')':
                cur_str = ""
                while stack and stack[-1] != '(':
                    cur_str += stack.pop()
                stack.pop()
                for c in cur_str:
                    stack.append(c)
            else:
                stack.append(char)
        return "".join(stack)

def reverseParentheses(self, s):
        opened = []
        pair = {}
        for i, c in enumerate(s):
            if c == '(':
                opened.append(i)
            if c == ')':
                j = opened.pop()
                pair[i], pair[j] = j, i
        res = []
        i, d = 0, 1
        while i < len(s):
            if s[i] in '()':
                i = pair[i]
                d = -d
            else:
                res.append(s[i])
            i += d
        return ''.join(res)

# print('Output', reverseParentheses("(u(love)i)"))
print('Output', reverseParentheses("(ed(et(oc))el)"))
# print('Output', reverseParentheses("a(bcdefghijkl(mno)p)q"))

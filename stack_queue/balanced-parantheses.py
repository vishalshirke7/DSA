"""
https://www.interviewbit.com/old/problems/balanced-parantheses/
"""

#own
def solve(A):
    stack = list()
    for char in A:
        if char == '(':
            stack.append('(')
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 0
    if stack:
        return 0
    return 1

#editorial
def solve(string):
    level = 0
    for c in string:
        if c == "(":
            level += 1
        else:
            level -= 1
        if level < 0:
            return 0
    
    if level != 0:
        return 0
    
    return 1    
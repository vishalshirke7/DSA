"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
"""

def minRemoveToMakeValid(s):
    s, stack, output = list(s), list(), [0] * len(s)
    for index in range(len(s)):
        output[index] = s[index]
        if s[index] == '(':
            stack.append(index)
        elif s[index] == ')':
            if stack:
                stack.pop(-1)
            else:
                output[index] = ' '
    while stack:
        output[stack.pop()] = ' '
    op_str = ""
    for val in output:
        if val != ' ':
            op_str += val
    return op_str


print('Output', minRemoveToMakeValid("lee(t(c)o)de)"))
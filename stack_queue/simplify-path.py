"""
https://leetcode.com/problems/simplify-path/
"""


def simplifyPath(path):
    stack = []
    path = path.split('/')
    for val in path:
        if val == '..':
            if stack:
                stack.pop()
        elif val not in ['.', '_', '']:
            stack.append(val)
    op = "/"
    return op + "/".join(stack)


print('Output', simplifyPath("/a/./b/../../c/"))
print('Output', simplifyPath("/home//foo/"))
print('Output', simplifyPath("/../"))
"""
https://leetcode.com/problems/valid-parenthesis-string/
"""

def checkValidString(s):
    open_stack, star_stack = list(), list()
    for index, char in enumerate(s):
        if char == '(':
            open_stack.append(index)
        elif char == '*':
            star_stack.append(index)
        else:
            if open_stack:
                open_stack.pop()
            elif star_stack:
                star_stack.pop()
            else:
                return False
    while open_stack and star_stack:
        if open_stack.pop() > star_stack.pop():
            return False
    return len(open_stack) == 0
            

# print('Output', checkValidString("(*))(*"))
print('Output', checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
# print('Output', checkValidString("(*))"))
# print('Output', checkValidString("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"))



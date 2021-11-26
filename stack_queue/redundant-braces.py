"""
https://www.interviewbit.com/problems/redundant-braces/
"""

def braces(A):
    stack = list()
    for char in A:
        if char == ')':
            count = 0
            while stack.pop() != '(':
                count += 1
            if count == 0 or count == 1:
                return 1
        else:
            stack.append(char)
    return 0



print('Output', braces("((a + b))"))
print('Output', braces("(a+(a+b))"))
print('Output', braces("a+b"))
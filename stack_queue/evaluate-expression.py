"""
https://www.interviewbit.com/old/problems/evaluate-expression/
"""

def evalRPN(A):
    stack = list()
    for val in A:
        print(stack)
        if val not in ['+', '-', '*', '/']:
            stack.append(int(val))
        elif len(stack) >= 2:
            val1 = stack.pop()
            val2 = stack.pop()
            if val == '+':
                res = val1 + val2
            if val == '-':
                res = val2 - val1
            if val == '*':
                res = val1 * val2
            if val == '/':
                res = val2 // val1
            stack.append(res)
        else:
            return None
    return stack[0]


print('Output', evalRPN([ "5", "1", "2", "+", "4", "*", "+", "3", "-" ]))
print('Output', evalRPN([ "4", "13", "5", "/", "+" ]))

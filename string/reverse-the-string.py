"""
https://www.interviewbit.com/problems/reverse-the-string/
"""

def solve(A):
    start = 0
    stack, output = list(), ""
    for index in range(len(A)):
        if A[index].isalpha():
            if not A[start].isalpha():
                start = index
            if index == len(A) - 1 or (index + 1 < len(A) and not A[index + 1].isalpha()):
                stack.append(A[start:index + 1])
                start = index + 1
    for val in stack:
        output = val + " " + output
    return output[:-1]
        


print('Output', solve("       fwbpudnbrozzifml osdt ulc jsx kxorifrhubk ouhsuhf sswz qfho dqmy sn myq igjgip iwfcqq                 "))
# print('Output', solve("  hello world  "))
# print('Output', solve("j"))
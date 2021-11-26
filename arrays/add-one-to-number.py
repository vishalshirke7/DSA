"""
https://www.interviewbit.com/problems/add-one-to-number/
"""

def plusOne(A):
    output, carry = [], 1
    for index in range(len(A) - 1, -1, -1):
        if A[index] + carry > 9:
            output = [(A[index] + carry) % 10] + output
            carry = (A[index] + carry) // 10
        else:
            output = [A[index] + carry] + output
            carry = 0
    if carry:
        output = [carry] + output
    return output



print('Output', plusOne([3,7,6,4,0,5,5,6]))
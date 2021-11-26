"""
https://www.interviewbit.com/old/problems/first-index/
"""

def solve(A, B):
    sorted_A = sorted(A)
    result = [0] * len(B)
    for index_i in range(len(B)):
        for index_j in range(len(A)):
            if B[index_i] > sorted_A[-1]:
                result[index_i] = -1
                break
            elif B[index_i] <= A[index_j]:
                result[index_i] = index_j
                break
    return result



print('Output', solve([ 9, 6, 1, 1 ], [ 4, 1, 10, 8 ]))
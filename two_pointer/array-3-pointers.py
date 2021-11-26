"""
https://www.interviewbit.com/problems/array-3-pointers/
"""


def minimize(A, B, C):
    A_ptr, B_ptr, C_ptr = 0, 0, 0
    A_len, B_len, C_len = len(A), len(B), len(C)
    output = float('inf')
    while A_ptr < A_len and B_ptr < B_len and C_ptr < C_len:
        a, b, c = A[A_ptr], B[B_ptr], C[C_ptr]
        diff = max(a,b,c) - min(a,b,c)
        output = min(diff, output)
        if a <= b and a <= c:
            A_ptr += 1
        elif b <= a and b <= c:
            B_ptr += 1
        else:
            C_ptr += 1
    return output


print('Output', minimize([1, 4, 10], [2, 15, 20], [10, 12]))
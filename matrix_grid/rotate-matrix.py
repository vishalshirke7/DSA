"""
https://www.interviewbit.com/old/problems/rotate-matrix/
"""

def rotate_A_90(A): 
    A_length = len(A)
    for level in range(A_length//2):
        for current_index in range(level, A_length-1-level):
            temp = A[level][current_index]
            A[level][current_index] = A[A_length-1-current_index][level]
            A[A_length-1-current_index][level] = A[A_length-1-level][A_length-1-current_index]
            A[A_length-1-level][A_length-1-current_index] = A[current_index][A_length-1-level]
            A[current_index][A_length-1-level] = temp

            # temp = A[level][current_index]
            # A[level][current_index] = A[current_index][A_length-1-level]
            # A[current_index][A_length-1-level] = A[A_length-1-level][A_length-1-current_index]
            # A[A_length-1-level][A_length-1-current_index] = A[A_length-1-current_index][level]
            # A[A_length-1-current_index][level] = temp
    print(A)


rotate_A_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
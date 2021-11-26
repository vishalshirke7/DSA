"""
https://www.interviewbit.com/problems/maximum-unsorted-subarray/
"""


def subUnsort(A):
    sorted_A = sorted(A)
    if (A == sorted_A):
        return [-1]
    else:
        unsorted_array = [index for index in range(len(A)) if A[index] != sorted_A[index]]
        return [min(unsorted_array), max(unsorted_array)]


def subUnsort(A):
    array_length = len(A)
    A_sorted = sorted(A) 
    start, end = -1, -1
    for index in range(array_length):
        A[index] = A[index] - A_sorted[index]
    for index in range(array_length - 1):
        if(A[0]!=0):
            start=0
            break
        if(A[index] == 0 and A[index+1] != 0):
            start = index + 1
            break
    for index in range(array_length - 1, 0, -1):
        if(A[array_length - 1] != 0):
            end = array_length - 1
            break
        if(A[index] == 0 and A[index - 1] != 0):
            end = index - 1
            break
    if(start == -1 and end ==-1):
        return [-1]
    return [start, end]

print('Output', subUnsort([1, 2, 3, 4, 5, 7, 6]))
print('Output', subUnsort([5,1,1,2,2,3]))
print('Output', subUnsort([1, 3, 2, 4, 5]))
print('Output', subUnsort([1, 1, 1, 1]))
print('Output', subUnsort([1, 2, 3, 4, 5]))
print('Output', subUnsort([1, 1, 10, 10, 15, 10, 15, 10, 10, 15, 10, 15 ]))

"""
Given an array A[] of n positive integers which can contain integers from 1 to P where elements can be repeated or can be absent from the array.
Your task is to count the frequency of all elements from 1 to n.
"""
# def cal():
#     N = 5
#     A = [2,3,2,3,5]
#     for i in range(N):
#         index_to_be_updated = A[i] - 1
#         if A[i] > N:
#             index_to_be_updated = (A[i] % N) - 1
#         A[index_to_be_updated] = A[index_to_be_updated] + N
#     for i in range(N):
#         if A[i] // N == 0:
#             A[i] = 0
#         elif A[i] // N != 0:
#             if A[i] % N == 0:
#                 A[i] = (A[i] // N) - 1
#             else:
#                 A[i] = A[i] // N
#     print(A)

# cal()


def frequencycount(A,N):
    # code here
    i = 0
    while i < N:
        if A[i] <= 0:
            i = i + 1
            continue
        index_to_be_updated = A[i] - 1
        if A[index_to_be_updated] > 0:
            A[i] = A[index_to_be_updated]
            A[index_to_be_updated] = -1
        else:
            A[index_to_be_updated] = A[index_to_be_updated] - 1
            A[i] = 0
            i = i + 1
    for i in range(N):
        A[i] = abs(A[i])
    print(A)

frequencycount([2,3,2,3,5], 5)
"""
https://www.interviewbit.com/old/problems/diffk/
"""

# def diffPossible(self, A, B):
#     if len(A) <= 1:
#         return 0
#     cnt_map = dict()
#     for val in A:
#         cnt_map[val] = cnt_map.get(val, 0) + 1
#     for val in A:
#         if B == 0:
#             if cnt_map[val] > 1:
#                 return 1
#         elif val + B in cnt_map:
#             return 1
#     return 0

def diffPossible(A, B):
    size = len(A)
    if size <= 1:
        return 0    
    start, end = 0, 1
    while end < size:
        diff = A[end] - A[start]
        if diff == B:
            return 1
        elif diff > B:
            start += 1
        else:
            end += 1
    return 0

# print('Output', diffPossible([1, 3, 4, 4], 1))
# print('Output', diffPossible([-1, -1, 0, 1, 2], 0))
print('Output', diffPossible([14, 28, 37, 39, 42, 56, 60, 62, 62, 74, 76, 77, 82, 86, 86, 96], 16))
# print('Output', diffPossible([ 0, 1, 9, 10, 13, 17, 17, 17, 23, 25, 29, 30, 37, 38, 39, 39, 40, 41, 42, 60, 64, 70, 70, 70, 72, 75, 85, 85, 90, 91, 91, 93, 95 ], 83))

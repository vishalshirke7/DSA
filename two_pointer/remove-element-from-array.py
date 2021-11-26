"""
https://leetcode.com/problems/remove-element/
https://www.interviewbit.com/old/problems/remove-element-from-array/
"""

# OWN
def removeElement(A, B):
    start = 0
    for end in range(len(A)):
        if A[end] != B:
            A[start] = A[end]
            start += 1
    return start 
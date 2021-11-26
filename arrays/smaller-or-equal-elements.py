"""
https://www.interviewbit.com/old/problems/smaller-or-equal-elements/
"""


def solve(A, B):
    start, end = 0, len(A) - 1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] <= B:
            if mid + 1 < len(A) and A[mid + 1] <= B:
                start = mid + 1
            else:
                return mid + 1
        else:
            end = mid - 1
    return end + 1

def solve(A, B):
    start = 0
    end = len(A)-1

    while start<=end:
        mid = (start+end)//2
        if A[mid]<=B:
            start = mid+1
        else:
            end = mid-1
    return start

print('Output', solve([1, 3, 4, 4, 6], 1))
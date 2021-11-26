"""
https://www.interviewbit.com/old/problems/search-in-bitonic-array/
"""

# own
def solve(A, B):
    start, end = 0, len(A) - 1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == B:
            return mid
        if end - start <= 1:
            if start == mid:
                return end if A[end] == B else -1
            else:
                return start if A[start] == B else -1
        if A[mid - 1] < A[mid] < A[mid + 1]:
            if B > A[mid]:
                start = mid + 1
            else:
                end = mid - 1
        elif A[mid - 1] < A[mid] > A[mid + 1]:
            if B > A[mid - 1]:
                start = mid + 1
            else:
                end = mid - 1
        elif A[mid - 1] > A[mid] > A[mid + 1]:
            if B > A[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1


print('Output', solve([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21 ], 1))   
# print('Output', solve([ 1, 20, 50, 40, 10 ], 5))   
# print('Output', solve([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31 ], 44))    


def binarySearch(Arr,target) :
    start, end = 0, len(Arr)-1
    while start <= end :
        mid = (start + end) // 2
        if Arr[mid] == target :
            return mid
        elif Arr[mid] < target :
            start = mid + 1
        else :
            end = mid - 1;
    return -1

class Solution:
    def solve(self, A, B):
        start=0
        end=len(A)-1
        while start<end:
            mid=(start+end)//2
            if A[mid-1]<A[mid] and A[mid]<A[mid+1]:
                start=mid+1
            elif A[mid-1]>A[mid] and A[mid]>A[mid+1]:
                end=mid-1
            else:
                break
        A1=A[:mid+1]
        A2=A[mid+1:][::-1]
        # print(A1)
        # print(A2)
        a=binarySearch(A1,B)
        if a!=-1:
            return a
        a=binarySearch(A2,B)
        if a!=-1:
            return len(A)-1-a
        return -1

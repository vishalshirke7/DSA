"""
https://www.interviewbit.com/old/problems/maximum-sum-triplet/
https://www.geeksforgeeks.org/find-maximum-sum-triplets-array-j-k-ai-aj-ak/
"""

from bisect import bisect_left 

def solve(A):

    def BinarySearch(a, x): 
        i = bisect_left(a, x) 
        if i: 
            return (i-1) 
        else: 
            return -1

    maxe = 0
    right_max = len(A) * [0]
    right_max[-1] = A[-1]
    left_elements = [A[0]]
    for index in range(len(A) - 2, -1, -1):
        right_max[index] = max(A[index], A[index + 1])
    for index in range(1, len(A) - 1):
        left_max_min = BinarySearch(left_elements, A[index])
        if left_max_min != -1:
            if right_max[index + 1] <= A[index]:
                continue
            ans = left_elements[left_max_min] + A[index] + right_max[index + 1]
            maxe = max(maxe, ans)
        left_elements.insert(left_max_min + 1, A[index])
    return maxe


# print('Output', solve([2, 5, 3, 1, 4, 9]))
print('Output', solve([ 18468, 6335, 26501, 19170, 15725, 11479, 29359, 26963, 24465, 5706, 28146, 23282, 16828, 9962, 492, 2996, 11943, 4828, 5437, 32392, 14605 ]))

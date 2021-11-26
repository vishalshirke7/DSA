"""
https://www.interviewbit.com/old/problems/3-sum-zero/
"""


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        A.sort()
        op_set, op_list = set(), list()
        for index in range(len(A)):
            start, end = index + 1, len(A) - 1
            while start < end:
                cur_sum = A[index] + A[start] + A[end]
                if cur_sum ==0:
                    if (A[index], A[start], A[end]) not in op_set:
                        op_set.add((A[index], A[start], A[end]))
                        op_list.append([A[index], A[start], A[end]])
                    start += 1
                elif cur_sum > 0:
                    end -= 1
                else:
                    start += 1
        return op_list
"""
https://leetcode.com/problems/merge-sorted-array/
https://www.interviewbit.com/old/problems/merge-two-sorted-lists-ii/
"""


def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n -1
    if m==0:
        for i in range(n):
            nums1[i] = nums2[i]
    elif n == 0:
        pass
    else:
        while j >=0 and i>=0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        while j>=0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


def merge(A, B):
    A_len, B_len = len(A), len(B)
    A += [0] * B_len
    ptr_A, ptr_B =  A_len - 1, B_len - 1
    cur_ptr = (A_len + B_len) - 1
    if A_len == 0:
        for index in range(B_len):
            A[index] = B[index]
    elif B_len == 0:
        pass
    else:
        while ptr_A >= 0 and ptr_B >= 0:
            if A[ptr_A] < B[ptr_B]:
                A[cur_ptr] = B[ptr_B]
                ptr_B -= 1
            else:
                A[cur_ptr] = A[ptr_A]
                ptr_A -= 1
            cur_ptr -= 1
        while ptr_A >= 0:
            A[cur_ptr] = A[ptr_A]
            cur_ptr -= 1
            ptr_A -= 1
        while ptr_B >= 0:
            A[cur_ptr] = B[ptr_B]
            cur_ptr -= 1
            ptr_B -= 1
    print(A)

# print('Output', merge([1,5,8], [6,9]))            
print('Output', merge([1,2], [-1,2]))
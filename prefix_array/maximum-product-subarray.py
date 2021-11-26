"""
https://leetcode.com/problems/maximum-product-subarray/
"""



def maxProduct(nums):
    max_prod, min_prod, ans = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        local_max = max(nums[i], max_prod*nums[i], min_prod*nums[i])
        local_min = min(nums[i], max_prod*nums[i], min_prod*nums[i])
        max_prod, min_prod = local_max, local_min
        ans = max(max_prod, ans)
    return ans

def maxProduct(A):
    B = A[::-1]
    for i in range(1, len(A)):
        A[i] *= A[i - 1] or 1
        B[i] *= B[i - 1] or 1
    return max(A + B)

def maxProduct(A):
    max_so_far, cur_prod = -float('inf'), 1
    for index in range(len(A)):
        cur_prod *= A[index]
        max_so_far = max(max_so_far, cur_prod)
        if cur_prod == 0:
            cur_prod = 1
    cur_prod = 1
    for index in range(len(A) - 1, -1, -1):
        cur_prod *= A[index]
        max_so_far = max(max_so_far, cur_prod)
        if cur_prod == 0:
            cur_prod = 1
    return max_so_far

print("Output", maxProduct([-2,0,-1]))
print("Output", maxProduct([-2,3,-4]))
print("Output", maxProduct([2,3,-2,4]))
"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
https://www.interviewbit.com/old/problems/remove-duplicates-from-sorted-array/
"""

#own
def removeDuplicates(self, A):
    left, right, prev = 0, 1, 0
    while right < len(A):
        if A[left] != A[right]:
            prev += 1                
            A[prev] = A[right]
            left = right
        right += 1
    return prev + 1            


def removeDuplicates(nums):
    if len(nums) < 2:
        return len(nums)
    cur, fast = 0, 1
    while fast < len(nums):
        if nums[fast] <= nums[cur]:
            pass
        else:
            if (cur + 1) != fast:
                nums[cur + 1] = nums[fast]
            if nums[cur + 1] > nums[cur]:
                cur += 1
        fast += 1
    return cur + 1
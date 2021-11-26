"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
https://www.interviewbit.com/old/problems/remove-duplicates-from-sorted-array-ii/
"""


def removeDuplicates(A):
	size = len(A)
	if  size < 3:
		return size
	fast_ptr = 2
	for index in range(2, size):
		if A[fast_ptr - 1] != A[index] or A[fast_ptr - 2] != A[index]:
			A[fast_ptr] = A[index]
			fast_ptr += 1
	return fast_ptr

def removeDuplicates(A):
	size = len(A)
	index = 0
	for val in A:
		if index < 2 or val > A[index - 2]:
			A[index] = val
			index += 1
	return index

# generalized for atMost K
def removeDuplicates(A, K=2):
	start, end, duplicates = 1, 1, 1
	while end < len(A):
		if A[end] != A[end - 1]:
			A[start] = A[end]
			start += 1
			duplicates = 1
		else:
			if duplicates < K:
				A[start] = A[end]
				start += 1
				duplicates += 1
		end += 1
	return start

def removeDuplicates(nums):
	if len(nums) < 2: return len(nums)
    slow, fast = 2, 2

    while fast < len(nums):
        if nums[slow - 2] != nums[fast]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow
    
print('Output', removeDuplicates([1,1,1,2]))
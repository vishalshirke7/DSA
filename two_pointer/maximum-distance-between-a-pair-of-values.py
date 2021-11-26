"""
https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/
"""

#OWN 
def maxDistance(nums1, nums2):
	ptr1 = ptr2 = ans = 0
	nums1_len, nums2_len = len(nums1), len(nums2)
	while ptr1 < nums1_len and ptr2 < nums2_len:
		if nums1[ptr1] <= nums2[ptr2]:
			ans = max(ans, ptr2 - ptr1)
			ptr2 += 1
		else:
			ptr1 += 1
			# ptr2 += 1			
	return ans



print('Output', maxDistance([55,30,5,4,2], [100,20,10,10,5]))
print('Output', maxDistance([2,2,2], [10,10,1]))
print('Output', maxDistance([30,29,19,5], [25,25,25,25,25]))
print('Output', maxDistance([5,4], [3,2]))
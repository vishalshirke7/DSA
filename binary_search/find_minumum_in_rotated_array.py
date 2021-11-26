"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""

"https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/158940/Beat-100%3A-Very-Simple-(Python)-Very-Detailed-Explanation"

# def findMin(nums):
# 	if len(nums) == 1:
# 		return nums[0]
# 	low, high = 0, len(nums) - 1
# 	if nums[low] < nums[high]:
# 		return nums[low]
# 	while low <= high:
# 		mid = (low + high) // 2
# 		if nums[mid] > nums[low]:
# 			low = mid + 1
# 		else:
# 			high = mid - 1		
# 		if nums[mid] > nums[mid + 1]:
# 			return nums[mid + 1]
# 		if nums[mid] < nums[mid - 1]:
# 			return nums[mid]



def findMin(nums):
	left, right = 0, len(nums) - 1
	while left < right:
		mid = (left + right) // 2		
		if nums[mid] > nums[right]:
			left = mid + 1
		else:
			right = mid
	return nums[left]


"""
Really the BEST solution!! Binary search always bothers me, thanks for sharing. Followings are my understanding from the comments as others reference.

(1) loop is left < right, which means inside the loop, left always < right
(2 ) since we use round up for mid, and left < right from (1), right would never be the same as mid
(3) Therefore, we compare mid with right, since they will never be the same from (2)
(4) if nums[mid] < nums[right], we will know the minimum should be in the left part, so we are moving right.
We can always make right = mid while we don't have to worry the loop will not ends. Since from (2), we know right would never be the same as mid, making right = mid will assure the interval is shrinking.
(5) if nums[mid] > nums[right], minimum should be in the right part, so we are moving left. Since nums[mid] > nums[right],mid can't be the minimum, we can safely move left to mid + 1, which also assure the interval is shrinking
"""
print(findMin([3, 1, 2]))
print(findMin([3,4,5,1,2]))
print(findMin([4,5,6,7,0,1,2]))
print(findMin([11,13,15,17]))
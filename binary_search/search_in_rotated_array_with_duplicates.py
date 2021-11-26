"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
"""

# class Solution {
#     public boolean search(int[] nums, int target) {
#         int n = nums.length;
#         if (n == 0) return false;
#         int end = n - 1;
#         int start = 0;

#         while (start <= end) {
#             int mid = start + (end - start) / 2;

#             if (nums[mid] == target) {
#                 return true;
#             }

#             if (!isBinarySearchHelpful(nums, start, nums[mid])) {
#                 start++;
#                 continue;
#             }
#             // which array does pivot belong to.
#             boolean pivotArray = existsInFirst(nums, start, nums[mid]);

#             // which array does target belong to.
#             boolean targetArray = existsInFirst(nums, start, target);
#             if (pivotArray ^ targetArray) { // If pivot and target exist in different sorted arrays, recall that xor is true when both operands are distinct
#                 if (pivotArray) {
#                     start = mid + 1; // pivot in the first, target in the second
#                 } else {
#                     end = mid - 1; // target in the first, pivot in the second
#                 }
#             } else { // If pivot and target exist in same sorted array
#                 if (nums[mid] < target) {
#                     start = mid + 1;
#                 } else {
#                     end = mid - 1;
#                 }
#             }
#         }
#         return false;
#     }

#     // returns true if we can reduce the search space in current binary search space
#     private boolean isBinarySearchHelpful(int[] arr, int start, int element) {
#         return arr[start] != element;
#     }

#     // returns true if element exists in first array, false if it exists in second
#     private boolean existsInFirst(int[] arr, int start, int element) {
#         return arr[start] <= element;
#     }
# }  


def search(nums, target):
	left, right = 0, len(nums) - 1
	while left <= right:
		mid = (left + right) // 2
		if nums[mid] == target:
			return True
		if nums[mid] >= nums[left] and target < nums[mid]:
			right = mid
		else:
			left = mid + 1
	return False


# print('Output -->', search([1], 1))	
# print('Output -->', search([2,5,6,0,0,1,2], 0))	
# print('Output -->', search([1, 0, 1, 1, 1], 0))	
print('Output -->', search([ 180, 181, 182, 183, 184, 187, 188, 189, 191, 192, 193, 194, 195, 196, 201, 202, 203, 204, 3, 4, 5, 6, 7, 8, 9, 10, 14, 16, 17, 18, 19, 23, 26, 27, 28, 29, 32, 33, 36, 37, 38, 39, 41, 42, 43, 45, 48, 51, 52, 53, 54, 56, 62, 63, 64, 67, 69, 72, 73, 75, 77, 78, 79, 83, 85, 87, 90, 91, 92, 93, 96, 98, 99, 101, 102, 104, 105, 106, 107, 108, 109, 111, 113, 115, 116, 118, 119, 120, 122, 123, 124, 126, 127, 129, 130, 135, 137, 138, 139, 143, 144, 145, 147, 149, 152, 155, 156, 160, 162, 163, 164, 166, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177 ], 42))
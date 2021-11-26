"""
https://www.geeksforgeeks.org/next-greater-element/
https://leetcode.com/problems/next-greater-element-ii/
"""

# own version
def nextGreaterElements(nums):
    def find_max(start, end, nums, k):
        for val in nums[start:end]:
            if val > k:
                return val
        return None
    arr_len, output = len(nums), list()
    for index in range(arr_len):
        right = find_max(index + 1, arr_len, nums, nums[index])
        if right is not None:
            output.append(right)
        else:
            left = find_max(0, index, nums, nums[index])
            if left is None:
                output.append(-1)
            else:
                output.append(left)
    return output

#editorial
# public class Solution {

#     public int[] nextGreaterElements(int[] nums) {
#         int[] res = new int[nums.length];
#         Stack<Integer> stack = new Stack<>();
#         for (int i = 2 * nums.length - 1; i >= 0; --i) {
#             while (!stack.empty() && nums[stack.peek()] <= nums[i % nums.length]) {
#                 stack.pop();
#             }
#             res[i % nums.length] = stack.empty() ? -1 : nums[stack.peek()];
#             stack.push(i % nums.length);
#         }
#         return res;
#     }
# }
    

def nextGreaterElements(nums):
    stack, res = [], [-1] * len(nums)
    for i in range(len(nums)):
        while stack and (nums[stack[-1]] < nums[i]):
            res[stack.pop()] = nums[i]
        stack.append(i)
    for i in range(len(nums)):
        while stack and (nums[stack[-1]] < nums[i]):
            res[stack.pop()] = nums[i]
    return res  


print('Output', nextGreaterElements([13, 7, 6, 12]))
# print('Output', nextGreaterElements([4, 5, 2, 25]))
# print('Output', nextGreaterElements([4, 5, 2, 25]))


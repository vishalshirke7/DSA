"""
https://leetcode.com/problems/132-pattern/
"""
import sys

# def find132pattern(nums):
#     stack = []
#     s3 = -float('inf')
#     for n in nums[::-1]:
#         print(n, s3, stack)
#         if n < s3:
#             return True
#         while stack and stack[-1] < n:
#             s3 = stack.pop()
#         stack.append(n)
#     return False

# int third = INT_MIN;
#         stack<int> s;
#         for (int i = nums.size() - 1; i >= 0; -- i) {
#             if (nums[i] < third) return true;
#             while (!s.empty() && nums[i] > s.top()) {
#                 third = s.top(); 
#                 s.pop();
                
#             }
#             s.push(nums[i]);
#         }
#         return false;

def find132pattern(nums):
    length = len(nums)
    if length <= 2:
        return False
    stack = []    
    cur_min = [nums[0]]
    for index in range(1, length):
        cur_min.append(min(nums[index], cur_min[-1]))
    for index in range(length - 1, -1, -1):
        if nums[index] > cur_min[index]:
            while stack and stack[-1] <= cur_min[index]:
                stack.pop()
            if stack and cur_min[index] < stack[-1] < nums[index]:
                return True
            stack.append(nums[index])
    return False


# print('Output', find132pattern([3,1,4,2]))
print('Output', find132pattern([3,5,0,3,4]))   
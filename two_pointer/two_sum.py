"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = list()
        complement_map = dict()
        for i in range(len(nums)):
            if (target - nums[i]) in complement_map:
                indices.append(i)
                indices.append(complement_map[target - nums[i]])
                return indices
            else:
                complement_map[nums[i]] = i
"""
https://leetcode.com/problems/maximum-subarray/
"""

def maxSubArray(nums):
	for i in range(1, len(nums)):
	        if nums[i-1] > 0:
	            nums[i] += nums[i-1]
	return max(nums)

def maxSubArray(nums):
    max_ending_here, max_so_far = 0, -10 ** 5
    for index in range(len(nums)):
        max_ending_here = max_ending_here + nums[index]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here 
            if max_ending_here < 0:
                max_ending_here = 0  
    return max_so_far

print('Output', maxSubArray([-3, -1, -1]))

import  sys

def largest_sum_continuous(array):
    max_sum, current_sum = -sys.maxsize -1, 0
    for i in range(len(array)):
        current_sum += array[i]
        if max_sum < current_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum

def maxSubArray(nums):
    for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

def maxSubArray(nums, size):
    start, end = 0, 0
    cur_sum, max_sum = 0, -10 ** 4
    while end < size:
        cur_sum += nums[end]
        if cur_sum > max_sum:
            max_sum = cur_sum
        if cur_sum < 0:
            cur_sum -= nums[start]
            start += 1
        while cur_sum < 0:
            cur_sum -= nums[start]
            start += 1
        end += 1
    return max_sum

# print(largest_sum_continuous([-4,-5,-2,-1]))
print(maxSubArray([-4,-5,-2,-1], 4))
print(maxSubArray([1,2,3,-2,5], 5))
print(maxSubArray([74,-72,94,-53,-59,-3,-66,36,-13,22,73,15,-52,75], 14))

"""
public static int maxSubArray(int[] A) {
    int maxSoFar=A[0], maxEndingHere=A[0];
    for (int i=1;i<A.length;++i){
        maxEndingHere= Math.max(maxEndingHere+A[i],A[i]);
        maxSoFar=Math.max(maxSoFar, maxEndingHere); 
    }
    return maxSoFar;
}
"""
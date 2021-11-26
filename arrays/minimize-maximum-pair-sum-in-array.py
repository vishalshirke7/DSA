"""
https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
"""


#accepated editorial
def minPairSum(nums):
	nums.sort()
	start, end, ans = 0, len(nums) - 1, 0
	while start < end:
		ans = max(ans, nums[start] + nums[end])
		start += 1
		end -= 1
	return ans

"""
public int minPairSum(int[] nums) {
    int res = Integer.MIN_VALUE;
    Arrays.sort(nums);
    for (int i = 0; i < nums.length / 2; ++i)
        res = Math.max(res, nums[i] + nums[nums.length - i - 1]);
    return res;
}
"""
print('Output', minPairSum([3,5,2,3]))
print('Output', minPairSum([3,5,4,2,4,6]))
print('Output', minPairSum([4,1,5,1,2,5,1,5,5,4]))

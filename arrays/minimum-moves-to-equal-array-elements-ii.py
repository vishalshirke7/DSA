"""
https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
"""
"""https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/discuss/1217473/C%2B%2BPythonJava-2-Solutions-(w-and-wo-Median)-Explained-with-Example-implementation"""

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        mid = n // 2
        nums.sort()
        output = 0
        for num in nums:
            output += abs(num + nums[mid])
        return output


"""
class Solution {
    public int minMoves2 (int[] nums) {
        Arrays.sort (nums);
        int left = 0, right = nums.length - 1, moves = 0;
        while (left < right)
            moves += nums [right--] - nums [left++];
        return moves;
    }
}
"""
"""
https://leetcode.com/problems/non-decreasing-array/
"""

#editorial 
"""
public boolean checkPossibility(int[] nums) {
    int cnt = 0;
    for(int i = 1; i < nums.length && cnt<=1 ; i++){
        if(nums[i-1] > nums[i]){
            cnt++;
            if(i-2<0 || nums[i-2] <= nums[i])nums[i-1] = nums[i];
            else nums[i] = nums[i-1];
        }
    }
    return cnt<=1; 
    }
"""    

def checkPossibility(nums):
    if len(nums) <= 1:
        return True
    violation_count = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            violation_count += 1
            if violation_count == 2:
                return False
            if i - 2 >= 0 and nums[i - 2] > nums[i]: # have to promote nums[i]
                nums[i] = nums[i - 1]
    return True


# print('Output', checkPossibility([4,2,3]))
# print('Output', checkPossibility([4,2,1]))
# print('Output', checkPossibility([5, 7, 1, 8]))
# print('Output', checkPossibility([3, 4, 2, 3]))
print('Output', checkPossibility([2, 4, 3, 3]))
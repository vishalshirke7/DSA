def removeDuplicates(nums):
    if len(nums) < 2:
        return len(nums)
    cur, fast = 0, 1
    while fast < len(nums):
        if nums[fast] <= nums[cur]:
            pass
        else:
            if (cur + 1) != fast:
                nums[cur + 1] = nums[fast]
            if nums[cur + 1] > nums[cur]:
                cur += 1
        fast += 1
    return cur + 1

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

"""
    if (nums.length == 0) return 0;
    int i = 0;
    for (int j = 1; j < nums.length; j++) {
        if (nums[j] != nums[i]) {
            i++;
            nums[i] = nums[j];
        }
    }
    return i + 1;
"""
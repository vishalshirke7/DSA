"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""

"https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/28128/Python-9-lines-2-extra-variables-76ms.-Any-simpler-solution-else"

def removeDuplicates(nums):
    i = 0
    for n in nums:
        if i < 2 or n > nums[i-2]:
            nums[i] = n
            i += 1
    print(nums)
    return i
 

print('Output', removeDuplicates([1,1,1,2,2,2,3,3]))

"""
public int removeDuplicates(int[] nums) {
    		//define at most k times of duplicate numbers
    		final int k = 2;

    		//check if it is an empty array
    		if(nums.length == 0) return 0;

    		//start pointer of new array
    		int m = 1;

    		// count the time of duplicate numbers occurence
    		int count = 1;

    		for(int i = 1; i < nums.length; ++i) {
    			if(nums[i] == nums[i - 1]) {
    				if(count < k) {
    					nums[m++] = nums[i];
    				}
    				count++;
    			} else {
    				count = 1;
    				nums[m++] = nums[i];
    			}
    		}
    		return m;
    	}

"""
"""
    def removeDuplicates(self, nums):
		if len(nums) < 2: return len(nums)
        slow, fast = 2, 2

        while fast < len(nums):
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
"""

"""
int removeDuplicates(vector<int>& nums) {
    int n = nums.size(), count = 0;
    for (int i = 2; i < n; i++)
        if (nums[i] == nums[i - 2 - count]) count++;
        else nums[i - count] = nums[i];
    return n - count;
}
"""

"""
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while i+2<len(nums):
            if nums[i]==nums[i+2]:
                nums.pop(i+2)
            else:
                i=i+1
        return len(nums)

"""        
"""
https://leetcode.com/problems/sort-colors/
"""
"https://leetcode.com/problems/sort-colors/discuss/26500/Four-different-solutions"

def sortColors(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if i != j:
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
    print(nums)

"""
Dutch partitioning algorithm
"""
def sortColors(nums):
    red, white, blue = 0, 0, len(nums)-1    
    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1
    print('Final ', nums)


def sortColors(nums):
    first, last = 0, len(nums) - 1
    for index in range(len(nums) - 1):
        while nums[index] == 2 and index < last:
            nums[index], nums[last] = nums[last], nums[index]
            last -= 1
        while nums[index] == 0 and index > first:
            nums[index], nums[first] = nums[first], nums[index]
            first += 1
    print(nums)

sortColors([2,0,2,1,1,0]) 


def sortColors(nums):
    i = j = 0
    for k in range(len(nums)):
        v = nums[k]
        nums[k] = 2
        if v < 2:
            nums[j] = 1
            j += 1
        if v == 0:
            nums[i] = 0
            i += 1

"""
public void sortColors(int[] nums) {
    int start = 0;
    int end = nums.length - 1;
    int i = 0;
    while (i <= end) {
        if (nums[i] == 0) {
            nums[i]=1;
            nums[start]=0;
            start++;
            i++;
        } else if (nums[i] == 2) {
            nums[i]=nums[end];
            nums[end]=2;
            end--;
        } else {
            i++;
        }
    }
}
"""    


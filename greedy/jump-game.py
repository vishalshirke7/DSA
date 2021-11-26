"""
https://leetcode.com/problems/jump-game/
"""

# own
def check_jumps(nums):
    current_end, current_farthest = 0, 0
    for index in range(len(nums)):
        current_farthest = max(current_farthest, index + nums[index])
        if current_end == index:
            if current_farthest == current_end:
                break
            else:
                current_end = current_farthest
    if current_end < len(nums) - 1:
        return False
    return True


# print(check_jumps([3, 2, 1, 0, 4]))
print(check_jumps([2, 3, 0, 1, 4, 1]))
# print(check_jumps([1, 4, 3, 7, 1, 2, 6, 7, 6, 10]))

"""
OWN version:

def check_jumps(nums):
    N = len(nums)
    jump_index = N - 1
    for index in range(N - 2, 0 , -1):
        if abs(index - jump_index) <= nums[index]:
            jump_index = index
    if abs(0 - jump_index) <= nums[0]:
        return True
    return False
"""
"""
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for index, number in enumerate(nums):
            if index > farthest:
                return False
            farthest = max(farthest, index + number)
        return True
"""
"""
def canJump(self, nums):
    m = 0
    for i, n in enumerate(nums):
        if i > m:
            return False
        m = max(m, i+n)
    return True

"""    
"""
def canJump(self, nums):
    goal = len(nums) - 1
    for i in range(len(nums))[::-1]:
        if i + nums[i] >= goal:
            goal = i
    return not goal
"""

"""
bool canJump(int A[], int n) {
    int i = 0;
    for (int reach = 0; i < n && i <= reach; ++i)
        reach = max(i + A[i], reach);
    return i == n;
}
"""

"""
bool canJump(int A[], int n) {
    int last=n-1,i,j;
    for(i=n-2;i>=0;i--){
        if(i+A[i]>=last)last=i;
    }
    return last<=0;
}
"""
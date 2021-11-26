"""
https://leetcode.com/problems/jump-game-ii/
"""

"""
https://leetcode.com/problems/jump-game-ii/discuss/18019/10-lines-C%2B%2B-(16ms)-Python-BFS-Solutions-with-Explanations
https://leetcode.com/problems/jump-game-ii/discuss/170518/8-Lines-in-Python!-Easiest-Solution!
https://leetcode.com/problems/jump-game-ii/discuss/18035/Easy-Python-Greedy-solution-with-explanation
"""

def calculate_jumps(nums):
    array_length = len(nums)
    if array_length <= 1:
        return 0
    jump, ladder, stairs = 1, nums[0], nums[0]
    for index in range(1, array_length):
        if index == array_length - 1:
            return jump
        if index + nums[index] > ladder:
            ladder = index + nums[index]
        stairs -= 1
        if stairs == 0:
            jump += 1
            stairs = ladder - index
    return jump

# BFS
def calculate_jumps(nums):
    jump, current_end, current_farthsest = 0, 0, 0
    for index in range(len(nums) - 1):
        current_farthsest = max([current_farthsest, index + nums[index]])
        if current_end == index:
            jump += 1
            current_end = current_farthsest
    return jump


def jump(nums):
    if len(nums) <= 1: return 0
    l, r = 0, nums[0]
    times = 1
    while r < len(nums) - 1:
        times += 1
        nxt = max(i + nums[i] for i in range(l, r + 1))
        l, r = r, nxt
    return times

# print(calculate_jumps([2, 3, 1, 1, 4]))
print(calculate_jumps([1, 4, 3, 7, 1, 2, 6, 7, 6, 10]))

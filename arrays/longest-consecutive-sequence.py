
def longestConsecutive(nums):
    longest_streak = 0
    nums_map = dict(map(lambda num: (num, 1), nums))
    for num in nums:
        if num - 1 not in nums_map:
            current_num = num
            current_streak = 1
            while current_num + 1 in nums_map:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
    return longest_streak


def longestConsecutive(nums):
    longest_streak = 0
    nums_set = set(nums)
    for num in nums:
        if num - 1 not in nums_set:
            y = num + 1
            while y in nums_set:
                y += 1
            longest_streak = max(longest_streak, y - num)
    return longest_streak    


print(longestConsecutive([100,4,200,1,3,2]))
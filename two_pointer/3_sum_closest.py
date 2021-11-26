import  bisect

def three_sum_closest(nums, target):
    nums.sort()
    cur_sum = 0
    cur_min = 9999999999
    for i in range(len(nums)):
        start, end = i+1, len(nums) - 1
        while start < end:
            total = nums[i] + nums[start] + nums[end]
            diff = abs(total - target)
            if diff < cur_min:
                cur_min = diff
                cur_sum = total
            if total > target:
                end -= 1
            else:
                start += 1
    return cur_sum

print("TWO POINTERS", three_sum_closest([1, 1, -1], 2))


def three_sum_closest_binary(nums, target):
    diff = float('inf')
    nums.sort()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            complement = target - nums[i] - nums[j]
            hi = bisect.bisect_right(nums, complement, j + 1)
            lo = hi - 1
            if hi < len(nums) and abs(complement - nums[hi]) < abs(diff):
                diff = complement - nums[hi]
            if lo > j and abs(complement - nums[lo]) < abs(diff):
                diff = complement - nums[lo]
        if diff == 0:
            break
    return target - diff

print("BINARY SEARCH", three_sum_closest_binary([1, 1, -1], 2))
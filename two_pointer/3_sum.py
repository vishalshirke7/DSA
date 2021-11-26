def threeSum(nums):
    nums.sort()
    output_set = set()
    output_list = list()
    for i in range(len(nums)):
        start, end = i+1, len(nums) - 1
        while start < end:
            a, b, c = nums[i], nums[start], nums[end]
            total = (a + b + c)
            if total == 0:
                if (a, b, c) not in output_set:
                    output_set.add((a, b, c))
                    output_list.append([a, b, c])
                start += 1
            elif total > 0:
                end -= 1
            else:
                start += 1
    return output_list

print(threeSum([0]))
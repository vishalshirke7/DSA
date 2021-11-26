"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
https://www.interviewbit.com/old/problems/search-for-a-range/
"""
def find_boundary(nums, target, is_first=False):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            if is_first:
                if (mid - 1) >=0 and nums[mid - 1] == target:
                    end = mid - 1
                else:
                    return mid
            else:
                if (mid + 1) <= len(nums) - 1 and nums[mid + 1] == target:
                    start = mid + 1
                else:
                    return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1
    
    
def searchRange(nums, target):
    output_list = list()
    first_occur = find_boundary(nums, target, is_first=True)
    if first_occur == -1:
        return [-1, -1]
    output_list.append(first_occur)
    output_list.append(find_boundary(nums, target))
    return output_list


def searchRange(nums, target):
    if not nums:
        return [-1, -1]

    def bisect_left(nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l if nums[l] == target else -1

    def bisect_right(nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2 + 1
            if nums[m] > target:
                r = m - 1
            else:
                l = m
        return l if nums[l] == target else -1

    return [bisect_left(nums, target), bisect_right(nums, target)]

print(searchRange([1], 1))
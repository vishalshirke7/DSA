"""
https://leetcode.com/problems/search-insert-position/
https://www.interviewbit.com/problems/sorted-insert-position/
"""


def searchInsert(array, target):
    start, end = 0, len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start += 1
        else:
            end = mid - 1
    return end + 1

print(searchInsert([1,3,5,6], 2))
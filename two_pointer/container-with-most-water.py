"""
https://leetcode.com/problems/container-with-most-water/
https://www.interviewbit.com/problems/container-with-most-water/
"""
def max_area_2(height):
    l, r, max_area = 0, len(height) - 1, 0
    while l < r:
        if height[l] < height[r]:
            max_area = max(max_area, height[l] * (r - l))
            l += 1
        else:
            max_area = max(max_area, height[r] * (r - l))
            r -= 1
    return max_area


print(max_area_2([1,8,6,2,5,4,8,3,7]))



# def max_area_1(height):
#     current_area = 0
#     max_area = -1
#     l, r = 0, len(height) - 1
#     while l < r:
#         print(l, r)
#         distance = r - l 
#         min_of_both = min(height[l], height[r])
#         max_area = max(max_area, min_of_both * distance)
#         if height[l] < height[r]:
#             l += 1
#         elif height[l] > height[r]:
#             r -= 1
#         else:
#             l += 1
#     return max_area


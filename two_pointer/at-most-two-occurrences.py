"""
https://www.interviewbit.com/old/problems/at-most-two-occurrences/
"""

def solve(A):
    count_map = {}
    for val in A:
        count_map[val] = count_map.get(val, 0) + 1
    special_count = 0
    for val in count_map:
        if count_map[val] > 2:
            special_count += 1
    if special_count == 0:
        return 0
    end, arr_len = -1, len(A)
    ans = arr_len
    for index in range(arr_len):
        while end + 1 < arr_len and special_count:
            end += 1
            count_map[A[end]] -= 1
            if count_map[A[end]] == 2:
                special_count -= 1
        if special_count == 0:
            ans = min(ans, end - index + 1)
        count_map[A[index]] += 1
        if count_map[A[index]] == 3:
            special_count += 1
    return ans
            

print('Output', solve([ 68, 35, 1, 70, 25, 79, 59, 63, 65, 6, 46, 82, 28, 62, 92, 96, 43, 28, 37, 92, 5, 3, 54, 93, 83, 22, 17, 19, 96, 48, 27, 72, 39, 70, 13, 68, 100, 36, 95, 4, 12, 23, 34, 74, 65, 42, 12, 54, 69, 48, 45 ]))
print('Output', solve([1, 1, 1, 2, 2, 2]))
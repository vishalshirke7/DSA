"""
https://www.interviewbit.com/old/problems/woodcutting-made-easy/
"""

def solve(A, B):

    def can_cut(height):
        distance = 0
        for val in A:
            if val > height:
                distance += val - height
        if distance < B:
            return False
        return True

    start, end, ans = 0, max(A), 0
    A.sort()
    while start <= end:
        mid = (start + end) // 2
        if can_cut(mid):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans


print('Output', solve([ 62, 117, 149, 85, 144, 53, 61, 72, 83, 123, 114, 91, 61, 103 ], 68))
print('Output', solve([ 114, 55, 95, 131, 77, 111, 141 ], 95))
print('Output', solve([20, 15, 10, 17], 7))
print('Output', solve([4, 42, 40, 26, 46], 20))

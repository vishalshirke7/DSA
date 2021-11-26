"""
https://www.interviewbit.com/old/problems/painters-partition-problem/
"""


def paint(A, B, C):
    
    def is_possible(time):
        cur_sum, painters = 0, A
        for val in C:
            cur_sum += (val * B)
            if cur_sum > time:
                painters -= 1
        return painters >= 0
        
    start, end, ans = 1, sum(C) * B, 1
    while start < end:
        mid = (start + end) // 2
        if is_possible(mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    print(ans)
    return ans % 10000003




print('Output', paint(2,5, [1,10]))
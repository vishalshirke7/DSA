"""
https://www.interviewbit.com/problems/minimum-appends-for-palindrome/
"""

def solve(A):

    def check(st):
        s, e = 0, len(st) - 1
        while s < e:
            if st[s] != st[e]:
                return 0
            s += 1
            e -= 1
        return 1

    if check(A):
    	return 0
    st_len = len(A) - 1
    last_char = A[-1]
    for index in range(st_len - 1, -1, -1):
        if A[index] == last_char:
            if check(A[index:]):
                return st_len - (st_len - index)
            else:
                return st_len
    return st_len



print('Output', solve("aabaa"))
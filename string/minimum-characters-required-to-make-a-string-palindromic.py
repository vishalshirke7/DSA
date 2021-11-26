"""
https://www.interviewbit.com/old/problems/minimum-characters-required-to-make-a-string-palindromic/
"""
# editorial
def solve(A):
    if len(A) <= 1:
        return 0
    i, j, j_start = 0, len(A) - 1, len(A) - 1
    while i < j:
        if A[i] == A[j]:
            i += 1
            j -= 1
        else:
            j = j_start - 1
            j_start -= 1
            i = 0
    return len(A) - 1 - j_start

#own
def shortestPalindrome(s):
    def is_palindrome(ip):
        s, e = 0 , len(ip) - 1
        while s <= e:
            if ip[s] != ip[e]:
                return 0
            s += 1
            e -= 1
        return 1
    if is_palindrome(s):
        return s
    start, end = 0, len(s) - 1
    while start < end:
        if s[start] == s[end]:
            if is_palindrome(s[start: end + 1]):
                return s[len(s) - 1:end:-1] + s
        end -= 1
    if start == end:
        return s[len(s) - 1:0:-1] + s
                

def solve(A):
    def is_palindrome(ip):
        s, e = 0 , len(ip) - 1
        while s <= e:
            if ip[s] != ip[e]:
                return 0
            s += 1
            e -= 1
        return 1
    if is_palindrome(A):
        return 0
    size = len(A) - 1
    last_char = A[0]
    for index in range(1, len(A)):
        if A[index] == last_char:
            if is_palindrome(A[:index + 1]):
                return size - index
            else:
                size
    return size

print('Output', shortestPalindrome("abcd"))    
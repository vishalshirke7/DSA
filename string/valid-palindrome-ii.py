"""
https://leetcode.com/problems/valid-palindrome-ii/
"""

def validPalindrome(s): 

    def is_palindrome(arr, start, end):
        while start < end:
            if arr[start] != arr[end]:
                return False
            start += 1
            end -= 1
        return True    

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
        left += 1
        right -= 1
    return True

# def validPalindrome(s):
#     left, right = 0, len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             one, two = s[left:right], s[left + 1:right + 1]
#             return one == one[::-1] or two == two[::-1]
#         left, right = left + 1, right - 1
#     return True



print('Output', validPalindrome("abca"))
# ececabbacec

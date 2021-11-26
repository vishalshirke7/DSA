"""
https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/
"""

class Solution:

    def longestKSubstr(self, s, k):
        start = 0
        cur_char_count = dict()
        longest_substr = -1
        for end, char in enumerate(s):
            cur_char_count[char] = cur_char_count.get(char, 0) + 1
            if cur_char_count[char] == 1:
                k -= 1
            while k < 0:
                cur_char_count[s[start]] -= 1
                if cur_char_count[s[start]] == 0:
                    k += 1
                start += 1
            if k == 0:
                longest_substr = max(longest_substr, end - start + 1)
        return longest_substr
"""
https://leetcode.com/problems/minimum-window-substring/
"""

import collections
from collections import Counter

def minWindow(s, t):

	def is_target_found(target_len):
		return target_len == 0

	t_count = collections.Counter(t)
	start, target_len, min_window = 0, len(t), ""
	for end, char in enumerate(s):
		print(t_count, char)
		if t_count[char] > 0:
			target_len -= 1
		t_count[char] -= 1
		while is_target_found(target_len):
			cur_window_len = end - start + 1
			if not min_window or len(min_window) > cur_window_len:
				min_window = s[start: end + 1]
			t_count[s[start]] += 1
			if t_count[s[start]] > 0:
				target_len += 1
			start += 1
	return min_window


def minWindow(s, t):
    dict_t = Counter(t)
    required = len(dict_t)
    l, r = 0, 0
    # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
    # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
    formed = 0
    # Dictionary which keeps a count of all the unique characters in the current window.
    window_counts = {}
    # ans tuple of the form (window length, left, right)
    ans = float("inf"), None, None
    while r < len(s):
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1
        # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1
        # Try and contract the window till the point where it ceases to be 'desirable'.
        while l <= r and formed == required:
            character = s[l]
            # Save the smallest window until now.
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
            # The character at the position pointed by the `left` pointer is no longer a part of the window.
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1
            # Move the left pointer ahead, this would help to look for a new window.
            l += 1    
        # Keep expanding the window once we are done contracting.
        r += 1    
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


def minWindow(s, t):
    need, missing = Counter(t), len(t)
    i = I = J = 0
    for j, c in enumerate(s, 1):
        missing -= need[c] > 0
        need[c] -= 1
        if not missing:
            while need[s[i]] < 0: need[s[i]] += 1; i += 1
            if not J or j - i <= J - I: I, J = i, j
            need[s[i]] += 1; i += 1; missing += 1       # SPEEEEEEEED UP!
    return s[I : J]

print('Output', minWindow("ADOBECODEBANC", "ABC"))	
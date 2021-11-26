"""
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
"""

def numberOfSubstrings(s):
	count_map = {char: 0 for char in 'abc'}
	start, end, ans, s_len = 0, 0, 0, len(s)
	count_map[s[0]] += 1
	while start <= end:
		if all(count_map.values()):
			ans += s_len - end
			count_map[s[start]] -= 1
			start += 1
		else:
			end += 1
			if end == s_len:
				break
			count_map[s[end]] += 1
	return ans



print('Output', numberOfSubstrings("abcabc"))
print('Output', numberOfSubstrings("aaacb"))
print('Output', numberOfSubstrings("abc"))
"""
https://leetcode.com/problems/longest-repeating-character-replacement/

https://leetcode.com/problems/longest-repeating-character-replacement/discuss/363071/Simple-Python-two-pointer-solution
"""


# def characterReplacement(s, k):
# 	output, start, max_char, char_count_map = 0, 0, 0, dict()
# 	for index in range(len(s)):
# 		char_count_map[s[index]] = char_count_map.get(s[index], 0) + 1
# 		max_char = max(max_char, char_count_map[s[index]])
# 		if index - start + 1 - max_char > k:
# 			char_count_map[s[start]] -= 1
# 			start += 1
# 		output = max(output, index - start + 1)
# 	return output


def characterReplacement(s, k):
	if len(s) <= 1:
		return 1
	max_len = -float('inf')
	start, end = 0, 1
	while start <= end and end < len(s):
		if s[start] != s[end]:
			k -= 1
		cur_char = s[start] 
		while k < 0:
			if s[start] != cur_char:
				k += 1
			if k != 0:
				start += 1
		max_len = max(max_len, end - start + 1)
		end += 1
	return max_len

# print(characterReplacement("ABAB", 2))
# print(characterReplacement("AABABBA", 1))
# print(characterReplacement("AABABABBAA", 3))
# print(characterReplacement("ABAA", 0))
# print(characterReplacement("BAAA", 0))
print(characterReplacement("ABBB", 2))
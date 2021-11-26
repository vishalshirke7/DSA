"""
https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/
"""


def numSmallerByFrequency(queries, words):
	queries_len = len(queries)
	ans = [0] * queries_len
	queries_cnt, words_cnt = list(), list()
	for query in queries:
		small_char = None
		char_map = dict()		
		for char in query:
			if small_char:
				small_char = min(small_char, char)
			else:
				small_char = char
			char_map[char] = char_map.get(char, 0) + 1
		queries_cnt.append(char_map[small_char])
	for word in words:
		small_char = None
		char_map = dict()
		for char in word:
			if small_char:
				small_char = min(small_char, char)
			else:
				small_char = char
			char_map[char] = char_map.get(char, 0) + 1
		words_cnt.append(char_map[small_char])
	words_cnt.sort()
	# print(queries_cnt, words_cnt)
	for query_cnt in queries_cnt:
		start, end = 0, len(words_cnt) - 1
		while start < end:
			mid = (start + end) // 2
			if words_cnt[mid] > query_cnt:
				end  = mid - 1
			else:
				start = mid + 1
		ans[0] = len(queries_cnt) - end
	return ans


# print('Output', numSmallerByFrequency(["cbd"], ["zaaaz"]))
print('Output', numSmallerByFrequency(["bbb","cc"], ["a","aa","aaa","aaaa"]))
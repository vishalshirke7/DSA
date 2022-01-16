"""
https://leetcode.com/problems/word-subsets/
"""

# O(A + B)
def wordSubsets(words1, words2):
    ans = list()
    def char_count(word):
        char_count = dict()
        for char in word:
            char_count[char] = char_count.get(char, 0) + 1
        return char_count

    combined_word2_map = dict()
    for word2 in words2:
        word2_map = char_count(word2)
        for char, count in word2_map.items():
            combined_word2_map[char] = max(combined_word2_map.get(char, 0), count)
    for word1 in words1:
        is_universal = True
        word1_map = char_count(word1)
        for char, count in combined_word2_map.items():
            if char not in word1_map or word1_map[char] < count:
                is_universal = False
                break
        if is_universal:
            ans.append(word1)
    return ans


print('Output', wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))    
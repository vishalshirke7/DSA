"""
https://www.interviewbit.com/old/problems/anagrams/
"""
from collections import Counter

def anagrams(A):
    visited = set()
    anagrams = list()
    for index_i in range(len(A)):
        if index_i not in visited:
            index_i_angram = [index_i + 1]
            index_i_char = Counter(A[index_i])
            for index_j in range(index_i + 1, len(A)):
                if not len(A[index_i]) == len(A[index_j]):
                    continue
                index_j_char = Counter(A[index_j])
                if index_i_char == index_j_char:
                    index_i_angram.append(index_j + 1)
                    visited.add(index_j)
            anagrams.append(index_i_angram)
    return anagrams


# OWN
    # def anagrams(self, A):
    #     visited = set()
    #     anagrams = list()
    #     for index_i in range(len(A)):
    #         if index_i not in visited:
    #             index_i_char = dict()
    #             index_i_angram = list()
    #             index_i_length = len(A[index_i])
    #             index_i_angram.append(index_i + 1)
    #             for char_i in A[index_i]:
    #                 index_i_char[char_i] = index_i_char.get(char_i, 0) + 1
    #             for index_j in range(index_i + 1, len(A)):
    #                 if not index_i_length == len(A[index_j]):
    #                     continue
    #                 is_angram = True
    #                 index_j_char = dict()
    #                 for char_j in A[index_j]:
    #                     if char_j in index_i_char:
    #                         index_j_char[char_j] = index_j_char.get(char_j, 0) + 1
    #                     else:
    #                         is_angram = False
    #                         break
    #                 if is_angram and len(index_i_char.keys()) == len(index_j_char.keys()):
    #                     for char, val in index_i_char.items():
    #                         if index_j_char[char] != val:
    #                             is_angram = False
    #                     if is_angram:
    #                         index_i_angram.append(index_j + 1)
    #                         visited.add(index_j)
    #             anagrams.append(index_i_angram)
    #     return anagrams
                    

print('Output', anagrams([ "cat", "dog", "god", "tca" ]))
print('Output', anagrams([ "abbbaabbbabbbbabababbbbbbbaabaaabbaaababbabbabbaababbbaaabbabaabbaabbabbbbbababbbababbbbaabababba", "abaaabbbabaaabbbbabaabbabaaaababbbbabbbaaaabaababbbbaaaabbbaaaabaabbaaabbaabaaabbabbaaaababbabbaa", "babbabbaaabbbbabaaaabaabaabbbabaabaaabbbbbbabbabababbbabaabaabbaabaabaabbaabbbabaabbbabaaaabbbbab", "bbbabaaabaaaaabaabaaaaaaabbabaaaabbababbabbabbaabbabaaabaabbbabbaabaabaabaaaabbabbabaaababbaababb", "abbbbbbbbbbbbabaabbbbabababaabaabbbababbabbabaaaabaabbabbaaabbaaaabbaabbbbbaaaabaaaaababababaabab", "aabbbbaaabbaabbbbabbbbbaabbababbbbababbbabaabbbbbbababaaaabbbabaabbbbabbbababbbaaabbabaaaabaaaaba", "abbaaababbbabbbbabababbbababbbaaaaabbbbbbaaaabbaaabbbbbbabbabbabbaabbbbaabaabbababbbaabbbaababbaa", "aabaaabaaaaaabbbbaabbabaaaabbaababaaabbabbaaaaababaaabaabbbabbababaabababbaabaababbaabbabbbaaabbb" ]))
# print('Output', anagrams([ "abbabbaa", "abaaaaba", "aaaaabba", "aabaaaba", "baabbaab", "abbaabbb", "bababaab", "bbabaaab", "bbaaaabb", "aaabbbba", "abbbbabb", "abbaaaba", "babbbbab", "abaaaabb", "baaababb", "aaaaaaaa", "abbbbbbb", "abbaaaba", "baabaabb", "babbbaaa", "baababaa", "babaabaa", "abaabbaa", "abbbabab", "aaaaabba", "aabaaabb", "abbbbaba", "bbaaabaa", "babbbbbb", "bababbba", "aabababa", "aabbaabb", "ababbaba", "abbbabaa", "babaabbb", "ababaaaa", "aaabbaab", "ababaaba", "bbaabbba", "ababaabb", "ababbaba", "bbabbaaa", "aaabbaaa", "bbaaaaaa", "baababbb", "bbaabbab", "bbbabaaa", "bbbabbaa", "baaaaabb", "bbabaabb", "bbaabbbb", "bbaaabba", "baababaa", "baaabbab", "abbbbbaa", "aaaaabaa", "babbabbb", "aabbaabb", "bbbababb", "bbaaaaab", "aabababb", "aabbaabb", "bbabbbba", "aabbabba" ]))

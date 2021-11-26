"""
https://leetcode.com/problems/group-anagrams/
"""


def groupAnagrams(strs)
    str_index_map = dict()
    for index, val in enumerate(strs):
        sorted_val = "".join(sorted(list(val)))
        if sorted_val in str_index_map:
            str_index_map[sorted_val].append(val)
        else:
            str_index_map[sorted_val] = [val]
    return list(str_index_map.values())
"""
https://leetcode.com/problems/partition-labels/
"""

def partitionLabels(input_str):
	start, end, parts = 0, 0, list()
	last_occurence = {character: index for index, character in enumerate(input_str)}
	for index, character in enumerate(input_str):
		end = max(end, last_occurence[character])
		if index == end:
			parts.append(index - start + 1)
			start = index + 1
	return parts


print('Output', partitionLabels('ababcbacadefegdehijhklij'))
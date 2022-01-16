"""
https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
"""

def findLeastNumOfUniqueInts(arr, k):
	char_count = dict()
	for value in arr:
		char_count[value] = char_count.get(value, 0) + 1
	data = sorted(char_count.items(), key=lambda x:x[1])
	for val in data:
		if val[1] - k <= 0:
			k -= val[1]
			del char_count[val[0]]
		elif val[1] - k > 0:
			break
	return len(char_count.keys())


print('Output', findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3))
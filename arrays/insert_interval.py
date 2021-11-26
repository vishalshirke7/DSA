"""
https://leetcode.com/problems/insert-interval/
"""


def insert(intervals, newInterval):
	if not intervals:
		return [newInterval]
	output = []
	for index, interval in enumerate(intervals):
		if interval[1] < newInterval[0]:
			output.append(interval)
		elif newInterval[1] < interval[0]:
			output.append(newInterval)
			return output + intervals[index:]
		else:
			newInterval[0] = min(newInterval[0], interval[0])
			newInterval[1] = max(newInterval[1], interval[1])
	output.append(newInterval)
	return output

def insert(intervals, newInterval):
	if not intervals:
		return [newInterval]
	intervals.append(newInterval)
	output = list()
	for interval in sorted(intervals, key=lambda val:val[0]):
		if output and output[-1][1] >= interval[0]:
			output[-1][1] = max(interval[1], output[-1][1])
		else:
			output.append(interval)
	return output

print('Output', insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
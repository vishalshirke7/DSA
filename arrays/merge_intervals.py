"""
https://leetcode.com/problems/merge-intervals/
"""




def merge(intervals):
	merged = list()
	intervals.sort(key=lambda x: x[0])
	for interval in intervals:
		if not merged or merged[-1][1] < interval[0]:
			merged.append(interval)
		else:
			merged[-1][1] = max(merged[-1][1], interval[1])			
	return merged

print('Final Interval', merge([[1,3],[2,6],[8,10],[15,18]]))



def merge(intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i.start):
        if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out += i,
    return out
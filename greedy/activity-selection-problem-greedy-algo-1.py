"""
https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/
"""

def maximumMeetings(n,start,end):
	stack = list()
	combined = list()
	for index in range(len(start)):
		combined.append([start[index], end[index]])
	combined = sorted(combined, key=lambda x:x[0])
	for val in combined:
		if stack and stack[-1][1] >= val[1]:
			stack.pop()
		stack.append(val)
	print(stack)



print('Output', maximumMeetings(6, [1,3,0,5,8,5], [2,4,6,7,9,9]))	
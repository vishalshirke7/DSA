"""
https://leetcode.com/problems/task-scheduler/
"""




def leastInterval(tasks, n):
	tasks_len = len(tasks)
	if tasks_len == n:
		return tasks_len
	char_count = dict()
	for char in tasks:
		char_count[char] = char_count.get(char, 0) + 1
	char_count = sorted(char_count.items(), key=lambda x:x[0])
	start, end = 0, len(char_count) - 1
	all_finish = False
	while start <= end and not all_finish:
		



print('Output', leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
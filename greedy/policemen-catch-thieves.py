"""
https://www.geeksforgeeks.org/policemen-catch-thieves/
"""


def policeThief(arr, n, k):
	police, thief, output = list(), list(), 0
	for index in range(len(arr)):
		if arr[index] == 'P':
			police.append(index)
		else:
			thief.append(index)
	police_index, thief_index = 0, 0
	while police_index < len(police) and thief_index < len(thief):
		if abs(police[police_index] - thief[thief_index]) <= k:
			output += 1
			police_index += 1
			thief_index += 1
		elif thief[thief_index] < police[police_index]:
			thief_index += 1
		else:
			police_index += 1
	return output


print('Output', policeThief(['P', 'T', 'T', 'P', 'T'], 5, 1))
print('Output', policeThief(['T', 'T', 'P', 'P', 'T', 'P'], 6, 2))
print('Output', policeThief(['P', 'T', 'P', 'T', 'T', 'P'], 6, 3))

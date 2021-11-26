"""
https://www.interviewbit.com/problems/kth-row-of-pascals-triangle/
"""


def getRow(A):
	rows = list()
	single_row = list()
	for index_i in range(A + 1):
		for index_j in range(index_i + 1):
			if index_j == 0 or index_i == index_j:
				single_row.append(1)
			else:
				single_row.append(rows[index_i - 1][index_j - 1] + rows[index_i - 1][index_j])
		rows.append(single_row)
		single_row = list()
	return rows[A]



print('Output', getRow(4))	